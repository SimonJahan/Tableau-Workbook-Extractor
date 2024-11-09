@echo off

set WORK_DIR=%~dp0
cd /d "%WORK_DIR%"
set PYTHON_SCRIPT="./utils/main.py"

if [%1]==[] (
    python "%PYTHON_SCRIPT%"
    exit
)
else (
    python "%PYTHON_SCRIPT%" "%~1"
    exit
)