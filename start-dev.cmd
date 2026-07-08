@echo off
setlocal

cd /d "%~dp0"

echo Starting Django backend on http://127.0.0.1:8010 ...
start "Django Backend" cmd /k "cd /d \"%~dp0\" && \"%~dp0venv\Scripts\python.exe\" manage.py migrate && \"%~dp0venv\Scripts\python.exe\" manage.py runserver 127.0.0.1:8010"

echo Starting Vue frontend on http://127.0.0.1:5173 ...
start "Vue Frontend" cmd /k "cd /d \"%~dp0frontend\" && npm run dev -- --host 127.0.0.1"

echo.
echo Dev environment is launching in two new terminals.
echo Backend:  http://127.0.0.1:8010
echo Frontend: http://127.0.0.1:5173
