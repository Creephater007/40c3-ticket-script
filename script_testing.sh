curl -L "https://raw.githubusercontent.com/Creephater007/40c3-ticket-script/main/testing.py" -o ~/Tickets.py
sudo apt install python3-playwright
sudo playwright install chromium
python3 ~/Tickets.py
rm -f ~/Tickets.py
