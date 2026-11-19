curl -L "https://raw.githubusercontent.com/Creephater007/40c3-ticket-script/main/testing.py" -o ~/Tickets.py;
python3 -m pip install playwright;
if [ $? -ne 0 ]; then
    echo "playwright installation failed! Fallback to flag --break-system-packages";
    python3 -m pip install playwright --break-system-packages;
fi
if [ $? -ne 0 ]; then
    echo "playwright installation failed with flag. Please read the script and adapt it for your OS installation.";
    echo "Exiting with flag 1 ...";
    exit 1;
fi
python3 -m playwright install chromium;
if [ $? -ne 0 ]; then
    echo "Could not install chromium using playwright python module.";
    echo "Exiting with flag 1 ...";
    exit 1;
fi

echo "\n\nDependencies collected. Starting script ...";

python3 ~/Tickets.py;
rm -f ~/Tickets.py;
