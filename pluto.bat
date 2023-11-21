@echo off

:: Activate your virtual environment (replace venv\Scripts\activate with the path to your activate script)
pluto_env\Scripts\activate

:: Run your Pluto project (replace main.py with the actual file)
python runner.py

:: Deactivate the virtual environment
deactivate
