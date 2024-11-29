from pyrogram import Client, filters


API_ID = ""
API_HASH = ""
BOT_TOKEN = ""


LazzyXRename = Client(
    name="renamer", 
    api_id=Config.API_ID,
    api_hash=Config.API_HASH,
    bot_token=Config.BOT_TOKEN
) 

print("Bot Was Started ⚡") 

LazzyXRename.run() 
  
