echo "Cloning Repo...."
git clone https://github.com/mdisklink/mdisklink.git /mdisklink
cd /mdisklink
pip3 install -r requirements.txt
echo "Starting Bot...."
python3 bot.py
