
import argparse
import json
import sys
from datetime import datetime, timezone
from urllib.parse import urlparse

import requests

SECURITY_HEADERS = [
    "Content-Security-Policy",
    "Strict-Transport-Security",
    "X-Content-Type-Options",
    "X-Frame-Options",
    "Referrer-Policy",
    "Permissions-Policy",
]


def validate_url(url):
    parsed = urlparse(url)

    if parsed.scheme not in ("http", "https") or not parsed.hostname:
        raise ValueError("Enter a valid HTTP or HTTPS URL.")

    if parsed.username or parsed.password:
        raise ValueError("URLs containing credentials are not allowed.")

    return url


def scan_website(url):
    validate_url(url)

    try:
        response = requests.get(
            url,
            timeout=10,
            allow_redirects=True,
            headers={"User-Agent": "EducationalSecurityHeaderChecker/1.0"},
        )
    except requests.RequestException as error:
        return {
            "url": url,
            "error": str(error),
            "checked_at": datetime.now(timezone.utc).isoformat(),
        }

    headers = {
        name: response.headers.get(name)
        for name in SECURITY_HEADERS
    }

    missing_headers = [
        name for name, value in headers.items() if not value
    ]

    return {
        "url": url,
        "final_url": response.url,
        "status_code": response.status_code,
        "security_headers": headers,
        "missing_headers": missing_headers,
        "cors": {
            "Access-Control-Allow-Origin":
                response.headers.get("Access-Control-Allow-Origin"),
            "Access-Control-Allow-Credentials":
                response.headers.get("Access-Control-Allow-Credentials"),
            "Access-Control-Allow-Methods":
                response.headers.get("Access-Control-Allow-Methods"),
        },
        "checked_at": datetime.now(timezone.utc).isoformat(),
        "note": (
            "This is a basic header check, not a complete vulnerability scan."
        ),
    }


def main():
    parser = argparse.ArgumentParser(
        description="Basic web security header and CORS checker."
    )
    parser.add_argument("url", help="Website URL to check")
    parser.add_argument("--json", metavar="FILE",
                        help="Save results to a JSON file")
    args = parser.parse_args()

    try:
        result = scan_website(args.url)
    except ValueError as error:
        print(f"Error: {error}", file=sys.stderr)
        return 2

    print(json.dumps(result, indent=4))

    if args.json:
        with open(args.json, "w", encoding="utf-8") as file:
            json.dump(result, file, indent=4)
            file.write("\n")
        print(f"\nReport saved to {args.json}")

    return 1 if "error" in result else 0


if __name__ == "__main__":
    sys.exit(main())
