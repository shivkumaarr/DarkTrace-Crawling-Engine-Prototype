from collections import deque
from threading import Lock

class QueueManager:
    def __init__(self):
        self.queue = deque()
        self.seen = set()
        self.lock = Lock()

    def add(self, url, depth=0):
        with self.lock:
            if url in self.seen:
                return False
            self.seen.add(url)
            self.queue.append((url, depth))
            return True

    def get(self):
        with self.lock:
            return self.queue.popleft() if self.queue else None

    def empty(self):
        with self.lock:
            return not self.queue

    def __len__(self):
        with self.lock:
            return len(self.queue)
