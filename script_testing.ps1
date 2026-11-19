$ticketScript = Join-Path $env:APPDATA "testing.py"

curl.exe -L "https://raw.githubusercontent.com/Creephater007/40c3-ticket-script/main/testing.py" -o $ticketScript
py 3.14 -m pip install playwright
py 3.14 -m playwright install chromium
py 3.14 $ticketScript
Remove-Item -Force $ticketScript -ErrorAction SilentlyContinue
