from concurrent.futures import ThreadPoolExecutor, as_completed
from urllib.parse import urlparse
from config import settings
from crawler.queue_manager import QueueManager
from crawler.fetcher import Fetcher
from crawler.parser import parse_html
from crawler.metadata import build_metadata
from crawler.robots import RobotsChecker
from crawler.exporter import export_json, export_csv
from crawler.logger import logger
from crawler.stats import CrawlStats
from crawler.elasticsearch_hook import from_environment

class CrawlEngine:
    def __init__(self, start_url):
        self.start_url = start_url.rstrip("/") or start_url
        self.domain = urlparse(self.start_url).netloc.lower()
        self.queue = QueueManager()
        self.results = []
        self.stats = CrawlStats()
        self.fetcher = Fetcher()
        self.robots = None

        if settings.RESPECT_ROBOTS_TXT:
            try:
                self.robots = RobotsChecker(self.start_url, settings.USER_AGENT)
            except Exception as exc:
                logger.warning("Could not load robots.txt: %s", exc)
                self.robots = None

        self.es_hook = (
            from_environment(settings.ELASTICSEARCH_URL, settings.ELASTICSEARCH_INDEX)
            if settings.ELASTICSEARCH_ENABLED
            else None
        )

    def allowed_domain(self, url):
        if not settings.SAME_DOMAIN_ONLY:
            return True
        return urlparse(url).netloc.lower() == self.domain

    def process(self, item):
        url, depth = item

        if self.robots and not self.robots.allowed(url):
            logger.info("Blocked by robots.txt: %s", url)
            return None

        response, latency_ms = self.fetcher.fetch(url)
        if response is None:
            self.stats.failed += 1
            return build_metadata(
                url, "", None, "", 0, depth, None, 0, "request_failed"
            )

        self.stats.processed += 1
        self.stats.max_depth = max(self.stats.max_depth, depth)

        if latency_ms is not None:
            self.stats.latencies.append(latency_ms)

        content_type = response.headers.get("Content-Type", "")
        content_length = len(response.content)

        if response.status_code >= 400:
            self.stats.http_errors += 1
            return build_metadata(
                url,
                "",
                response.status_code,
                content_type,
                content_length,
                depth,
                latency_ms,
                0,
            )

        self.stats.successful += 1

        title = ""
        links = []
        if "text/html" in content_type.lower():
            title, links = parse_html(response.text, url)

        result = build_metadata(
            url,
            title,
            response.status_code,
            content_type,
            content_length,
            depth,
            latency_ms,
            len(links),
        )

        if depth < settings.MAX_DEPTH:
            for link in links:
                if self.allowed_domain(link) and self.queue.add(link, depth + 1):
                    self.stats.discovered += 1

        if self.es_hook:
            self.es_hook.send(result)

        return result

    def run(self):
        logger.info("Starting crawl: %s", self.start_url)
        self.queue.add(self.start_url, 0)
        self.stats.discovered = 1

        # Use a small worker pool, while queue operations remain thread-safe.
        with ThreadPoolExecutor(max_workers=max(1, settings.WORKERS)) as pool:
            while not self.queue.empty() and len(self.results) < settings.MAX_PAGES:
                batch = []
                while not self.queue.empty() and len(batch) < settings.WORKERS:
                    batch.append(self.queue.get())

                futures = [pool.submit(self.process, item) for item in batch]
                for future in as_completed(futures):
                    result = future.result()
                    if result:
                        self.results.append(result)

        export_json(self.results, settings.OUTPUT_JSON)
        export_csv(self.results, settings.OUTPUT_CSV)
        logger.info("Crawl completed: %s", self.stats.as_dict())
        return self.results, self.stats.as_dict()
