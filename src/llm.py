# src/llm.py
import os
import json
import requests
from datetime import datetime
from logger import LOG


class LLM:
    def __init__(self, config):
        """
        初始化 LLM 类，根据配置选择使用的模型（OpenAI 或 Ollama）。

        :param config: 配置对象，包含所有的模型配置参数。
        """
        self.config = config
        self.model = config.llm_model_type.lower()  # 获取模型类型并转换为小写
        if self.model == "openai":
            from openai import OpenAI  # 导入OpenAI库用于访问GPT模型
            self.client = OpenAI()  # 创建OpenAI客户端实例
        elif self.model == "ollama":
            self.api_url = config.ollama_api_url  # 设置Ollama API的URL
        else:
            raise ValueError(f"Unsupported model type: {self.model}")  # 如果模型类型不支持，抛出错误

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
        生成报告，根据配置选择不同的模型来处理请求。

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

        # 准备消息列表，包含系统提示和用户内容
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
            LOG.debug(f"Prompt已保存到 {filename}")
            return "DRY RUN"

        # 根据选择的模型调用相应的生成报告方法
        if self.model == "openai":
            return self._generate_report_openai(messages, report_type)
        elif self.model == "ollama":
            return self._generate_report_ollama(messages, report_type)
        else:
            raise ValueError(f"Unsupported model type: {self.model}")

    def _generate_report_openai(self, messages, report_type):
        """
        使用 OpenAI GPT 模型生成报告。

        :param messages: 包含系统提示和用户内容的消息列表。
        :param report_type: 报告类型，用于日志记录。
        :return: 生成的报告内容。
        """
        LOG.info(f"使用 OpenAI GPT 模型开始生成{report_type}报告。")
        try:
            response = self.client.chat.completions.create(
                model=self.config.openai_model_name,  # 使用配置中的OpenAI模型名称
                messages=messages,
                temperature=0.3
            )
            LOG.debug("GPT response: {}", response)
            return response.choices[0].message.content  # 返回生成的报告内容
        except Exception as e:
            LOG.error(f"生成报告时发生错误：{e}")
            raise

    def _generate_report_ollama(self, messages, report_type):
        """
        使用 Ollama LLaMA 模型生成报告。

        :param messages: 包含系统提示和用户内容的消息列表。
        :param report_type: 报告类型，用于日志记录。
        :return: 生成的报告内容。
        """
        LOG.info(f"使用 Ollama 托管模型服务开始生成{report_type}报告。")
        try:
            payload = {
                "model": self.config.ollama_model_name,  # 使用配置中的Ollama模型名称
                "messages": messages,
                "stream": False
            }
            response = requests.post(self.api_url, json=payload)  # 发送POST请求到Ollama API
            response_data = response.json()

            # 调试输出查看完整的响应结构
            LOG.debug("Ollama response: {}", response_data)

            # 直接从响应数据中获取 content
            message_content = response_data.get("message", {}).get("content", None)
            if message_content:
                return message_content  # 返回生成的报告内容
            else:
                LOG.error("无法从响应中提取报告内容。")
                raise ValueError("Invalid response structure from Ollama API")
        except Exception as e:
            LOG.error(f"生成报告时发生错误：{e}")
            raise


if __name__ == '__main__':
    from config import Config  # 导入配置管理类
    config = Config()
    llm = LLM(config)

    markdown_content = """
# Progress for langchain-ai/langchain (2024-08-20 to 2024-08-21)


## Issues Closed in the Last 1 Days
- partners/chroma: release 0.1.3 #25599
- docs: few-shot conceptual guide #25596
- docs: update examples in api ref #25589
"""

    report = llm.generate_daily_report(markdown_content, dry_run=False)
    print(report)
