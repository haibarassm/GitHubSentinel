# src/hackernews_report_generator.py
import os
import json
from datetime import datetime
from logger import LOG


class HackerNewsReportGenerator:
    """HackerNews报告生成器"""

    def __init__(self, llm):
        self.llm = llm

    def generate_trend_report(self, json_file_path, hours):
        """
        生成HackerNews趋势报告

        Args:
            json_file_path: HackerNews数据的JSON文件路径
            hours: 时间范围（小时）

        Returns:
            tuple: (报告内容, 报告文件路径)
        """
        try:
            # 读取JSON数据
            with open(json_file_path, 'r', encoding='utf-8') as f:
                stories = json.load(f)

            if not stories:
                return "过去{}小时内没有新的HackerNews文章。".format(hours), None

            # 生成基础报告（中文）
            report_content = self._format_stories_report(stories, hours)

            # 使用LLM生成深度分析 - 明确传递 report_type='hackernews'
            if self.llm:
                analysis = self._generate_llm_analysis(stories, hours)
                if analysis and analysis != "DRY RUN":
                    report_content += "\n\n## 🤖 AI 趋势分析\n\n" + analysis

            # 保存报告
            report_file_path = self._save_report(report_content, hours)

            LOG.info(f"HackerNews趋势报告已保存到 {report_file_path}")
            return report_content, report_file_path

        except Exception as e:
            LOG.error(f"生成HackerNews报告失败: {e}")
            return f"生成报告时出错: {str(e)}", None

    def _format_stories_report(self, stories, hours):
        """格式化文章列表为报告（全部用中文）"""
        # 按热度排序
        stories.sort(key=lambda x: x.get('score', 0), reverse=True)

        report = f"# HackerNews 技术趋势报告 (过去{hours}小时)\n\n"
        report += f"生成时间: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n"
        report += f"文章数量: {len(stories)}篇\n\n"

        # 热门文章排行
        report += "## 🔥 热门文章排行\n\n"

        for i, story in enumerate(stories[:20], 1):
            title = story.get('title', '无标题')
            url = story.get('url', f"https://news.ycombinator.com/item?id={story.get('id')}")
            score = story.get('score', 0)
            by = story.get('by', 'unknown')
            comments = story.get('descendants', 0)

            # 转换时间戳
            time_str = datetime.fromtimestamp(story.get('time', 0)).strftime('%Y-%m-%d %H:%M')

            report += f"### {i}. [{title}]({url})\n\n"
            report += f"- **热度**: {score} 分\n"
            report += f"- **评论**: {comments} 条\n"
            report += f"- **作者**: {by}\n"
            report += f"- **发布时间**: {time_str}\n\n"

        # 统计信息
        report += self._generate_statistics(stories)

        # 热门来源网站
        report += self._categorize_by_domain(stories)

        return report

    def _generate_statistics(self, stories):
        """生成统计信息（中文）"""
        if not stories:
            return ""

        total_score = sum(s.get('score', 0) for s in stories)
        avg_score = total_score / len(stories)
        total_comments = sum(s.get('descendants', 0) for s in stories)

        # 找出最活跃的作者
        author_stats = {}
        for story in stories:
            author = story.get('by', 'unknown')
            score = story.get('score', 0)
            if author in author_stats:
                author_stats[author]['count'] += 1
                author_stats[author]['total_score'] += score
            else:
                author_stats[author] = {'count': 1, 'total_score': score}

        top_authors = sorted(
            author_stats.items(),
            key=lambda x: x[1]['total_score'],
            reverse=True
        )[:5]

        stats = "## 📊 统计概览\n\n"
        stats += f"- **总热度分**: {total_score}\n"
        stats += f"- **平均热度分**: {avg_score:.1f}\n"
        stats += f"- **总评论数**: {total_comments}\n"
        stats += f"- **平均评论数**: {total_comments / len(stories):.1f}\n\n"

        if top_authors:
            stats += "### 👥 热门作者\n\n"
            for author, data in top_authors:
                stats += f"- **{author}**: {data['total_score']} 分 ({data['count']} 篇文章)\n"
            stats += "\n"

        return stats

    def _categorize_by_domain(self, stories):
        """按域名分类文章（中文）"""
        domains = {}
        for story in stories:
            url = story.get('url', '')
            if url:
                # 提取域名
                try:
                    domain = url.split('/')[2] if '://' in url else url.split('/')[0]
                    domain = domain.replace('www.', '')
                except:
                    domain = '其他'
            else:
                domain = 'HackerNews讨论'

            if domain in domains:
                domains[domain] += 1
            else:
                domains[domain] = 1

        # 排序并取前10个
        top_domains = sorted(domains.items(), key=lambda x: x[1], reverse=True)[:10]

        if not top_domains:
            return ""

        result = "## 🌐 热门来源网站\n\n"
        for domain, count in top_domains:
            result += f"- **{domain}**: {count} 篇文章\n"
        result += "\n"

        return result

    def _generate_llm_analysis(self, stories, hours):
        """使用LLM生成中文趋势分析"""
        try:
            # 准备分析数据 - 取前15篇文章
            top_stories = stories[:15]

            # 构建用户消息内容
            user_content = f"请分析过去{hours}小时HackerNews上的热门技术文章：\n\n"

            for i, story in enumerate(top_stories, 1):
                title = story.get('title', '无标题')
                score = story.get('score', 0)
                comments = story.get('descendants', 0)
                user_content += f"{i}. 《{title}》 (热度: {score}分, 评论: {comments}条)\n"

            # 调用LLM，明确传递 report_type='hackernews'
            analysis = self.llm.generate_daily_report(
                user_content,
                report_type='hackernews'  # 新增参数
            )

            if analysis and analysis != "DRY RUN":
                return analysis
            return None

        except Exception as e:
            LOG.error(f"LLM分析生成失败: {e}")
            return None

    def _save_report(self, content, hours):
        """保存报告到文件"""
        os.makedirs('exports', exist_ok=True)

        timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
        filename = f"exports/hackernews_trend_report_{hours}h_{timestamp}.md"

        with open(filename, 'w', encoding='utf-8') as f:
            f.write(content)

        return filename