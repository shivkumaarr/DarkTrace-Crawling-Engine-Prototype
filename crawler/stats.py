import time

class CrawlStats:
    def __init__(self):
        self.started = time.perf_counter()
        self.processed = 0
        self.discovered = 0
        self.successful = 0
        self.failed = 0
        self.http_errors = 0
        self.max_depth = 0
        self.latencies = []

    @property
    def duration_seconds(self):
        return round(time.perf_counter() - self.started, 2)

    @property
    def average_latency_ms(self):
        return round(sum(self.latencies) / len(self.latencies), 2) if self.latencies else 0

    def as_dict(self):
        return {
            "duration_seconds": self.duration_seconds,
            "urls_discovered": self.discovered,
            "urls_processed": self.processed,
            "successful_requests": self.successful,
            "failed_requests": self.failed,
            "http_error_responses": self.http_errors,
            "average_latency_ms": self.average_latency_ms,
            "max_depth": self.max_depth,
        }
