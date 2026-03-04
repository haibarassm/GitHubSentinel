# config.py
import json
import os
from logger import LOG


class Config:
    """配置管理类"""

    def __init__(self):
        self.load_config()

    def load_config(self):
        """加载配置文件"""
        try:
            # 直接从 config.json 读取配置
            with open('config.json', 'r', encoding='utf-8') as f:
                config = json.load(f)

            # GitHub Token 可以通过环境变量覆盖（敏感信息）
            self.github_token = os.getenv('GITHUB_TOKEN', config.get('github_token', ''))

            # GitHub 配置
            self.github_enabled = config.get('github_enabled', True)
            self.github_freq_days = config.get('github_progress_frequency_days', 1)
            self.github_exec_time = config.get('github_progress_execution_time', "08:00")

            # HackerNews 配置（直接从配置文件读取）
            self.hackernews_enabled = config.get('hackernews_enabled', True)
            self.hackernews_freq_hours = config.get('hackernews_frequency_hours', 6)
            self.hackernews_exec_time = config.get('hackernews_execution_time', "10:00")
            self.hackernews_hours = config.get('hackernews_time_range_hours', 24)
            self.hackernews_min_score = config.get('hackernews_min_score', 0)
            self.hackernews_max_stories = config.get('hackernews_max_stories', 100)
            self.hackernews_keywords = config.get('hackernews_keywords', [])

            # 通用配置
            self.subscriptions_file = config.get('subscriptions_file', 'subscriptions.json')
            self.slack_webhook_url = config.get('slack_webhook_url', '')

            # 邮件配置
            self.email = config.get('email', {})
            # 邮件密码可以通过环境变量覆盖（敏感信息）
            self.email['password'] = os.getenv('EMAIL_PASSWORD', self.email.get('password', ''))

            # 保留旧配置字段以兼容现有代码
            self.freq_days = self.github_freq_days
            self.exec_time = self.github_exec_time

            LOG.info("配置加载成功")
            LOG.info(f"GitHub监控: {'启用' if self.github_enabled else '禁用'}")
            LOG.info(f"HackerNews监控: {'启用' if self.hackernews_enabled else '禁用'}")
            LOG.info(f"HackerNews过滤条件: 最低热度={self.hackernews_min_score}, 关键词={self.hackernews_keywords}")

        except FileNotFoundError:
            LOG.error("配置文件 config.json 不存在")
            raise
        except json.JSONDecodeError as e:
            LOG.error(f"配置文件格式错误: {e}")
            raise
        except Exception as e:
            LOG.error(f"加载配置时发生未知错误: {e}")
            raise

    def get_github_config(self):
        """获取GitHub配置"""
        return {
            'enabled': self.github_enabled,
            'token': self.github_token,
            'freq_days': self.github_freq_days,
            'exec_time': self.github_exec_time
        }

    def get_hackernews_config(self):
        """获取HackerNews配置"""
        return {
            'enabled': self.hackernews_enabled,
            'freq_hours': self.hackernews_freq_hours,
            'exec_time': self.hackernews_exec_time,
            'hours': self.hackernews_hours,
            'min_score': self.hackernews_min_score,
            'max_stories': self.hackernews_max_stories,
            'keywords': self.hackernews_keywords
        }

    def get_email_config(self):
        """获取邮件配置"""
        return self.email

    def reload(self):
        """重新加载配置"""
        LOG.info("重新加载配置")
        self.load_config()