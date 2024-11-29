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
    api_id=Config.API_ID,
    api_hash=Config.API_HASH,
    bot_token=Config.BOT_TOKEN,
    admin=Config.ADMIN, 
    database_uri=Config.DATABASE_URI, 
    database_name=Config.DATABASE_NAME, 
    force_sub=Config.FORCE_SUB, 
    log_channel=Config.LOG_CHANNEL, 
    start_pic=Config.START_PIC
) 

print("Bot Was Started ⚡") 

LazzyXRename.run() 
  
