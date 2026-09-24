# DarkTrace Crawling Engine Prototype

DarkTrace Crawling Engine Prototype is a modular Python-based web crawling engine built for authorized security research, web reconnaissance, OSINT workflows, and website structure analysis.

The project demonstrates how a crawling engine can discover URLs, retrieve web content, extract metadata, manage crawl depth, handle errors, and store results in structured formats.

It is designed as a lightweight prototype that can be extended with databases, dashboards, threat intelligence platforms, and other security-analysis components.

---

## Project Objectives

The main objective of DarkTrace is to understand and implement the core components of a modern crawling engine.

The crawler focuses on:

* Controlled URL discovery
* Efficient queue management
* Domain-restricted crawling
* Depth-based navigation
* Metadata collection
* Request handling and retries
* Crawl statistics
* Structured result storage
* Modular architecture for future expansion

---

## Key Features

### Single-Source Crawling

The crawler starts from one seed URL and discovers additional pages from links found on that website.

### Depth Control

A maximum crawl depth can be configured to control how far the crawler follows discovered links.

Example:

```text
Depth 0 → Seed URL
Depth 1 → Links found on seed
Depth 2 → Links found on depth 1 pages
```

### URL Queue Management

The queue manager maintains pending URLs and prevents the same URL from being processed multiple times.

### robots.txt Support

The crawler can check `robots.txt` rules before requesting pages.

This behaviour is enabled by default and can be controlled from the project configuration.

### Domain Restriction

By default, the crawler stays within the host of the original seed URL.

This helps keep the crawl controlled and prevents unintended expansion to unrelated domains.

### Retry and Error Handling

Temporary request failures are handled through configurable retry attempts, timeout values, and logging.

### Metadata Extraction

The crawler collects useful page information such as:

```text
URL
Page Title
HTTP Status Code
Content Type
Content Length
Crawl Depth
Request Latency
Timestamp
Number of Links
```

### JSON and CSV Export

Collected results are exported into:

```text
output/crawl_results.json
output/crawl_results.csv
```

### Logging

Crawler activities and errors are recorded in:

```text
logs/crawler.log
```

### Crawl Statistics

At the end of a crawl, the engine reports information such as:

```text
URLs discovered
URLs processed
Successful requests
HTTP errors
Average latency
Maximum depth
Total crawl duration
```

### Concurrent Crawling

The prototype uses a small configurable worker pool to process multiple queued URLs concurrently while keeping URL management thread-safe.

---

## Architecture

```text
                  Seed URL
                     |
                     v
             +---------------+
             | Crawl Engine  |
             +-------+-------+
                     |
             +-------v-------+
             | URL Queue     |
             +-------+-------+
                     |
             +-------v-------+
             | robots.txt    |
             | Validation    |
             +-------+-------+
                     |
             +-------v-------+
             | HTTP Fetcher  |
             +-------+-------+
                     |
             +-------v-------+
             | HTML Parser   |
             +-------+-------+
                /         \
               /           \
              v             v
       Metadata         New URLs
          |                |
          |                v
          |          Queue Manager
          |                |
          +-------+--------+
                  |
                  v
        JSON / CSV / Optional ES
```

---

## Project Structure

```text
DarkTrace-Crawling-Engine-Prototype/
│
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
│
├── config/
│   ├── __init__.py
│   └── settings.py
│
├── docs/
│   └── ARCHITECTURE.md
│
├── output/
├── logs/
│
├── tests/
│   └── test_parser.py
│
├── main.py
├── requirements.txt
├── .gitignore
└── README.md
```

---

## Technologies Used

* Python 3
* Requests
* BeautifulSoup
* lxml
* urllib
* ThreadPoolExecutor
* JSON
* CSV
* Python Logging

---

## Installation

Clone the repository:

```bash
git clone https://github.com/your-username/DarkTrace-Crawling-Engine-Prototype.git
cd DarkTrace-Crawling-Engine-Prototype
```

Create a virtual environment:

### Windows

```powershell
python -m venv .venv
.venv\Scripts\activate
```

### Linux

```bash
python3 -m venv .venv
source .venv/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## Usage

Run the crawler:

```bash
python main.py
```

The program asks for a starting URL:

```text
Enter authorized target URL: https://example.com
```

After completion, the crawler displays statistics and saves the collected data.

Example:

```text
Crawl completed.

Pages processed: 12
Pages discovered: 18
Successful requests: 11
HTTP errors: 1
Average latency: 184.52 ms
Max depth: 2
Duration: 4.31 seconds
```

---

## Configuration

Crawler behaviour can be customized from:

```text
config/settings.py
```

Important settings include:

```python
MAX_DEPTH = 2
MAX_PAGES = 50
REQUEST_DELAY = 0.5
TIMEOUT = 10
MAX_RETRIES = 2
WORKERS = 4
```

Domain and robots controls:

```python
SAME_DOMAIN_ONLY = True
RESPECT_ROBOTS_TXT = True
```

These settings keep the prototype bounded and easier to use in an authorized testing environment.

---

## Output Example

A result record can look like:

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

---

## Testing

Basic parser tests are included in the project.

Run:

```bash
python -m unittest discover -s tests
```

---

## Elasticsearch Integration

The project contains an optional Elasticsearch integration hook:

```text
crawler/elasticsearch_hook.py
```

It is disabled by default.

The hook can be connected to an authorized Elasticsearch environment for indexing crawl metadata.

Example configuration:

```text
DARKTRACE_ES_URL=http://127.0.0.1:9200
DARKTRACE_ES_INDEX=darktrace-crawl
```

This makes the prototype easier to extend into a larger security-monitoring or threat-intelligence pipeline.

---

## Future Improvements

The current prototype can be extended with:

* Persistent crawl-state storage
* Resume-after-failure functionality
* Incremental crawling
* Sitemap support
* Content hashing
* Database integration
* Search and dashboard functionality
* Threat-intelligence enrichment
* Distributed crawling architecture

---

## Learning Outcomes

This project provides practical experience with:

* Web crawling concepts
* HTTP request handling
* URL normalization
* Queue-based processing
* HTML parsing
* Metadata extraction
* Concurrent task execution
* Error handling
* Logging
* Structured data export
* Modular Python architecture

---

## Disclaimer

DarkTrace Crawling Engine Prototype is intended for educational, research, and authorized security-testing purposes.

Only crawl websites and systems where you have permission to perform the activity.

Do not use the project to bypass authentication, access controls, rate limits, robots rules, or other security mechanisms.

---

## Author

**Shiv Kumar**

Red Team Operator | Threat Intelligence | Security Research | Penetration Tester

---

## Project Status

**Status:** Prototype / Research Project

The architecture is intentionally modular so that individual components can be improved or replaced without redesigning the complete system.
