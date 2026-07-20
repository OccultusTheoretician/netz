#!/usr/bin/env python3
"""Local test: serves fake RSS feeds + a mock LM Studio API, runs netz.py against them."""
import json
import subprocess
import sys
import threading
from datetime import datetime, timedelta, timezone
from http.server import BaseHTTPRequestHandler, HTTPServer

NOW = datetime.now(timezone.utc)


def rfc822(dt):
    return dt.strftime("%a, %d %b %Y %H:%M:%S +0000")


def rss(title, items):
    body = "".join(
        f"<item><title>{t}</title><link>{l}</link>"
        f"<description>{d}</description><pubDate>{rfc822(w)}</pubDate></item>"
        for t, l, d, w in items)
    return (f'<?xml version="1.0"?><rss version="2.0"><channel>'
            f"<title>{title}</title>{body}</channel></rss>").encode()


FEEDS = {
    "/mil_a": rss("Mil A", [
        ("Strait of Hormuz transit disrupted as naval escorts deployed",
         "http://x.test/a1?utm_source=t", "Escorts deployed after seizure incident.", NOW - timedelta(hours=2)),
        ("Ceasefire talks stall in third round", "http://x.test/a2", "Talks stall.", NOW - timedelta(hours=5)),
        ("Old story outside window", "http://x.test/a3", "Stale.", NOW - timedelta(hours=60)),
    ]),
    "/mil_b": rss("Mil B", [
        ("Naval escorts deployed as Hormuz strait transit disrupted",
         "http://y.test/b1", "Corroborating account of the escort deployment.", NOW - timedelta(hours=1)),
        ("Border shelling reported in northern sector", "http://y.test/b2", "Shelling.", NOW - timedelta(hours=3)),
    ]),
    "/econ_a": rss("Econ A", [
        ("Oil futures spike on Strait of Hormuz disruption fears",
         "http://z.test/c1", "Brent jumps as Hormuz risk priced in.", NOW - timedelta(hours=1)),
        ("Central bank holds rates steady", "http://z.test/c2", "Rates held.", NOW - timedelta(hours=8)),
    ]),
    "/cyber_a": rss("Cyber A", [
        ("Ransomware wave hits port logistics operators",
         "http://w.test/d1", "Port systems encrypted at two terminals.", NOW - timedelta(hours=4)),
    ]),
}

MOCK_SYNTH = ("Naval escorts were deployed after transit through the Strait of Hormuz "
              "was disrupted [1]. Ceasefire talks stalled in a third round [2]. "
              "This sentence has no citation on purpose.")


class Handler(BaseHTTPRequestHandler):
    def log_message(self, *a):
        pass

    def do_GET(self):
        if self.path in FEEDS:
            self.send_response(200)
            self.send_header("Content-Type", "application/rss+xml")
            self.end_headers()
            self.wfile.write(FEEDS[self.path])
        elif self.path == "/v1/models":
            self._json({"data": [{"id": "mock-qwen2.5-14b-instruct"}]})
        elif self.path == "/dead":
            self.send_response(500)
            self.end_headers()
        else:
            self.send_response(404)
            self.end_headers()

    def do_POST(self):
        if self.path == "/v1/chat/completions":
            length = int(self.headers.get("Content-Length", 0))
            _ = self.rfile.read(length)
            self._json({"choices": [{"message": {"content": MOCK_SYNTH}}]})
        else:
            self.send_response(404)
            self.end_headers()

    def _json(self, obj):
        data = json.dumps(obj).encode()
        self.send_response(200)
        self.send_header("Content-Type", "application/json")
        self.end_headers()
        self.wfile.write(data)


def main():
    srv = HTTPServer(("127.0.0.1", 8931), Handler)
    threading.Thread(target=srv.serve_forever, daemon=True).start()
    base = "http://127.0.0.1:8931"

    config = {
        "window_hours": 24,
        "output_dir": "test_reports",
        "lmstudio_base_url": f"{base}/v1",
        "categories": {
            "military_conflict": {"Mil A": f"{base}/mil_a", "Mil B": f"{base}/mil_b",
                                  "Dead Feed": f"{base}/dead"},
            "economic": {"Econ A": f"{base}/econ_a"},
            "cyber": {"Cyber A": f"{base}/cyber_a"},
        },
    }
    with open("test_config.json", "w") as f:
        json.dump(config, f)

    r = subprocess.run([sys.executable, "netz.py", "--config", "test_config.json"],
                       capture_output=True, text=True)
    print(r.stderr)
    if r.returncode != 0:
        print("FAIL:", r.stdout, r.stderr)
        sys.exit(1)
    path = r.stdout.strip().splitlines()[-1]
    report = open(path).read()
    print("=" * 70)
    print(report)
    print("=" * 70)

    checks = {
        "Hormuz story clustered 2x": "2× corroborated" in report,
        "utm stripped": "utm_source" not in report,
        "stale item excluded": "Old story outside window" not in report,
        "dead feed surfaced": "fetch_fail" in report,
        "convergence fired (Hormuz mil+econ)": "CONVERGENCE" in report and "Hormuz" in report.split("CONVERGENCE")[1].split("##")[0],
        "synthesis present": "mock-qwen2.5-14b-instruct" in report,
        "uncited sentence flagged": "no citation" in report or "carry no citation" in report,
        "single-source flag": "single-source" in report,
    }
    ok = True
    for name, passed in checks.items():
        print(("PASS " if passed else "FAIL ") + name)
        ok = ok and passed
    sys.exit(0 if ok else 2)


if __name__ == "__main__":
    main()
