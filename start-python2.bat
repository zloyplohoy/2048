IF EXIST .\venv (
    venv\Scripts\activate.bat
    python .
    deactivate.bat
) ELSE (
    pip install virtualenv
    python -m virtualenv venv
    venv\Scripts\activate.bat
    pip install -r requirements.txt
    python .
    deactivate.bat
)