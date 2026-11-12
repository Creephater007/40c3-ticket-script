curl -L "https://raw.githubusercontent.com/Creephater007/40c3-ticket-script/main/Tickets.py" -o %appdata%\Tickets.py
python3 -m pip install playwright
python3 -m playwright install chromium
python3 %appdata%\Tickets.py
del /f /q %appdata%\Tickets.py