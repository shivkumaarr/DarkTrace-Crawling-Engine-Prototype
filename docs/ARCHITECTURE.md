# DarkTrace Architecture

## Components

**Crawl Controller**
Coordinates the crawl lifecycle.

**Queue Manager**
Stores URLs with their crawl depth and avoids duplicates.

**Fetcher**
Performs HTTP requests with timeout, delay, and retry controls.

**Robots Checker**
Uses `robots.txt` rules before fetching a URL.

**Parser**
Extracts page titles and hyperlinks from HTML.

**Metadata Collector**
Creates structured records for each processed URL.

**Exporter**
Writes JSON and CSV result files.

**Statistics**
Tracks crawl duration, request counts, latency, errors, and depth.

**Elasticsearch Hook**
Optional integration point for indexing crawl records.

## Data Flow

`Seed -> Queue -> Robots Check -> Fetch -> Parse -> Metadata -> Queue/Export`

The engine keeps the default scope inside the starting host and applies a
maximum depth and page count to keep crawling bounded.
