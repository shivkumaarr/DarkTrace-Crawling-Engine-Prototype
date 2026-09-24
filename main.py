from crawler.engine import CrawlEngine

def main():
    url = input("Enter authorized target URL: ").strip()
    if not url.startswith(("http://", "https://")):
        print("Please enter a valid http:// or https:// URL.")
        return

    engine = CrawlEngine(url)
    results, stats = engine.run()

    print("\nCrawl completed.")
    print(f"Pages processed: {stats['urls_processed']}")
    print(f"Pages discovered: {stats['urls_discovered']}")
    print(f"Successful requests: {stats['successful_requests']}")
    print(f"HTTP errors: {stats['http_error_responses']}")
    print(f"Average latency: {stats['average_latency_ms']} ms")
    print(f"Max depth: {stats['max_depth']}")
    print(f"Duration: {stats['duration_seconds']} seconds")
    print("\nResults:")
    print("  output/crawl_results.json")
    print("  output/crawl_results.csv")
    print("  logs/crawler.log")

if __name__ == "__main__":
    main()
