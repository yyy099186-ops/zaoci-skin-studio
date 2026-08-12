#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
StyleForge 本地工作台后端
零第三方依赖，仅用 Python 标准库。
职责：
  1. 托管静态前端（index.html / skills / outputs）
  2. POST /api/save-job   —— 工具点生成后，把出图任务存到 jobs/latest.json
  3. GET  /api/outputs    —— 返回 outputs/manifest.json，供前端轮询自动回填
  4. GET  /api/job-status —— 告诉前端当前是否有待处理任务
"""
import json
import os
import sys
import webbrowser
import threading
import time
from http.server import HTTPServer, SimpleHTTPRequestHandler
from urllib.parse import urlparse

ROOT = os.path.dirname(os.path.abspath(__file__))
PORT = 8799
JOBS_DIR = os.path.join(ROOT, "jobs")
OUTPUTS_DIR = os.path.join(ROOT, "outputs")
os.makedirs(JOBS_DIR, exist_ok=True)
os.makedirs(OUTPUTS_DIR, exist_ok=True)


class Handler(SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=ROOT, **kwargs)

    def log_message(self, fmt, *args):
        pass

    def _json(self, obj, code=200):
        body = json.dumps(obj, ensure_ascii=False).encode("utf-8")
        self.send_response(code)
        self.send_header("Content-Type", "application/json; charset=utf-8")
        self.send_header("Content-Length", str(len(body)))
        self.send_header("Cache-Control", "no-store")
        self.end_headers()
        self.wfile.write(body)

    def do_GET(self):
        path = urlparse(self.path).path
        if path == "/api/outputs":
            mf = os.path.join(OUTPUTS_DIR, "manifest.json")
            if os.path.exists(mf):
                try:
                    with open(mf, "r", encoding="utf-8") as f:
                        return self._json(json.load(f))
                except Exception as e:
                    return self._json({"error": str(e)}, 500)
            return self._json({"cells": {}})
        if path == "/api/job-status":
            jf = os.path.join(JOBS_DIR, "latest.json")
            if os.path.exists(jf):
                try:
                    with open(jf, "r", encoding="utf-8") as f:
                        j = json.load(f)
                    return self._json({"pending": True, "style": j.get("style_name", ""),
                                       "cells": len(j.get("cells", []))})
                except Exception:
                    pass
            return self._json({"pending": False})
        return super().do_GET()

    def do_POST(self):
        path = urlparse(self.path).path
        if path == "/api/save-job":
            length = int(self.headers.get("Content-Length", 0))
            raw = self.rfile.read(length)
            try:
                job = json.loads(raw.decode("utf-8"))
            except Exception as e:
                return self._json({"ok": False, "error": "bad json: " + str(e)}, 400)
            job["_saved_at"] = time.strftime("%Y-%m-%d %H:%M:%S")
            with open(os.path.join(JOBS_DIR, "latest.json"), "w", encoding="utf-8") as f:
                json.dump(job, f, ensure_ascii=False, indent=2)
            stamp = time.strftime("%Y%m%d-%H%M%S")
            with open(os.path.join(JOBS_DIR, "job-%s.json" % stamp), "w", encoding="utf-8") as f:
                json.dump(job, f, ensure_ascii=False, indent=2)
            return self._json({"ok": True, "saved": "jobs/latest.json"})
        return self._json({"ok": False, "error": "unknown endpoint"}, 404)


def open_browser():
    time.sleep(1.0)
    webbrowser.open("http://localhost:%d/index.html" % PORT)


def main():
    try:
        httpd = HTTPServer(("127.0.0.1", PORT), Handler)
    except OSError as e:
        print("=" * 52)
        print("  端口 %d 被占用，可能工具已经在运行。" % PORT)
        print("  请先关掉旧窗口，或直接打开：")
        print("  http://localhost:%d/index.html" % PORT)
        print("=" * 52)
        sys.exit(1)
    threading.Thread(target=open_browser, daemon=True).start()
    print("=" * 52)
    print("  StyleForge 设计工作台已启动")
    print("  浏览器地址： http://localhost:%d/index.html" % PORT)
    print("  关闭工具：直接关掉这个窗口即可")
    print("=" * 52)
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("\n已关闭。")


if __name__ == "__main__":
    main()
