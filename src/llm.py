# src/llm.py
import os
import json
from datetime import datetime
from openai import OpenAI
from logger import LOG


class LLM:
    def __init__(self):
        self.client = OpenAI()

        # 加载所有提示词
        self.system_prompts = {}

        # 加载GitHub报告提示词
        try:
            with open("prompts/report_prompt.txt", "r", encoding='utf-8') as file:
                self.system_prompts['github'] = file.read()
            LOG.info("已加载GitHub报告提示词")
        except Exception as e:
            LOG.error(f"加载GitHub提示词失败: {e}")
            self.system_prompts['github'] = ""  # 如果文件不存在，使用空字符串

        # 加载HackerNews报告提示词
        try:
            with open("prompts/hackernews_prompt.txt", "r", encoding='utf-8') as file:
                self.system_prompts['hackernews'] = file.read()
            LOG.info("已加载HackerNews报告提示词")
        except Exception as e:
            LOG.error(f"加载HackerNews提示词失败: {e}")
            self.system_prompts['hackernews'] = ""  # 如果文件不存在，使用空字符串

    def generate_daily_report(self, content, report_type='github', dry_run=False):
        """
        生成报告

        Args:
            content: 用户消息内容
            report_type: 报告类型，'github' 或 'hackernews'，默认为 'github'
            dry_run: 是否为试运行模式
        """
        # 根据 report_type 选择对应的系统提示词
        system_prompt = self.system_prompts.get(report_type, "")

        if not system_prompt:
            LOG.error(f"未找到 {report_type} 类型的提示词文件")
            return f"错误：无法生成{report_type}报告，提示词文件不存在"

        messages = [
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": content},
        ]

        if dry_run:
            LOG.info(f"Dry run mode enabled for {report_type} report. Saving prompt to file.")
            filename = f"daily_progress/prompt_{report_type}_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"
            os.makedirs('daily_progress', exist_ok=True)
            with open(filename, "w+", encoding='utf-8') as f:
                json.dump(messages, f, indent=4, ensure_ascii=False)
            return "DRY RUN"

        LOG.info(f"使用模型开始生成{report_type}报告。")

        try:
            response = self.client.chat.completions.create(
                model="deepseek-chat",
                messages=messages,
                temperature=0.3
            )
            return response.choices[0].message.content
        except Exception as e:
            LOG.error(f"生成报告时发生错误：{e}")
            raise