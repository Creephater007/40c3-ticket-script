curl -L "https://raw.githubusercontent.com/Creephater007/40c3-ticket-script/main/Tickets.py" -o ~/Tickets.py
apt install python-playwright
playwright install chromium
python3 ~/Tickets.py
rm -f ~/Tickets.py
