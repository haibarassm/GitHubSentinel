# src/arxiv_client.py
import requests
import feedparser
from datetime import datetime, timedelta
from logger import LOG


class ArxivClient:
    """arXiv API客户端，用于获取最新的学术论文信息"""

    def __init__(self):
        self.base_url = "http://export.arxiv.org/api/query"
        # 推荐的arXiv分类
        self.categories = {
            'cs.AI': 'Artificial Intelligence',
            'cs.CL': 'Computation and Language',
            'cs.LG': 'Machine Learning',
            'cs.CV': 'Computer Vision'
        }

    def fetch_papers_by_category(self, category, days=1, max_results=50):
        """
        根据分类获取论文

        :param category: arXiv分类，如 'cs.AI'
        :param days: 获取最近几天的论文
        :param max_results: 最大结果数
        :return: (文件路径, 论文列表)
        """
        try:
            # 计算日期范围
            end_date = datetime.now()
            start_date = end_date - timedelta(days=days)

            # 构建查询
            search_query = f"cat:{category}"
            query_url = (
                f"{self.base_url}?"
                f"search_query={search_query}&"
                f"sortBy=submittedDate&"
                f"sortOrder=descending&"
                f"max_results={max_results}"
            )

            LOG.info(f"正在获取 {category} 分类最近{days}天的论文...")
            response = requests.get(query_url, timeout=30)
            response.raise_for_status()

            # 解析Atom feed
            feed = feedparser.parse(response.content)

            papers = []
            for entry in feed.entries:
                # 解析发布日期
                published_date = datetime(*entry.published_parsed[:6])

                # 只保留指定日期范围内的论文
                if published_date >= start_date:
                    # 提取作者信息
                    authors = [author.name for author in entry.authors]

                    # 提取PDF链接
                    pdf_url = entry.link.replace('/abs/', '/pdf/') + '.pdf'

                    # 提取arXiv ID
                    arxiv_id = entry.id.split('/abs/')[-1]

                    paper = {
                        'title': entry.title,
                        'summary': entry.summary,
                        'authors': authors,
                        'published': published_date.strftime('%Y-%m-%d'),
                        'pdf_url': pdf_url,
                        'arxiv_id': arxiv_id,
                        'category': category
                    }
                    papers.append(paper)

            LOG.info(f"获取到 {len(papers)} 篇论文")

            # 导出到文件
            if papers:
                date_str = datetime.now().strftime('%Y-%m-%d')
                filename = f"arxiv_{category.replace('.', '_')}_{date_str}.md"
                filepath = f"arxiv/{filename}"

                import os
                os.makedirs('arxiv', exist_ok=True)

                with open(filepath, 'w', encoding='utf-8') as f:
                    f.write(f"# arXiv Papers - {category}\n")
                    f.write(f"Date: {date_str}\n")
                    f.write(f"Total Papers: {len(papers)}\n\n")

                    for i, paper in enumerate(papers, 1):
                        f.write(f"## {i}. {paper['title']}\n\n")
                        f.write(f"**Authors**: {', '.join(paper['authors'][:5])}")
                        if len(paper['authors']) > 5:
                            f.write(f" et al. ({len(paper['authors'])} authors)")
                        f.write(f"\n\n**Published**: {paper['published']}\n\n")
                        f.write(f"**arXiv ID**: {paper['arxiv_id']}\n\n")
                        f.write(f"**PDF**: {paper['pdf_url']}\n\n")
                        f.write(f"**Abstract**:\n{paper['summary']}\n\n")
                        f.write("---\n\n")

                LOG.info(f"论文已导出到: {filepath}")
                return filepath, papers

            return None, []

        except Exception as e:
            LOG.error(f"获取arXiv论文失败: {str(e)}")
            raise

    def export_papers_by_days(self, days=1, categories=None, max_results_per_category=30):
        """
        获取指定天数范围内的论文

        :param days: 近N天（1-7天）
        :param categories: 分类列表，如 ['cs.AI', 'cs.CL']
        :param max_results_per_category: 每个分类的最大结果数
        :return: (文件路径, 所有论文列表)
        """
        if categories is None:
            categories = list(self.categories.keys())

        all_papers = []
        filepaths = []

        for category in categories:
            try:
                filepath, papers = self.fetch_papers_by_category(
                    category, days, max_results_per_category
                )
                if filepath:
                    filepaths.append(filepath)
                all_papers.extend(papers)
            except Exception as e:
                LOG.error(f"获取 {category} 分类失败: {e}")
                continue

        # 创建汇总文件（按日期命名）
        if all_papers:
            date_str = datetime.now().strftime('%Y-%m-%d')
            filename = f"arxiv_summary_{date_str}.md"
            filepath = f"arxiv/{filename}"

            import os
            os.makedirs('arxiv', exist_ok=True)

            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(f"# arXiv Papers Summary\n")
                f.write(f"Date: {date_str}\n")
                f.write(f"Days: {days}\n")
                f.write(f"Total Papers: {len(all_papers)}\n")
                f.write(f"Categories: {', '.join(categories)}\n\n")

                # 按分类分组
                papers_by_category = {}
                for paper in all_papers:
                    cat = paper['category']
                    if cat not in papers_by_category:
                        papers_by_category[cat] = []
                    papers_by_category[cat].append(paper)

                for category, papers in papers_by_category.items():
                    f.write(f"\n## {category} - {self.categories.get(category, category)} ({len(papers)} papers)\n\n")
                    for paper in papers[:10]:  # 每个分类只显示前10篇
                        f.write(f"### {paper['title']}\n")
                        f.write(f"- **Authors**: {', '.join(paper['authors'][:3])} et al.\n")
                        f.write(f"- **Published**: {paper['published']}\n")
                        f.write(f"- **arXiv**: [{paper['arxiv_id']}]({paper['pdf_url']})\n\n")

            LOG.info(f"汇总文件已创建: {filepath}")
            return filepath, all_papers

        return None, all_papers

    def export_papers_by_hours(self, hours=24, categories=None, max_results=100):
        """
        获取指定时间范围内的论文（兼容HackerNews客户端接口）

        :param hours: 时间范围（小时）
        :param categories: 分类列表
        :param max_results: 最大结果数
        :return: (文件路径, 论文列表)
        """
        days = max(1, hours // 24)
        if hours % 24 > 0:
            days += 1

        return self.export_papers_by_days(
            days=days,
            categories=categories,
            max_results_per_category=max_results // len(categories) if categories else 25
        )


if __name__ == '__main__':
    # 测试代码
    client = ArxivClient()
    filepath, papers = client.fetch_papers_by_category('cs.AI', days=1, max_results=10)
    print(f"获取到 {len(papers)} 篇论文")
    print(f"文件路径: {filepath}")
