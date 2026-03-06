# src/command_handler.py

import argparse  # 导入argparse库，用于处理命令行参数解析

class CommandHandler:
    def __init__(self, github_client, subscription_manager, report_generator, arxiv_client=None):
        # 初始化CommandHandler，接收GitHub客户端、订阅管理器、报告生成器和arXiv客户端
        self.github_client = github_client
        self.subscription_manager = subscription_manager
        self.report_generator = report_generator
        self.arxiv_client = arxiv_client
        self.parser = self.create_parser()  # 创建命令行解析器

    def create_parser(self):
        # 创建并配置命令行解析器
        parser = argparse.ArgumentParser(
            description='GitHub Sentinel Command Line Interface',
            formatter_class=argparse.RawTextHelpFormatter
        )
        subparsers = parser.add_subparsers(title='Commands', dest='command')

        # 添加订阅命令
        parser_add = subparsers.add_parser('add', help='Add a subscription')
        parser_add.add_argument('repo', type=str, help='The repository to subscribe to (e.g., owner/repo)')
        parser_add.set_defaults(func=self.add_subscription)

        # 删除订阅命令
        parser_remove = subparsers.add_parser('remove', help='Remove a subscription')
        parser_remove.add_argument('repo', type=str, help='The repository to unsubscribe from (e.g., owner/repo)')
        parser_remove.set_defaults(func=self.remove_subscription)

        # 列出所有订阅命令
        parser_list = subparsers.add_parser('list', help='List all subscriptions')
        parser_list.set_defaults(func=self.list_subscriptions)

        # 导出每日进展命令
        parser_export = subparsers.add_parser('export', help='Export daily progress')
        parser_export.add_argument('repo', type=str, help='The repository to export progress from (e.g., owner/repo)')
        parser_export.set_defaults(func=self.export_daily_progress)

        # 导出特定日期范围进展命令
        parser_export_range = subparsers.add_parser('export-range', help='Export progress over a range of dates')
        parser_export_range.add_argument('repo', type=str, help='The repository to export progress from (e.g., owner/repo)')
        parser_export_range.add_argument('days', type=int, help='The number of days to export progress for')
        parser_export_range.set_defaults(func=self.export_progress_by_date_range)

        # 生成日报命令
        parser_generate = subparsers.add_parser('generate', help='Generate daily report from markdown file')
        parser_generate.add_argument('file', type=str, help='The markdown file to generate report from')
        parser_generate.set_defaults(func=self.generate_daily_report)

        # 帮助命令
        parser_help = subparsers.add_parser('help', help='Show help message')
        parser_help.set_defaults(func=self.print_help)

        # ===== arXiv 相关命令 =====
        # arXiv获取论文命令
        parser_arxiv_fetch = subparsers.add_parser('arxiv-fetch', help='Fetch arXiv papers')
        parser_arxiv_fetch.add_argument('-d', '--days', type=int, default=1, help='Number of days (1-7), default is 1')
        parser_arxiv_fetch.add_argument('-c', '--categories', type=str, nargs='+', default=None, help='Paper categories, e.g., cs.AI cs.CL')
        parser_arxiv_fetch.add_argument('-m', '--max-results', type=int, default=30, help='Max results per category, default is 30')
        parser_arxiv_fetch.set_defaults(func=self.arxiv_fetch_papers)

        # arXiv生成报告命令
        parser_arxiv_report = subparsers.add_parser('arxiv-report', help='Generate arXiv report')
        parser_arxiv_report.add_argument('-d', '--days', type=int, default=1, help='Number of days (1-7), default is 1')
        parser_arxiv_report.add_argument('-i', '--input', type=str, default=None, help='Input file path (optional)')
        parser_arxiv_report.set_defaults(func=self.arxiv_generate_report)

        # arXiv显示分类命令
        parser_arxiv_categories = subparsers.add_parser('arxiv-categories', help='Show available arXiv categories')
        parser_arxiv_categories.set_defaults(func=self.arxiv_show_categories)

        return parser  # 返回配置好的解析器

    # 下面是各种命令对应的方法实现，每个方法都使用了相应的管理器来执行实际操作，并输出结果信息
    def add_subscription(self, args):
        self.subscription_manager.add_subscription(args.repo)
        print(f"Added subscription for repository: {args.repo}")

    def remove_subscription(self, args):
        self.subscription_manager.remove_subscription(args.repo)
        print(f"Removed subscription for repository: {args.repo}")

    def list_subscriptions(self, args):
        subscriptions = self.subscription_manager.list_subscriptions()
        print("Current subscriptions:")
        for sub in subscriptions:
            print(f"  - {sub}")

    def export_daily_progress(self, args):
        self.github_client.export_daily_progress(args.repo)
        print(f"Exported daily progress for repository: {args.repo}")

    def export_progress_by_date_range(self, args):
        self.github_client.export_progress_by_date_range(args.repo, days=args.days)
        print(f"Exported progress for the last {args.days} days for repository: {args.repo}")

    def generate_daily_report(self, args):
        self.report_generator.generate_github_report(args.file)
        print(f"Generated daily report from file: {args.file}")

    def print_help(self, args=None):
        self.parser.print_help()  # 输出帮助信息

    # ===== arXiv 相关命令实现 =====
    def arxiv_fetch_papers(self, args):
        """获取arXiv论文"""
        if not self.arxiv_client:
            print("❌ arXiv客户端未初始化")
            return

        try:
            days = min(max(args.days, 1), 7)  # 限制在1-7天
            categories = args.categories
            max_results = args.max_results

            LOG.info(f"正在获取近{days}天的arXiv论文...")
            if categories:
                LOG.info(f"分类: {', '.join(categories)}")

            filepath, papers = self.arxiv_client.export_papers_by_days(
                days=days,
                categories=categories,
                max_results_per_category=max_results
            )

            if filepath and papers:
                print(f"\n✅ 成功获取 {len(papers)} 篇论文")
                print(f"📄 数据已保存到: {filepath}")
            else:
                print("\n❌ 没有获取到符合条件的论文")

        except Exception as e:
            LOG.error(f"获取论文失败: {e}")
            print(f"❌ 获取论文失败: {e}")

    def arxiv_generate_report(self, args):
        """生成arXiv论文报告"""
        if not self.arxiv_client:
            print("❌ arXiv客户端未初始化")
            return

        try:
            if args.input:
                # 使用指定文件
                filepath = args.input
            else:
                # 获取论文数据
                days = min(max(args.days, 1), 7)
                LOG.info(f"正在获取近{days}天的arXiv论文...")
                filepath, papers = self.arxiv_client.export_papers_by_days(days=days)

                if not filepath or not papers:
                    print("\n❌ 没有获取到符合条件的论文")
                    return

            # 生成报告
            LOG.info("正在生成报告...")
            report, report_path = self.report_generator.generate_arxiv_report(filepath)

            print(f"\n✅ 报告生成完成")
            print(f"📄 报告已保存到: {report_path}")
            print(f"\n{report[:500]}...")  # 显示报告前500字符

        except Exception as e:
            LOG.error(f"生成报告失败: {e}")
            print(f"❌ 生成报告失败: {e}")

    def arxiv_show_categories(self, args):
        """显示可用的arXiv论文分类"""
        if not self.arxiv_client:
            print("❌ arXiv客户端未初始化")
            return

        print("\n📚 arXiv 可用分类:\n")
        for code, name in self.arxiv_client.categories.items():
            print(f"  {code:10s} - {name}")
        print("\n💡 使用示例:")
        print("  arxiv-fetch -c cs.AI cs.CL -d 3")
        print("  arxiv-report -d 1")
