# github_sentinel_cli.py
import shlex
import sys

from config import Config
from github_client import GitHubClient
from hackernews_client import HackerNewsClient
from report_generator import ReportGenerator
from hackernews_report_generator import HackerNewsReportGenerator
from llm import LLM
from subscription_manager import SubscriptionManager
from command_handler import CommandHandler
from hackernews_command_handler import HackerNewsCommandHandler
from logger import LOG


def print_banner():
    """打印欢迎横幅"""
    banner = """
╔══════════════════════════════════════════════════════════╗
║                 GitHubSentinel CLI v2.0                  ║
║              GitHub监控 & HackerNews趋势分析              ║
╚══════════════════════════════════════════════════════════╝
    """
    print(banner)


def main():
    print_banner()

    # 加载配置
    config = Config()

    # 创建各组件实例
    github_client = GitHubClient(config.github_token)
    hackernews_client = HackerNewsClient()
    llm = LLM(config)

    github_report_generator = ReportGenerator(llm)
    hackernews_report_generator = HackerNewsReportGenerator(llm)

    subscription_manager = SubscriptionManager(config.subscriptions_file)

    # 创建命令处理器
    github_command_handler = CommandHandler(github_client, subscription_manager, github_report_generator)
    hackernews_command_handler = HackerNewsCommandHandler(hackernews_client, hackernews_report_generator, config)

    # 设置主解析器
    parser = github_command_handler.parser
    subparsers = parser._subparsers._actions[-1]

    # 添加HackerNews命令
    hackernews_command_handler.setup_parser(subparsers)

    # 添加新的帮助信息
    parser.description = """
GitHub Sentinel 命令行工具

可用命令分类:
  📚 GitHub命令: help, list, add, remove, report, daily
  🔥 HackerNews命令: hn fetch, hn report, hn config, hn stats
  💡 其他命令: help, exit, quit

使用 'help' 查看详细帮助，'help <命令>' 查看特定命令的帮助
    """

    # 打印帮助信息
    github_command_handler.print_help()
    print("\n🔥 HackerNews 命令:")
    print("  hn fetch -H 24 -s 50 -k AI,Python    获取最近24小时热度>50且包含AI/Python的文章")
    print("  hn report -H 24 -o report.md         生成最近24小时的趋势报告")
    print("  hn config --show                      显示HackerNews配置")
    print("  hn stats -H 48                         显示最近48小时的统计信息")
    print()

    while True:
        try:
            user_input = input("GitHub Sentinel> ").strip()

            if not user_input:
                continue

            if user_input in ['exit', 'quit']:
                print("👋 再见!")
                break

            if user_input == 'help':
                parser.print_help()
                continue

            try:
                args = parser.parse_args(shlex.split(user_input))

                if hasattr(args, 'command') and args.command is None:
                    continue

                if hasattr(args, 'func'):
                    args.func(args)
                else:
                    print("❌ 未知命令。使用 'help' 查看可用命令。")

            except SystemExit:
                # argparse在错误时会抛出SystemExit，我们捕获它但不退出程序
                pass
            except Exception as e:
                LOG.error(f"命令执行错误: {e}")
                print(f"❌ 命令执行失败: {e}")

        except KeyboardInterrupt:
            print("\n👋 再见!")
            break
        except Exception as e:
            LOG.error(f"意外错误: {e}")
            print(f"❌ 意外错误: {e}")


if __name__ == '__main__':
    main()