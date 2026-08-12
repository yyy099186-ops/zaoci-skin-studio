@echo off
chcp 65001 >nul
title StyleForge 设计工作台
cd /d "%~dp0"

set PY=
where python >nul 2>nul && set PY=python
if "%PY%"=="" where py >nul 2>nul && set PY=py

if "%PY%"=="" (
  echo ========================================
  echo   没找到 Python。
  echo   请先安装 Python3（https://www.python.org/downloads/）
  echo   安装时勾选 "Add Python to PATH"，装完再双击本文件。
  echo ========================================
  pause
  exit /b 1
)

echo 使用 Python: %PY%
%PY% server.py
pause
