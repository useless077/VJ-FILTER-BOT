# Don't Remove Credit @tamilBots
# Subscribe YouTube Channel For Amazing Bot @TamilBots
# Ask Doubt on telegram @TamilSupport

if [ -z $UPSTREAM_REPO ]
then
  echo "Cloning main Repository"
  git clone https://github.com/VJBots/VJ-FILTER-BOT.git /VJ-FILTER-BOT 
else
  echo "Cloning Custom Repo from $UPSTREAM_REPO "
  git clone $UPSTREAM_REPO /VJ-FILTER-BOT 
fi
cd /VJ-FILTER-BOT 
pip3 install -U -r requirements.txt
echo "Starting Bot...."
python3 bot.py
