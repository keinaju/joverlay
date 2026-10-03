@echo off
cd /d "%~dp0"
uv run app.py
if errorlevel 1 pause