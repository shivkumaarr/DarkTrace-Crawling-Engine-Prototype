from bs4 import BeautifulSoup
from urllib.parse import urljoin, urldefrag

def normalize_url(url):
    url, _ = urldefrag(url)
    return url.rstrip("/") or url

def parse_html(html, base_url):
    soup = BeautifulSoup(html, "lxml")

    title = soup.title.get_text(" ", strip=True) if soup.title else ""
    links = set()

    for tag in soup.find_all("a", href=True):
        href = tag.get("href", "").strip()
        if not href:
            continue
        full_url = normalize_url(urljoin(base_url, href))
        if full_url.startswith(("http://", "https://")):
            links.add(full_url)

    return title, sorted(links)
