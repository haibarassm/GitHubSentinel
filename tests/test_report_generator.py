import sys
import os
import unittest
from unittest.mock import MagicMock, patch

# 添加 src 目录到模块搜索路径，以便可以导入 src 目录中的模块
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

from report_generator import ReportGenerator  # 导入要测试的 ReportGenerator 类

class TestReportGenerator(unittest.TestCase):
    def setUp(self):
        """
        在每个测试方法之前运行，初始化测试环境。
        """
        # 创建一个模拟的 LLM（大语言模型）对象
        self.mock_llm = MagicMock()
        self.mock_llm.model = "mock_model"  # 确保mock对象有一个有效的模型名称

        # 模拟提示内容
        self.mock_prompts = {
            "github": "GitHub specific prompt...",
            "hacker_news_hours_topic": "Hacker News topic specific prompt...",
            "hacker_news_daily_report": "Hacker News daily summary prompt...",
            "arxiv": "arXiv papers specific prompt..."
        }

        # 设置测试用的 Markdown 文件路径
        self.test_markdown_file_path = 'test_daily_progress.md'
        self.test_hn_topic_file_path = 'test_hn_topic.md'
        self.test_hn_daily_dir_path = 'test_hn_daily_dir'
        self.test_arxiv_file_path = 'test_arxiv_papers.md'

        # 模拟 Markdown 文件的内容，代表一个项目的每日进展
        self.markdown_content = """
        # Daily Progress for DjangoPeng/openai-quickstart (2024-08-24)

        ## Issues Closed Today
        - Fix bug #123
        """

        # 创建测试用的 Markdown 文件并写入内容
        with open(self.test_markdown_file_path, 'w') as file:
            file.write(self.markdown_content)

        with open(self.test_hn_topic_file_path, 'w') as file:
            file.write(self.markdown_content)

        # 创建测试用的 Hacker News 目录及文件
        os.makedirs(self.test_hn_daily_dir_path, exist_ok=True)
        self.hn_topic_report_path = os.path.join(self.test_hn_daily_dir_path, "test_topic_01_topic.md")
        with open(self.hn_topic_report_path, 'w') as file:
            file.write(self.markdown_content)

        # 创建测试用的 arXiv 文件
        self.arxiv_content = """
        # arXiv Papers Summary
        Date: 2024-09-01
        Total Papers: 2

        ## cs.AI - Artificial Intelligence (2 papers)

        ### Test Paper 1: Attention Is All You Need
        - **Authors**: Vaswani et al.
        - **Published**: 2024-09-01
        - **arXiv**: [1706.03762](http://arxiv.org/abs/1706.03762)

        ### Test Paper 2: BERT: Pre-training of Deep Bidirectional Transformers
        - **Authors**: Devlin et al.
        - **Published**: 2024-09-01
        - **arXiv**: [1810.04805](http://arxiv.org/abs/1810.04805)
        """
        with open(self.test_arxiv_file_path, 'w') as file:
            file.write(self.arxiv_content)

    def tearDown(self):
        """
        在每个测试方法之后运行，清理测试环境。
        """
        # 删除测试用的 Markdown 文件
        if os.path.exists(self.test_markdown_file_path):
            os.remove(self.test_markdown_file_path)
        if os.path.exists(self.test_hn_topic_file_path):
            os.remove(self.test_hn_topic_file_path)

        # 删除生成的报告文件
        report_file_path = os.path.splitext(self.test_markdown_file_path)[0] + "_report.md"
        if os.path.exists(report_file_path):
            os.remove(report_file_path)

        hn_topic_report_path = os.path.splitext(self.test_hn_topic_file_path)[0] + "_topic.md"
        if os.path.exists(hn_topic_report_path):
            os.remove(hn_topic_report_path)

        hn_daily_report_path = os.path.join("hacker_news/tech_trends/", f"{os.path.basename(self.test_hn_daily_dir_path)}_trends.md")
        if os.path.exists(hn_daily_report_path):
            os.remove(hn_daily_report_path)
        
        # 删除 Hacker News 测试目录
        if os.path.exists(self.test_hn_daily_dir_path):
            for file in os.listdir(self.test_hn_daily_dir_path):
                os.remove(os.path.join(self.test_hn_daily_dir_path, file))
            os.rmdir(self.test_hn_daily_dir_path)

        # 删除 arXiv 测试文件
        if os.path.exists(self.test_arxiv_file_path):
            os.remove(self.test_arxiv_file_path)

        # 删除生成的 arXiv 报告文件
        arxiv_report_path = os.path.join("reports", "arxiv_report_2024-09-01.md")
        if os.path.exists(arxiv_report_path):
            os.remove(arxiv_report_path)
        # 清理 reports 目录
        if os.path.exists("reports") and not os.listdir("reports"):
            os.rmdir("reports")

    @patch.object(ReportGenerator, '_preload_prompts', return_value=None)
    def test_generate_github_report(self, mock_preload_prompts):
        """
        测试 generate_github_report 方法是否正确生成报告并保存到文件。
        """
        # 初始化 ReportGenerator 实例，并手动设置 prompts
        self.report_generator = ReportGenerator(self.mock_llm, ["github", "hacker_news_hours_topic", "hacker_news_daily_report"])
        self.report_generator.prompts = self.mock_prompts

        # 模拟 LLM 返回的报告内容
        mock_report = "This is a generated report."
        self.mock_llm.generate_report.return_value = mock_report

        # 调用 generate_github_report 方法
        report, report_file_path = self.report_generator.generate_github_report(self.test_markdown_file_path)

        # 验证返回值是否正确
        self.assertEqual(report, mock_report)
        self.assertTrue(report_file_path.endswith("_report.md"))

        # 验证生成的报告文件内容是否正确
        with open(report_file_path, 'r') as file:
            content = file.read()
            self.assertEqual(content, mock_report)

        # 验证 LLM 的 generate_report 方法是否被正确调用，且传入了正确的参数
        self.mock_llm.generate_report.assert_called_once_with(self.mock_prompts["github"], self.markdown_content)

    @patch.object(ReportGenerator, '_preload_prompts', return_value=None)
    def test_generate_hn_topic_report(self, mock_preload_prompts):
        """
        测试 generate_hn_topic_report 方法是否正确生成报告并保存到文件。
        """
        # 初始化 ReportGenerator 实例，并手动设置 prompts
        self.report_generator = ReportGenerator(self.mock_llm, ["github", "hacker_news_hours_topic", "hacker_news_daily_report"])
        self.report_generator.prompts = self.mock_prompts

        # 模拟 LLM 返回的报告内容
        mock_report = "This is a generated Hacker News topic report."
        self.mock_llm.generate_report.return_value = mock_report

        # 调用 generate_hn_topic_report 方法
        report, report_file_path = self.report_generator.generate_hn_topic_report(self.test_hn_topic_file_path)

        # 验证返回值是否正确
        self.assertEqual(report, mock_report)
        self.assertTrue(report_file_path.endswith("_topic.md"))

        # 验证生成的报告文件内容是否正确
        with open(report_file_path, 'r') as file:
            content = file.read()
            self.assertEqual(content, mock_report)

        # 验证 LLM 的 generate_report 方法是否被正确调用，且传入了正确的参数
        self.mock_llm.generate_report.assert_called_once_with(self.mock_prompts["hacker_news_hours_topic"], self.markdown_content)

    @patch.object(ReportGenerator, '_preload_prompts', return_value=None)
    def test_generate_hn_daily_report(self, mock_preload_prompts):
        """
        测试 generate_hn_daily_report 方法是否正确生成每日汇总报告并保存到文件。
        """
        # 初始化 ReportGenerator 实例，并手动设置 prompts
        self.report_generator = ReportGenerator(self.mock_llm, ["github", "hacker_news_hours_topic", "hacker_news_daily_report"])
        self.report_generator.prompts = self.mock_prompts

        # 模拟 LLM 返回的报告内容
        mock_report = "This is a generated Hacker News daily trends report."
        self.mock_llm.generate_report.return_value = mock_report

        # 调用 generate_hn_daily_report 方法
        report, report_file_path = self.report_generator.generate_hn_daily_report(self.test_hn_daily_dir_path)

        # 验证返回值是否正确
        self.assertEqual(report, mock_report)
        self.assertTrue(report_file_path.endswith("_trends.md"))

        # 验证生成的报告文件内容是否正确
        with open(report_file_path, 'r') as file:
            content = file.read()
            self.assertEqual(content, mock_report)

        # 验证 LLM 的 generate_report 方法是否被正确调用，且传入了正确的参数
        aggregated_content = self.report_generator._aggregate_topic_reports(self.test_hn_daily_dir_path)
        self.mock_llm.generate_report.assert_called_once_with(self.mock_prompts["hacker_news_daily_report"], aggregated_content)

    @patch.object(ReportGenerator, '_preload_prompts', return_value=None)
    @patch('os.makedirs')
    def test_generate_arxiv_report(self, mock_makedirs, mock_preload_prompts):
        """
        测试 generate_arxiv_report 方法是否正确生成arXiv论文报告并保存到文件。
        """
        # 初始化 ReportGenerator 实例，并手动设置 prompts
        self.report_generator = ReportGenerator(
            self.mock_llm,
            ["github", "hacker_news_hours_topic", "hacker_news_daily_report", "arxiv"]
        )
        self.report_generator.prompts = self.mock_prompts

        # 模拟 LLM 返回的报告内容
        mock_report = "# arXiv Papers Technical Trend Report\n\nThis is a generated arXiv papers trend report."
        self.mock_llm.generate_report.return_value = mock_report

        # 调用 generate_arxiv_report 方法
        report, report_file_path = self.report_generator.generate_arxiv_report(self.test_arxiv_file_path)

        # 验证返回值是否正确
        self.assertEqual(report, mock_report)
        self.assertIsNotNone(report_file_path)
        self.assertTrue(report_file_path.endswith(".md"))
        self.assertIn("arxiv_report_", report_file_path)

        # 验证 reports 目录被创建
        mock_makedirs.assert_called_once_with("reports", exist_ok=True)

        # 验证 LLM 的 generate_report 方法是否被正确调用
        self.mock_llm.generate_report.assert_called_once_with(
            self.mock_prompts["arxiv"],
            self.arxiv_content
        )

if __name__ == '__main__':
    unittest.main()
