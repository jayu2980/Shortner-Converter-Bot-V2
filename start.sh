echo "Cloning Repo...."
git clone https://github.com/mdisklink/mdisklinkonline-Converter-Bot.git /mdisklinkonline-Converter-Bot
cd /mdisklinkonline-Converter-Bot
pip3 install -r requirements.txt
echo "Starting Bot...."
python3 bot.py
