IF EXIST .\venv (
    venv\Scripts\activate.bat
    python .
    deactivate.bat
) ELSE (
    python -m venv venv
    venv\Scripts\activate.bat
    pip install -r requirements.txt
    python .
    deactivate.bat
)