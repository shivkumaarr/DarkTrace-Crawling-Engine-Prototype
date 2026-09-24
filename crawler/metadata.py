from datetime import datetime, timezone

def build_metadata(
    url,
    title,
    status_code,
    content_type,
    content_length,
    depth,
    latency_ms,
    links_found,
    error=None,
):
    item = {
        "url": url,
        "title": title,
        "status_code": status_code,
        "content_type": content_type,
        "content_length": content_length,
        "depth": depth,
        "latency_ms": latency_ms,
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "links_found": links_found,
    }
    if error:
        item["error"] = error
    return item
