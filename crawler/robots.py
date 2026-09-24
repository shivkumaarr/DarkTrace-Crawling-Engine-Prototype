from urllib.robotparser import RobotFileParser
from urllib.parse import urljoin
from crawler.logger import logger

class RobotsChecker:
    def __init__(self, seed_url, user_agent):
        self.user_agent = user_agent
        robots_url = urljoin(seed_url, "/robots.txt")
        self.parser = RobotFileParser(robots_url)
        self.parser.read()
        logger.info("Loaded robots.txt from %s", robots_url)

    def allowed(self, url):
        try:
            return self.parser.can_fetch(self.user_agent, url)
        except Exception as exc:
            logger.warning("robots.txt check failed for %s: %s", url, exc)
            return False
