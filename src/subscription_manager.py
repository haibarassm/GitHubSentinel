# src/subscription_manager.py
import json
import os
from logger import LOG


class SubscriptionManager:
    def __init__(self, subscriptions_file):
        self.subscriptions_file = subscriptions_file
        self.subscriptions = self.load_subscriptions()

    def load_subscriptions(self):
        """加载订阅配置"""
        try:
            if os.path.exists(self.subscriptions_file):
                with open(self.subscriptions_file, 'r', encoding='utf-8') as f:
                    data = json.load(f)

                # 确保数据结构正确
                if isinstance(data, list):
                    # 兼容旧格式：转换为新格式
                    LOG.info("检测到旧版订阅格式，正在转换...")
                    return {"github": data}
                elif isinstance(data, dict):
                    # 确保有必要的键
                    if "github" not in data:
                        data["github"] = []
                    return data
            else:
                # 文件不存在，返回默认结构
                return {"github": []}
        except Exception as e:
            LOG.error(f"加载订阅文件失败: {e}")
            return {"github": []}

    def save_subscriptions(self):
        """保存订阅配置"""
        try:
            with open(self.subscriptions_file, 'w', encoding='utf-8') as f:
                json.dump(self.subscriptions, f, indent=4, ensure_ascii=False)
            LOG.info("订阅配置已保存")
        except Exception as e:
            LOG.error(f"保存订阅配置失败: {e}")

    # GitHub订阅管理
    def list_github_subscriptions(self):
        """获取GitHub订阅列表"""
        return self.subscriptions.get("github", [])

    def add_github_subscription(self, repo):
        """添加GitHub仓库订阅"""
        if "github" not in self.subscriptions:
            self.subscriptions["github"] = []

        if repo not in self.subscriptions["github"]:
            self.subscriptions["github"].append(repo)
            self.save_subscriptions()
            LOG.info(f"已添加GitHub订阅: {repo}")
            return True
        return False

    def remove_github_subscription(self, repo):
        """移除GitHub仓库订阅"""
        if "github" in self.subscriptions and repo in self.subscriptions["github"]:
            self.subscriptions["github"].remove(repo)
            self.save_subscriptions()
            LOG.info(f"已移除GitHub订阅: {repo}")
            return True
        return False

    # 兼容旧接口（保持原有方法名）
    def list_subscriptions(self):
        """兼容旧版接口：返回GitHub订阅列表"""
        return self.list_github_subscriptions()

    def add_subscription(self, repo):
        """兼容旧版接口：添加GitHub订阅"""
        return self.add_github_subscription(repo)

    def remove_subscription(self, repo):
        """兼容旧版接口：移除GitHub订阅"""
        return self.remove_github_subscription(repo)