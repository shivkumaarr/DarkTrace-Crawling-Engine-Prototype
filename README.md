# DarkTrace Crawling Engine Prototype

A modular Python web-crawling engine designed for authorized research,
cybersecurity labs, OSINT workflows, and website structure analysis.

> **Safety:** Use this crawler only on websites and systems you are authorized
> to test. The default configuration stays inside the starting domain and
> respects `robots.txt`.

## Highlights

- Single-source / single-domain crawling
- Depth-limited discovery
- URL deduplication
- `robots.txt` support
- Configurable request delay and timeout
- Retry and error handling
- Metadata extraction
- JSON + CSV exports
- Structured logging
- Crawl statistics
- Optional concurrent crawling
- Optional Elasticsearch integration hook
- Simple architecture designed for extension

## Architecture

```text
                 +------------------+
                 |    Seed URL      |
                 +--------+---------+
                          |
                          v
                 +------------------+
                 | Crawl Controller |
                 +--------+---------+
                          |
              +-----------+-----------+
              |                       |
              v                       v
      +---------------+       +---------------+
      |  URL Queue    |       | robots.txt    |
      +-------+-------+       +---------------+
              |
              v
      +---------------+
      | HTTP Fetcher  |
      +-------+-------+
              |
              v
      +---------------+
      | HTML Parser   |
      +-------+-------+
              |
        +-----+------+
        |            |
        v            v
   +---------+   +---------+
   |Metadata |   | New URLs|
   +----+----+   +----+----+
        |             |
        +------+------+
               |
               v
      +--------------------+
      | JSON / CSV / ES    |
      +--------------------+
```

## Project Structure

```text
DarkTrace-Crawling-Engine-Prototype/
├── crawler/
│   ├── engine.py
│   ├── fetcher.py
│   ├── parser.py
│   ├── queue_manager.py
│   ├── robots.py
│   ├── metadata.py
│   ├── exporter.py
│   ├── logger.py
│   ├── stats.py
│   └── elasticsearch_hook.py
├── config/
│   └── settings.py
├── docs/
│   └── ARCHITECTURE.md
├── output/
├── logs/
├── tests/
│   └── test_parser.py
├── main.py
├── requirements.txt
└── README.md
```

## Installation

```bash
python -m venv .venv
```

Windows:

```powershell
.venv\Scripts\activate
```

Linux/macOS:

```bash
source .venv/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

## Run

Interactive:

```bash
python main.py
```

Example:

```text
Enter target URL: https://example.com
```

The crawler saves:

```text
output/crawl_results.json
output/crawl_results.csv
logs/crawler.log
```

## Configuration

Edit `config/settings.py`:

- `MAX_DEPTH` — maximum link depth
- `MAX_PAGES` — page limit
- `REQUEST_DELAY` — delay between requests
- `TIMEOUT` — HTTP timeout
- `MAX_RETRIES` — retry attempts
- `WORKERS` — concurrent workers
- `SAME_DOMAIN_ONLY` — keep URLs in the starting domain
- `RESPECT_ROBOTS_TXT` — enforce robots.txt
- `USER_AGENT` — crawler identification

The default settings are intentionally conservative.

## Output Fields

Each result can contain:

```json
{
  "url": "https://example.com/",
  "title": "Example Domain",
  "status_code": 200,
  "content_type": "text/html",
  "content_length": 1256,
  "depth": 0,
  "latency_ms": 153.42,
  "timestamp": "2026-09-24T22:00:00+00:00",
  "links_found": 2
}
```

## Crawl Statistics

The engine reports:

- URLs discovered
- URLs processed
- Successful requests
- Failed requests
- HTTP error responses
- Average latency
- Maximum depth reached
- Total crawl duration

## Elasticsearch Hook

`crawler/elasticsearch_hook.py` contains an optional integration layer.

It is disabled by default. Configure an Elasticsearch endpoint only when you
have an authorized Elasticsearch instance available.

Example environment variables:

```text
DARKTRACE_ES_URL=http://127.0.0.1:9200
DARKTRACE_ES_INDEX=darktrace-crawl
```

Then enable the hook in `config/settings.py`.

## Testing

Run:

```bash
python -m unittest discover -s tests
```

## Future Work

- Persistent crawl-state database
- Resume after interruption
- Incremental crawling
- Content hashing
- Sitemap support
- More detailed MIME/content analysis
- Dashboard integration
- Distributed queue support

## Author

**Shiv Kumar**

Cyber Security | Red Team Operator | Threat Intelligence | Security Research

## Disclaimer

This project is for educational, research, and authorized security testing.
Do not use it to bypass access controls, authentication, rate limits, or other
security controls.
