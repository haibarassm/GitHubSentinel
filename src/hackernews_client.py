# src/hackernews_client.py
import requests
from datetime import datetime, timedelta
from logger import LOG
import json
import os
import time
from concurrent.futures import ThreadPoolExecutor, as_completed


class HackerNewsClient:
    """Hacker News API客户端"""

    BASE_URL = "https://hacker-news.firebaseio.com/v0"

    def __init__(self):
        self.session = requests.Session()
        # 设置连接池大小
        adapter = requests.adapters.HTTPAdapter(pool_connections=20, pool_maxsize=20)
        self.session.mount('https://', adapter)

    def get_top_stories(self, limit=100):
        """获取Top stories"""
        try:
            response = self.session.get(f"{self.BASE_URL}/topstories.json")
            response.raise_for_status()
            story_ids = response.json()[:limit]
            return self._get_stories_details_parallel(story_ids)
        except Exception as e:
            LOG.error(f"获取Hacker News top stories失败: {e}")
            return []

    def get_new_stories(self, limit=100):
        """获取最新 stories"""
        try:
            response = self.session.get(f"{self.BASE_URL}/newstories.json")
            response.raise_for_status()
            story_ids = response.json()[:limit]
            return self._get_stories_details_parallel(story_ids)
        except Exception as e:
            LOG.error(f"获取Hacker News new stories失败: {e}")
            return []

    def get_stories_by_hours(self, hours=24, min_score=0, keywords=None, limit=100):
        """
        获取指定小时内的stories，支持过滤 - 优化版本
        """
        start_time = time.time()

        try:
            # 获取最新的story IDs（前500个）
            response = self.session.get(f"{self.BASE_URL}/newstories.json")
            response.raise_for_status()
            story_ids = response.json()[:300]  # 只取前300个，减少请求数

            cutoff_time = datetime.now() - timedelta(hours=hours)
            cutoff_timestamp = int(cutoff_time.timestamp())

            stories = []
            keywords = keywords or []

            # 使用线程池并行获取story详情
            with ThreadPoolExecutor(max_workers=10) as executor:
                # 提交所有任务
                future_to_id = {
                    executor.submit(self._get_story_detail, story_id): story_id
                    for story_id in story_ids
                }

                # 按完成顺序处理结果
                for future in as_completed(future_to_id):
                    story = future.result()
                    if not story:
                        continue

                    # 时间过滤
                    if story.get('time', 0) < cutoff_timestamp:
                        # 如果时间太早，可以继续检查后面的（但不能break，因为不是按时间顺序返回的）
                        continue

                    # 热度过滤
                    if story.get('score', 0) < min_score:
                        continue

                    # 关键词过滤
                    if keywords:
                        title = story.get('title', '').lower()
                        if not any(kw.lower() in title for kw in keywords if kw):
                            continue

                    stories.append(story)

                    # 如果已经找到足够多的文章，可以取消剩余的任务
                    if len(stories) >= limit:
                        # 取消未完成的任务
                        for f in future_to_id:
                            if not f.done():
                                f.cancel()
                        break

            # 按热度排序
            stories.sort(key=lambda x: x.get('score', 0), reverse=True)

            elapsed_time = time.time() - start_time
            LOG.info(f"获取到{len(stories)}条符合条件的Hacker News stories，耗时{elapsed_time:.2f}秒")
            return stories

        except Exception as e:
            LOG.error(f"获取指定小时内的Hacker News stories失败: {e}")
            return []

    def _get_stories_details_parallel(self, story_ids):
        """并行批量获取story详情"""
        stories = []
        with ThreadPoolExecutor(max_workers=10) as executor:
            futures = [executor.submit(self._get_story_detail, story_id) for story_id in story_ids]
            for future in as_completed(futures):
                story = future.result()
                if story:
                    stories.append(story)
        return stories

    def _get_story_detail(self, story_id):
        """获取单个story详情"""
        try:
            response = self.session.get(f"{self.BASE_URL}/item/{story_id}.json", timeout=5)
            response.raise_for_status()
            story = response.json()

            # 只返回story类型（排除comment等）
            if story and story.get('type') == 'story':
                return {
                    'id': story.get('id'),
                    'title': story.get('title'),
                    'url': story.get('url', f"https://news.ycombinator.com/item?id={story_id}"),
                    'score': story.get('score', 0),
                    'by': story.get('by', 'unknown'),
                    'time': story.get('time', 0),
                    'descendants': story.get('descendants', 0),  # 评论数
                    'text': story.get('text', '')
                }
            return None
        except Exception as e:
            LOG.debug(f"获取story {story_id}详情失败: {e}")
            return None

    def export_stories_by_hours(self, hours, min_score=0, keywords=None, limit=100):
        """
        导出指定小时内的stories到文件，支持过滤
        """
        try:
            stories = self.get_stories_by_hours(
                hours=hours,
                min_score=min_score,
                keywords=keywords,
                limit=limit
            )

            # 创建exports目录（如果不存在）
            os.makedirs('exports', exist_ok=True)

            # 生成文件名
            filename = f"exports/hackernews_{hours}h_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"

            # 保存到文件
            with open(filename, 'w', encoding='utf-8') as f:
                json.dump(stories, f, ensure_ascii=False, indent=2)

            LOG.info(f"已导出{len(stories)}条Hacker News stories到{filename}")
            return filename, stories
        except Exception as e:
            LOG.error(f"导出Hacker News stories失败: {e}")
            return None, []