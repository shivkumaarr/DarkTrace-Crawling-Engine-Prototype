import csv
import json
from pathlib import Path

def export_json(results, path):
    Path(path).parent.mkdir(parents=True, exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        json.dump(results, f, indent=2, ensure_ascii=False)

def export_csv(results, path):
    Path(path).parent.mkdir(parents=True, exist_ok=True)
    if not results:
        Path(path).write_text("", encoding="utf-8")
        return

    fields = sorted({key for row in results for key in row.keys()})
    with open(path, "w", encoding="utf-8", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=fields)
        writer.writeheader()
        writer.writerows(results)
