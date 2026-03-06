# src/daemon_process.py
import schedule
import time
import signal
import sys

from config import Config
from github_client import GitHubClient
from hackernews_client import HackerNewsClient
from notifier import Notifier
from report_generator import ReportGenerator
from hackernews_report_generator import HackerNewsReportGenerator
from llm import LLM
from subscription_manager import SubscriptionManager
from logger import LOG


def graceful_shutdown(signum, frame):
    LOG.info("[优雅退出]守护进程接收到终止信号")
    sys.exit(0)


def github_job(subscription_manager, github_client, report_generator, notifier, days):
    LOG.info("[开始执行GitHub定时任务]")
    subscriptions = subscription_manager.list_github_subscriptions()
    LOG.info(f"GitHub订阅列表：{subscriptions}")
    for repo in subscriptions:
        markdown_file_path = github_client.export_progress_by_date_range(repo, days)
        report, report_file_path = report_generator.generate_report_by_date_range(markdown_file_path, days)
        notifier.notify(f"GitHub - {repo}", report)
    LOG.info(f"[GitHub定时任务执行完毕]")


def hackernews_job(hackernews_client, report_generator, notifier, config):
    """执行HackerNews定时任务 - 直接从config获取配置"""
    LOG.info("[开始执行HackerNews定时任务]")

    try:
        # 直接从config获取过滤参数
        hours = config.hackernews_hours
        min_score = config.hackernews_min_score
        keywords = config.hackernews_keywords
        max_stories = config.hackernews_max_stories

        LOG.info(
            f"正在获取过去{hours}小时的HackerNews数据，最低热度：{min_score}，关键词：{keywords}，最大文章数：{max_stories}")

        # 获取并导出数据
        raw_file_path, stories = hackernews_client.export_stories_by_hours(
            hours=hours,
            min_score=min_score,
            keywords=keywords,
            limit=max_stories
        )

        if stories and len(stories) > 0:
            report, report_file_path = report_generator.generate_trend_report(raw_file_path, hours)

            filter_info = f"过滤条件：过去{hours}小时，最低热度 {min_score}，关键词 {keywords if keywords else '无'}\n"
            filter_info += f"获取到文章数：{len(stories)}篇\n\n"
            full_report = filter_info + report

            notifier.notify(f"HackerNews趋势报告 (过去{hours}小时)", full_report)
            LOG.info(f"HackerNews任务完成，获取到{len(stories)}篇文章")
        else:
            LOG.info("HackerNews没有符合条件的文章")
            notifier.notify(
                "HackerNews趋势报告",
                f"过去{hours}小时内没有符合条件的HackerNews文章。\n过滤条件：最低热度 {min_score}，关键词 {keywords if keywords else '无'}"
            )

    except Exception as e:
        LOG.error(f"执行HackerNews任务失败: {str(e)}")

    LOG.info("[HackerNews定时任务执行完毕]")


def combined_job(subscription_manager, github_client, hackernews_client,
                 github_report_gen, hackernews_report_gen, notifier, config):
    """组合任务：同时执行GitHub和HackerNews任务"""
    LOG.info("[开始执行组合定时任务]")

    if config.github_enabled and subscription_manager.list_github_subscriptions():
        github_job(subscription_manager, github_client, github_report_gen, notifier, config.github_freq_days)
    else:
        LOG.info("GitHub监控已禁用或无订阅，跳过GitHub任务")

    if config.hackernews_enabled:
        hackernews_job(hackernews_client, hackernews_report_gen, notifier, config)
    else:
        LOG.info("HackerNews监控已禁用，跳过HackerNews任务")

    LOG.info("[组合定时任务执行完毕]")


def main():
    signal.signal(signal.SIGTERM, graceful_shutdown)
    signal.signal(signal.SIGINT, graceful_shutdown)

    config = Config()
    github_client = GitHubClient(config.github_token)
    hackernews_client = HackerNewsClient()
    notifier = Notifier(config.email)
    llm = LLM(config)

    github_report_generator = ReportGenerator(llm)
    hackernews_report_generator = HackerNewsReportGenerator(llm)
    subscription_manager = SubscriptionManager(config.subscriptions_file)

    LOG.info("启动时立即执行一次任务")
    combined_job(
        subscription_manager,
        github_client,
        hackernews_client,
        github_report_generator,
        hackernews_report_generator,
        notifier,
        config
    )

    if config.github_enabled:
        schedule.every(config.github_freq_days).days.at(
            config.github_exec_time
        ).do(github_job, subscription_manager, github_client, github_report_generator, notifier,
             config.github_freq_days)
        LOG.info(f"已安排GitHub任务: 每{config.github_freq_days}天 {config.github_exec_time}执行")

    if config.hackernews_enabled:
        if config.hackernews_freq_hours < 24:
            schedule.every(config.hackernews_freq_hours).hours.do(
                hackernews_job,
                hackernews_client,
                hackernews_report_generator,
                notifier,
                config
            )
            LOG.info(f"已安排HackerNews任务: 每{config.hackernews_freq_hours}小时执行一次")
        else:
            schedule.every(config.hackernews_freq_days).days.at(
                config.hackernews_exec_time
            ).do(
                hackernews_job,
                hackernews_client,
                hackernews_report_generator,
                notifier,
                config
            )
            LOG.info(f"已安排HackerNews任务: 每{config.hackernews_freq_days}天 {config.hackernews_exec_time}执行")

    try:
        while True:
            schedule.run_pending()
            time.sleep(1)
    except Exception as e:
        LOG.error(f"主进程发生异常: {str(e)}")
        sys.exit(1)


if __name__ == '__main__':
    main()