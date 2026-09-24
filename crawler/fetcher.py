import time
import requests
from config import settings
from crawler.logger import logger

class Fetcher:
    def __init__(self):
        self.session = requests.Session()
        self.session.headers.update({"User-Agent": settings.USER_AGENT})

    def fetch(self, url):
        last_error = None
        for attempt in range(settings.MAX_RETRIES + 1):
            started = time.perf_counter()
            try:
                response = self.session.get(
                    url,
                    timeout=settings.TIMEOUT,
                    allow_redirects=True,
                )
                latency_ms = round((time.perf_counter() - started) * 1000, 2)
                time.sleep(settings.REQUEST_DELAY)
                return response, latency_ms
            except requests.RequestException as exc:
                last_error = exc
                logger.warning(
                    "Request failed (%s/%s) %s: %s",
                    attempt + 1,
                    settings.MAX_RETRIES + 1,
                    url,
                    exc,
                )
                time.sleep(settings.REQUEST_DELAY)

        return None, None
