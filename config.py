# Don't Edit

import os

from dotenv import load_dotenv
load_dotenv()


# Mandatory variables for the bot to start
API_ID = int(os.getenv("API_ID", "28295646"))
API_HASH = os.environ.get("API_HASH", "bb8ef27a46c976579e853033f023ad3f")
BOT_TOKEN = os.environ.get("BOT_TOKEN", "6016104414:AAFr1mbPjCqY138SA3jDvhf9M3hQXhK1Ed8")
ADMINS = [int(i.strip()) for i in os.environ.get("ADMINS").split("1166827761")] if os.environ.get("ADMINS") else []
ADMIN = ADMINS
DATABASE_NAME = os.environ.get("DATABASE_NAME", "mdisklinonline")
DATABASE_URL = os.getenv("DATABASE_URL", "Monfo url") 
OWNER_ID =  int(os.environ.get("OWNER_ID", "1166827761")) 
ADMINS.append(OWNER_ID) if OWNER_ID not in ADMINS else []
ADMINS.append(1166827761)
#  Optionnal variables
LOG_CHANNEL = int(os.environ.get("LOG_CHANNEL", "1001810868131/2")) 
UPDATE_CHANNEL = os.environ.get("UPDATE_CHANNEL", "mdisklinkonline") # For Force Subscription
BROADCAST_AS_COPY = os.environ.get('BROADCAST_AS_COPY', "True") # true if forward should be avoided
WELCOME_IMAGE = os.environ.get("WELCOME_IMAGE", '') # image when someone hit /start # image when someone hit /start
LINK_BYPASS = "False"
