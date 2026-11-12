curl -L "https://raw.githubusercontent.com/Creephater007/40c3-ticket-script/main/Tickets.py" -o ~/Tickets.py
python3 -m pip install playwright
python3 -m playwright install chromium
python3 ~/Tickets.py
del /f /q ~/Tickets.py