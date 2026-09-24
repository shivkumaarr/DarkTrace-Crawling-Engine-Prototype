import json
import os
import requests
from crawler.logger import logger

class ElasticsearchHook:
    def __init__(self, url, index):
        self.url = url.rstrip("/")
        self.index = index

    def send(self, document):
        endpoint = f"{self.url}/{self.index}/_doc"
        try:
            response = requests.post(
                endpoint,
                headers={"Content-Type": "application/json"},
                data=json.dumps(document),
                timeout=5,
            )
            response.raise_for_status()
            return True
        except requests.RequestException as exc:
            logger.warning("Elasticsearch hook failed: %s", exc)
            return False

def from_environment(default_url, default_index):
    return ElasticsearchHook(
        os.getenv("DARKTRACE_ES_URL", default_url),
        os.getenv("DARKTRACE_ES_INDEX", default_index),
    )
