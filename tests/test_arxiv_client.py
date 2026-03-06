import unittest
from unittest.mock import patch, MagicMock, mock_open
import sys
import os

# 添加 src 目录到模块搜索路径，以便可以导入 src 目录中的模块
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

from arxiv_client import ArxivClient


class TestArxivClient(unittest.TestCase):
    def setUp(self):
        self.client = ArxivClient()

    def test_client_initialization(self):
        """测试客户端初始化"""
        self.assertIsNotNone(self.client)
        self.assertEqual(self.client.base_url, "http://export.arxiv.org/api/query")
        self.assertIsNotNone(self.client.categories)
        self.assertIn('cs.AI', self.client.categories)
        self.assertIn('cs.CL', self.client.categories)
        self.assertIn('cs.LG', self.client.categories)
        self.assertIn('cs.CV', self.client.categories)

    def test_categories_mapping(self):
        """测试分类映射"""
        expected_categories = {
            'cs.AI': 'Artificial Intelligence',
            'cs.CL': 'Computation and Language',
            'cs.LG': 'Machine Learning',
            'cs.CV': 'Computer Vision'
        }
        self.assertEqual(self.client.categories, expected_categories)

    @patch('arxiv_client.feedparser.parse')
    @patch('arxiv_client.requests.get')
    @patch('os.makedirs')
    @patch('builtins.open', new_callable=mock_open)
    def test_fetch_papers_by_category_success(self, mock_open_func, mock_makedirs, mock_get, mock_parse):
        """测试成功获取论文"""
        # 模拟feedparser解析结果
        mock_feed = MagicMock()
        mock_feed.entries = []
        mock_parse.return_value = mock_feed

        # 模拟HTTP响应
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_get.return_value = mock_response

        # 调用方法
        filepath, papers = self.client.fetch_papers_by_category('cs.AI', days=1, max_results=10)

        # 验证
        self.assertIsInstance(papers, list)

    @patch('arxiv_client.requests.get')
    def test_fetch_papers_by_category_failure(self, mock_get):
        """测试API请求失败"""
        mock_get.side_effect = Exception("Connection error")

        # 调用方法并验证抛出异常
        with self.assertRaises(Exception):
            self.client.fetch_papers_by_category('cs.AI', days=1)

    @patch('arxiv_client.feedparser.parse')
    @patch('arxiv_client.requests.get')
    @patch('os.makedirs')
    @patch('builtins.open', new_callable=mock_open)
    def test_export_papers_by_days(self, mock_open_func, mock_makedirs, mock_get, mock_parse):
        """测试按天数导出论文"""
        from datetime import datetime
        now = datetime.now()

        # 模拟feedparser解析结果 - 添加一个论文entry（使用当前时间）
        mock_author = MagicMock()
        mock_author.name = "Author 1"

        mock_entry = MagicMock()
        mock_entry.title = "Test Paper 1"
        mock_entry.summary = "Abstract 1"
        mock_entry.authors = [mock_author]
        mock_entry.published_parsed = now.timetuple()  # 使用当前时间
        mock_entry.id = "http://arxiv.org/abs/2409.00001"
        mock_entry.link = "http://arxiv.org/abs/2409.00001"

        mock_feed = MagicMock()
        mock_feed.entries = [mock_entry]
        mock_parse.return_value = mock_feed

        # 模拟HTTP响应
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_get.return_value = mock_response

        # 调用方法
        filepath, papers = self.client.export_papers_by_days(days=1)

        # 验证
        self.assertIsNotNone(filepath)
        self.assertIsInstance(papers, list)

    @patch('arxiv_client.feedparser.parse')
    @patch('arxiv_client.requests.get')
    @patch('os.makedirs')
    @patch('builtins.open', new_callable=mock_open)
    def test_export_papers_by_days_with_categories(self, mock_open_func, mock_makedirs, mock_get, mock_parse):
        """测试指定分类导出论文"""
        from datetime import datetime
        now = datetime.now()

        # 模拟feedparser解析结果
        mock_author = MagicMock()
        mock_author.name = "AI Author"

        mock_entry = MagicMock()
        mock_entry.title = "Test Paper AI"
        mock_entry.summary = "AI Abstract"
        mock_entry.authors = [mock_author]
        mock_entry.published_parsed = now.timetuple()  # 使用当前时间
        mock_entry.id = "http://arxiv.org/abs/2409.00001"
        mock_entry.link = "http://arxiv.org/abs/2409.00001"

        mock_feed = MagicMock()
        mock_feed.entries = [mock_entry]
        mock_parse.return_value = mock_feed

        # 模拟HTTP响应
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_get.return_value = mock_response

        # 调用方法，指定分类
        filepath, papers = self.client.export_papers_by_days(
            days=1,
            categories=['cs.AI'],
            max_results_per_category=10
        )

        # 验证
        self.assertIsNotNone(filepath)
        self.assertIsInstance(papers, list)

    @patch('arxiv_client.feedparser.parse')
    @patch('arxiv_client.requests.get')
    @patch('os.makedirs')
    @patch('builtins.open', new_callable=mock_open)
    def test_export_papers_by_hours_compatibility(self, mock_open_func, mock_makedirs, mock_get, mock_parse):
        """测试export_papers_by_hours方法兼容性"""
        from datetime import datetime
        now = datetime.now()

        # 模拟feedparser解析结果
        mock_author = MagicMock()
        mock_author.name = "Test Author"

        mock_entry = MagicMock()
        mock_entry.title = "Test Paper"
        mock_entry.summary = "Test Abstract"
        mock_entry.authors = [mock_author]
        mock_entry.published_parsed = now.timetuple()  # 使用当前时间
        mock_entry.id = "http://arxiv.org/abs/2409.00001"
        mock_entry.link = "http://arxiv.org/abs/2409.00001"

        mock_feed = MagicMock()
        mock_feed.entries = [mock_entry]
        mock_parse.return_value = mock_feed

        # 模拟HTTP响应
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_get.return_value = mock_response

        # 调用方法（使用hours参数）
        filepath, papers = self.client.export_papers_by_hours(hours=24)

        # 验证
        self.assertIsNotNone(filepath)
        self.assertIsInstance(papers, list)


if __name__ == '__main__':
    unittest.main()
