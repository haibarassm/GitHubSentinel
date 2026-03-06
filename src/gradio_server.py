# src/gradio_server.py
import gradio as gr  # 导入gradio库用于创建GUI

from config import Config  # 导入配置管理模块
from github_client import GitHubClient  # 导入用于GitHub API操作的客户端
from hackernews_client import HackerNewsClient  # 导入HackerNews客户端
from report_generator import ReportGenerator  # 导入报告生成器模块
from hackernews_report_generator import HackerNewsReportGenerator  # 导入HackerNews报告生成器
from llm import LLM  # 导入可能用于处理语言模型的LLM类
from subscription_manager import SubscriptionManager  # 导入订阅管理器
from logger import LOG  # 导入日志记录器

# 创建各个组件的实例
config = Config()
github_client = GitHubClient(config.github_token)
hackernews_client = HackerNewsClient()
llm = LLM(config)

# 创建不同的报告生成器
github_report_generator = ReportGenerator(llm)
hackernews_report_generator = HackerNewsReportGenerator(llm)

subscription_manager = SubscriptionManager(config.subscriptions_file)


def github_export_progress_by_date_range(repo, days):
    # 定义一个函数，用于导出和生成指定时间范围内项目的进展报告
    raw_file_path = github_client.export_progress_by_date_range(repo, days)  # 导出原始数据文件路径
    report, report_file_path = github_report_generator.generate_report_by_date_range(raw_file_path,
                                                                                     days)  # 生成并获取报告内容及文件路径
    return report, report_file_path  # 返回报告内容和报告文件路径


# src/gradio_server.py 中的 hackernews_export_trends 函数
def hackernews_export_trends(hours, min_score, keywords_input, max_stories):
    """HackerNews趋势报告生成函数"""
    LOG.info(f"生成HackerNews报告: 过去{hours}小时, 最低热度={min_score}, 最大文章数={max_stories}")

    # 处理关键词输入（逗号分隔）- 注意中文逗号问题
    if keywords_input:
        # 替换中文逗号为英文逗号，然后分割
        keywords_input = keywords_input.replace('，', ',')
        keywords = [k.strip() for k in keywords_input.split(',') if k.strip()]
    else:
        keywords = []

    LOG.info(f"处理后的关键词: {keywords}")

    # 获取并导出数据
    try:
        raw_file_path, stories = hackernews_client.export_stories_by_hours(
            hours=hours,
            min_score=min_score,
            keywords=keywords,
            limit=max_stories
        )

        if not raw_file_path or not stories:
            # 提供更友好的提示
            suggestion = ""
            if hours < 12:
                suggestion += "• 增加时间范围（例如24小时）\n"
            if min_score > 100:
                suggestion += "• 降低最低热度要求\n"
            if keywords:
                suggestion += "• 放宽关键词过滤条件\n"

            error_msg = f"❌ 过去{hours}小时内没有符合条件的文章。\n\n"
            if suggestion:
                error_msg += f"建议：\n{suggestion}"
            else:
                error_msg += "可能是当前时段HackerNews更新较少，请稍后再试。"

            return error_msg, None

        # 生成报告
        report, report_file_path = hackernews_report_generator.generate_trend_report(raw_file_path, hours)

        # 添加过滤信息到报告开头
        filter_info = f"**过滤条件**：过去{hours}小时，最低热度 {min_score}，关键词 {keywords if keywords else '无'}\n"
        filter_info += f"**获取到文章数**：{len(stories)}篇\n\n"

        return filter_info + report, report_file_path

    except Exception as e:
        LOG.error(f"生成HackerNews报告失败: {e}")
        return f"❌ 生成报告时出错: {str(e)}", None

# 创建带有Tab的Gradio界面 - 使用gr.Blocks替代gr.Interface
with gr.Blocks(title="GitHubSentinel") as demo:
    gr.Markdown("# GitHubSentinel")

    # 创建Tab组件
    with gr.Tabs():
        # GitHub Tab
        with gr.TabItem("GitHub 项目监控"):
            gr.Markdown("## GitHub项目进展报告")

            with gr.Row():
                with gr.Column(scale=1):
                    repo_dropdown = gr.Dropdown(
                        subscription_manager.list_github_subscriptions(),
                        label="订阅列表",
                        info="已订阅GitHub项目"
                    )

                    days_slider = gr.Slider(
                        value=2,
                        minimum=1,
                        maximum=7,
                        step=1,
                        label="报告周期",
                        info="生成项目过去一段时间进展，单位：天"
                    )

                    submit_btn = gr.Button("生成报告", variant="primary")

                with gr.Column(scale=2):
                    github_output = gr.Markdown(label="报告内容")
                    github_file = gr.File(label="下载报告")

            submit_btn.click(
                fn=github_export_progress_by_date_range,
                inputs=[repo_dropdown, days_slider],
                outputs=[github_output, github_file]
            )

        # HackerNews Tab
        with gr.TabItem("Hacker News 趋势"):
            gr.Markdown("## HackerNews技术趋势报告")

            with gr.Row():
                with gr.Column(scale=1):
                    hn_hours = gr.Slider(
                        value=6,
                        minimum=1,
                        maximum=72,
                        step=1,
                        label="时间范围",
                        info="获取过去多少小时内的文章，单位：小时"
                    )

                    hn_min_score = gr.Slider(
                        value=getattr(config, 'hackernews_min_score', 200),
                        minimum=0,
                        maximum=500,
                        step=10,
                        label="最低热度",
                        info="过滤低于此热度分的文章"
                    )

                    hn_keywords = gr.Textbox(
                        value=", ".join(getattr(config, 'hackernews_keywords', [])) if hasattr(config,
                                                                                               'hackernews_keywords') and config.hackernews_keywords else "",
                        label="关键词过滤",
                        placeholder="输入关键词，用逗号分隔，例如：AI, Python, 机器学习",
                        info="只在标题中包含这些关键词的文章"
                    )

                    hn_limit = gr.Slider(
                        value=getattr(config, 'hackernews_max_stories', 30),
                        minimum=10,
                        maximum=200,
                        step=10,
                        label="最大文章数",
                        info="最多返回多少篇文章"
                    )

                    hn_btn = gr.Button("生成报告", variant="primary")

                with gr.Column(scale=2):
                    hn_output = gr.Markdown(label="报告内容")
                    hn_file = gr.File(label="下载报告")

            hn_btn.click(
                fn=hackernews_export_trends,
                inputs=[hn_hours, hn_min_score, hn_keywords, hn_limit],
                outputs=[hn_output, hn_file]
            )

if __name__ == "__main__":
    demo.launch(share=True, server_name="0.0.0.0")
    # 可选带有用户认证的启动方式
    # demo.launch(share=True, server_name="0.0.0.0", auth=("django", "1234"))