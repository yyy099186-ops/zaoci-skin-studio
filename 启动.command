#!/bin/bash
# StyleForge 设计工作台 —— Mac 双击启动
# 双击本文件即可启动工具（首次可能需右键→打开，绕过安全提示）

cd "$(dirname "$0")"

# 依次尝试常见的 python3 位置
PY=""
for cand in \
  "python3" \
  "/usr/bin/python3" \
  "/usr/local/bin/python3" \
  "/opt/homebrew/bin/python3" \
  "$HOME/.workbuddy/binaries/python/versions/3.13.12/bin/python3"
do
  if command -v "$cand" >/dev/null 2>&1 || [ -x "$cand" ]; then
    PY="$cand"
    break
  fi
done

if [ -z "$PY" ]; then
  echo "========================================"
  echo "  没找到 Python3。"
  echo "  请先安装 Python3（https://www.python.org/downloads/）"
  echo "  安装后再双击本文件。"
  echo "========================================"
  read -n 1 -s -r -p "按任意键关闭..."
  exit 1
fi

echo "使用 Python: $PY"
"$PY" server.py
