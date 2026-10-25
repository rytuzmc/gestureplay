@echo off
setlocal
cd /d "%~dp0"
where py >nul 2>nul
if not errorlevel 1 goto use_py
where python >nul 2>nul
if errorlevel 1 goto no_python
python server.py --open
goto finish

:use_py
py -3 server.py --open
goto finish

:no_python
echo GesturePlay needs Python 3. Install Python 3, then double-click this launcher again.

:finish
if errorlevel 1 pause
