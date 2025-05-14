import urllib.robotparser
import urllib.request
from urllib.error import URLError, HTTPError
from urllib.parse import quote_plus
import requests
from bs4 import BeautifulSoup
from fake_useragent import UserAgent
import time
import random
import pandas as pd
import os

class CrawlabilityChecker:
    def __init__(self, robots_url='https://www.amazon.com/robots.txt'):
        self.robots_url = robots_url
        self.parser = urllib.robotparser.RobotFileParser()
        self._load_robots_txt()

    def _load_robots_txt(self):
        try:
            self.parser.set_url(self.robots_url)
            self.parser.read()
            print(f"✅ Loaded robots.txt from {self.robots_url}")
        except (URLError, HTTPError) as e:
            print(f"❌ Failed to load robots.txt: {e}")
            self.parser = None

    def can_crawl(self, url, user_agent='*'):
        if self.parser is None:
            print("⚠️ robots.txt parser not initialized.")
            return False

        is_allowed = self.parser.can_fetch(user_agent, url)
        reason = "ALLOWED ✅" if is_allowed else "BLOCKED ❌"
        print(f"[{user_agent}] {reason} -> {url}")
        return is_allowed

checker = CrawlabilityChecker()

urls_to_check = [
  'https://www.amazon.com/dp/B09G3HRMVP',               # Allowed path (Product Page)
  'https://www.amazon.com/wishlist/universal',          # Allowed path (But Flase Negative)
  'https://www.amazon.com/gp/customer-reviews/write-a-review.html'  # Disallowed
]

for url in urls_to_check:
  checker.can_crawl(url)