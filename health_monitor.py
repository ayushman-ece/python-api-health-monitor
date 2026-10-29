import csv
import time
from datetime import datetime, timezone
from pathlib import Path
from urllib.parse import urlparse

import requests

REPORT_FILE = Path(__file__).with_name("health_report.csv")
TIMEOUT_SECONDS = 10


def validate_url(url):
    url = url.strip()

    if "://" not in url:
        url = "https://" + url

    parsed = urlparse(url)

    if parsed.scheme not in ("http", "https") or not parsed.netloc:
        raise ValueError("Enter a valid HTTP or HTTPS URL.")

    return url


def check_endpoint(url):
    url = validate_url(url)
    checked_at = datetime.now(timezone.utc).isoformat()
    start = time.perf_counter()

    try:
        response = requests.get(
            url,
            timeout=TIMEOUT_SECONDS,
            allow_redirects=True,
            headers={"User-Agent": "Python-API-Health-Monitor/1.0"},
        )

        elapsed_ms = round((time.perf_counter() - start) * 1000, 2)

        return {
            "checked_at": checked_at,
            "url": url,
            "status_code": response.status_code,
            "response_ms": elapsed_ms,
            "result": "UP" if response.ok else "HTTP_ERROR",
            "error": "",
        }

    except requests.RequestException as error:
        elapsed_ms = round((time.perf_counter() - start) * 1000, 2)

        return {
            "checked_at": checked_at,
            "url": url,
            "status_code": "",
            "response_ms": elapsed_ms,
            "result": "DOWN",
            "error": str(error),
        }


def save_report(record):
    fields = [
        "checked_at",
        "url",
        "status_code",
        "response_ms",
        "result",
        "error",
    ]

    file_exists = REPORT_FILE.exists() and REPORT_FILE.stat().st_size > 0

    with REPORT_FILE.open("a", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=fields)

        if not file_exists:
            writer.writeheader()

        writer.writerow(record)


def get_recent_reports(limit=10):
    if not REPORT_FILE.exists():
        return []

    with REPORT_FILE.open("r", newline="", encoding="utf-8") as file:
        return list(csv.DictReader(file))[-limit:]