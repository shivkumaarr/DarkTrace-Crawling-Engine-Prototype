MAX_DEPTH = 2
MAX_PAGES = 50
REQUEST_DELAY = 0.5
TIMEOUT = 10
MAX_RETRIES = 2
WORKERS = 4

SAME_DOMAIN_ONLY = True
RESPECT_ROBOTS_TXT = True

USER_AGENT = "DarkTraceCrawler/1.0 (Authorized Research Prototype)"

OUTPUT_JSON = "output/crawl_results.json"
OUTPUT_CSV = "output/crawl_results.csv"
LOG_FILE = "logs/crawler.log"

ELASTICSEARCH_ENABLED = False
ELASTICSEARCH_URL = "http://127.0.0.1:9200"
ELASTICSEARCH_INDEX = "darktrace-crawl"
