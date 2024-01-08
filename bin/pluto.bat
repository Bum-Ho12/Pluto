@echo off

REM Get the directory of the pluto.bat script
set "SCRIPT_DIR=%~dp0"

REM Try to locate pluto.py in the current or parent directories
set "PLUTO_PY_PATH="
set "CURRENT_DIR=%CD%"
:SEARCH_PLUTO
if exist "%CURRENT_DIR%\pluto.py" (
    set "PLUTO_PY_PATH=%CURRENT_DIR%\pluto.py"
) else (
    set "CURRENT_DIR=%CURRENT_DIR:~0,-1%"
    if not "%CURRENT_DIR%" == "" goto SEARCH_PLUTO
)

REM If pluto.py is found, run it with the provided arguments
if not "%PLUTO_PY_PATH%" == "" (
    python "%PLUTO_PY_PATH%" %*
) else (
    echo "No pluto.py file found in this project or its parent directories."
)
