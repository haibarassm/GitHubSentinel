# src/github_client.py

import requests
from datetime import datetime, date, timedelta
import os
import time
from logger import LOG


class GitHubClient:
    BASE_URL = "https://api.github.com"

    def __init__(self, token):
        self.token = token
        self.headers = {
            "Authorization": f"token {self.token}",
            "Accept": "application/vnd.github+json"
        }

    # =============================
    # 通用分页请求方法
    # =============================
    def _get_with_pagination(self, url, params=None):
        """
        自动分页获取所有数据
        """
        all_items = []
        page = 1

        if params is None:
            params = {}

        params["per_page"] = 100  # 每页最大 100
        while True:
            params["page"] = page
            LOG.debug(f"Fetching page {page} from {url}")

            response = requests.get(url, headers=self.headers, params=params)
            response.raise_for_status()

            items = response.json()

            if not items:
                break

            all_items.extend(items)

            if len(items) < 100:
                break

            page += 1

            # 避免触发速率限制
            time.sleep(0.2)

        return all_items

    # =============================
    # Search API 分页封装
    # =============================
    def _search_with_pagination(self, query):
        url = f"{self.BASE_URL}/search/issues"
        all_items = []
        page = 1

        while True:
            params = {
                "q": query,
                "per_page": 100,
                "page": page
            }

            LOG.debug(f"Search query page {page}: {query}")

            response = requests.get(url, headers=self.headers, params=params)
            response.raise_for_status()

            data = response.json()
            items = data.get("items", [])

            if not items:
                break

            all_items.extend(items)

            if len(items) < 100:
                break

            page += 1
            time.sleep(0.3)

        return all_items

    # =============================
    # Commits（支持 since + until）
    # =============================
    def fetch_commits(self, repo, since=None, until=None):
        url = f"{self.BASE_URL}/repos/{repo}/commits"
        params = {}

        if since:
            params["since"] = since
        if until:
            params["until"] = until

        return self._get_with_pagination(url, params)

    # =============================
    # Issues（用 Search API 支持时间区间）
    # =============================
    def fetch_issues(self, repo, since=None, until=None):
        query = f"repo:{repo} type:issue is:closed"

        if since and until:
            query += f" closed:{since}..{until}"
        elif since:
            query += f" closed:>={since}"

        return self._search_with_pagination(query)

    # =============================
    # Pull Requests（用 Search API 支持时间区间）
    # =============================
    def fetch_pull_requests(self, repo, since=None, until=None):
        query = f"repo:{repo} type:pr is:closed"

        if since and until:
            query += f" merged:{since}..{until}"
        elif since:
            query += f" merged:>={since}"

        return self._search_with_pagination(query)

    # =============================
    # 聚合更新
    # =============================
    def fetch_updates(self, repo, since=None, until=None):
        return {
            "commits": self.fetch_commits(repo, since, until),
            "issues": self.fetch_issues(repo, since, until),
            "pull_requests": self.fetch_pull_requests(repo, since, until)
        }

    # =============================
    # 导出当天进展
    # =============================
    def export_daily_progress(self, repo):
        today = datetime.now().date().isoformat()
        updates = self.fetch_updates(repo, since=today, until=today)

        return self._export_markdown(repo, updates, today, today)

    # =============================
    # 导出指定天数进展
    # =============================
    def export_progress_by_date_range(self, repo, days):
        today = date.today()
        since = today - timedelta(days=days)

        updates = self.fetch_updates(
            repo,
            since=since.isoformat(),
            until=today.isoformat()
        )

        return self._export_markdown(
            repo,
            updates,
            since.isoformat(),
            today.isoformat()
        )

    # =============================
    # Markdown 输出统一方法
    # =============================
    def _export_markdown(self, repo, updates, since, until):
        repo_dir = os.path.join("daily_progress", repo.replace("/", "_"))
        os.makedirs(repo_dir, exist_ok=True)

        file_name = f"{since}_to_{until}.md"
        file_path = os.path.join(repo_dir, file_name)

        with open(file_path, "w", encoding="utf-8") as file:
            file.write(f"# Progress for {repo} ({since} to {until})\n\n")

            file.write("## Commits\n")
            for commit in updates["commits"]:
                msg = commit["commit"]["message"].split("\n")[0]
                file.write(f"- {msg} ({commit['sha'][:7]})\n")

            file.write("\n## Issues Closed\n")
            for issue in updates["issues"]:
                file.write(f"- {issue['title']} #{issue['number']}\n")

            file.write("\n## Pull Requests Merged\n")
            for pr in updates["pull_requests"]:
                file.write(f"- {pr['title']} #{pr['number']}\n")

        LOG.info(f"Exported progress to {file_path}")
        return file_path