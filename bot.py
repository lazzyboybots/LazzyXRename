from pyrogram import Client, filters


API_ID = ""
API_HASH = ""
BOT_TOKEN = ""
ADMIN = ""
DATABASE_URI = ""
DATABASE_NAME = ""
FORCE_SUB = ""
LOG_CHANNEL = ""
START_PIC = ""

LazzyXRename = Client(
    name="LazzyXRename", 
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN,
    admin=ADMIN, 
    database_uri=DATABASE_URI, 
    database_name=DATABASE_NAME, 
    force_sub=FORCE_SUB, 
    log_channel=LOG_CHANNEL, 
    start_pic=START_PIC
) 


print("Bot Was Started ⚡") 

LazzyXRename.run() 
  
