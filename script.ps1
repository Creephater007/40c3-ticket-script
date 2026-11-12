$ticketScript = Join-Path $env:APPDATA "Tickets.py"

curl.exe -L "https://raw.githubusercontent.com/Creephater007/40c3-ticket-script/main/Tickets.py" -o $ticketScript
python3 -m pip install playwright
python3 -m playwright install chromium
python3 $ticketScript
Remove-Item -Force $ticketScript -ErrorAction SilentlyContinue