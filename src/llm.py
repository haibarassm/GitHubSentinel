import os
from openai import OpenAI  # 导入OpenAI库用于访问GPT模型
from logger import LOG  # 导入日志模块

class LLM:
    def __init__(self):
        # 创建一个OpenAI客户端实例
        self.client = OpenAI()
        # 配置日志文件，当文件大小达到1MB时自动轮转，日志级别为DEBUG
        LOG.add("daily_progress/llm_logs.log", rotation="1 MB", level="DEBUG")

    def generate_daily_report(self, markdown_content, dry_run=False):
        # 构建一个用于生成报告的提示文本，要求生成的报告包含新增功能、主要改进和问题修复
        # prompt = f"以下是项目的最新进展，根据功能合并同类项，形成一份简报，至少包含：1）新增功能；2）主要改进；3）修复问题；:\n\n{markdown_content}"
        system_prompt = """
        你是一名资深软件项目经理助理，擅长整理技术变更记录和开发日志。

        你的任务是：
        1. 从给定的项目进展内容中提取有效信息
        2. 合并同类功能
        3. 去除重复描述
        4. 按类别归纳输出

        输出必须满足以下要求：
        - 使用 Markdown 格式
        - 必须包含以下三个一级标题：
          ## 新增功能
          ## 主要改进
          ## 问题修复
        - 每个标题下使用无序列表
        - 内容要简洁专业
        - 不要编造内容
        - 如果某类没有内容，写：暂无
        - 不要输出额外解释
        - 输出使用中文
        """

        user_prompt = f"""
        以下是项目的最新开发进展记录，请整理成日报简报：

        {markdown_content}
        """
        if dry_run:
            # 如果启用了dry_run模式，将不会调用模型，而是将提示信息保存到文件中
            LOG.info("Dry run mode enabled. Saving prompt to file.")
            with open("daily_progress/prompt.txt", "w+") as f:
                f.write(system_prompt)
                f.write(user_prompt)
            LOG.debug("Prompt saved to daily_progress/prompt.txt")
            return "DRY RUN"

        # 日志记录开始生成报告
        LOG.info("Starting report generation using GPT model.")
        
        try:
            # 调用OpenAI GPT模型生成报告
            response = self.client.chat.completions.create(
                model="deepseek-chat",  # 建议换模型
                messages=[
                    {"role": "system", "content": system_prompt},
                    {"role": "user", "content": user_prompt}
                ],
                temperature=0.3  # 降低发散
            )
            LOG.debug("deepseek response: {}", response)
            # 返回模型生成的内容
            return response.choices[0].message.content
        except Exception as e:
            # 如果在请求过程中出现异常，记录错误并抛出
            LOG.error("An error occurred while generating the report: {}", e)
            raise
