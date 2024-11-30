import random 
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, ForceReply, CallBackQuery
from helper.database import db
from config import Config, Txt

@Client.on_message(filters.private & filters.command("start"))
async def start(client, message):
    user = message.from_user
    await db.add_user(client, message)                
    button = InlineKeyboardMarkup([[
        InlineKeyboardButton('⚡Updates Channel⚡', url='https://t.me/Lazzy_Bots_Official/')
        ],[
        InlineKeyboardButton("About😎", callback_data='about'), 
        InlineKeyboardButton("⚙️Help", callback_data='help')
        ],[
        InlineKeyboardButton('❤️‍🔥Support Group❤️‍🔥', url='https://t.me/Lazzy_Bots_Support/') 
        ],[
        InlineKeyBoardButton("Admins🧐", callback_data='admins') 
     ]])
    if Config.START_PIC:
        await message.reply_photo(Config.START_PIC, caption=Txt.START_TXT.format(user.mention), reply_markup=button)       
    else:
        await message.reply_text(text=Txt.START_TXT.format(user.mention), reply_markup=button, disable_web_page_preview=True)
@Client.on_callback_query()
async def cb_handler(client, query: CallbackQuery):
    data = query.data 
    if data == "start":
        await query.message.edit_text(
            text=Txt.START_TXT.format(query.from_user.mention),
            disable_web_page_preview=True,
            reply_markup = InlineKeyboardMarkup([[ 
                InlineKeyboardButton('⚡ Updates Channel ⚡', url='https://t.me/Lazzy_Bots_Official/')
                ],[
                InlineKeyboardButton("About 😎", callback_data='about'), 
                InlineKeyboardButton("⚙️ Help", callback_data='help')
                ],[
                InlineKeyboardButton('❤️‍🔥 Support Group ❤️‍🔥', url='https://t.me/Lazzy_Bots_Support/') 
                ],[
                InlineKeyBoardButton("Admins 🧐", callback_data='admins') 
             ]])
        ) 
    elif data == "help":
        await query.message.edit_text(
            text=Txt.HELP_TXT.format, 
            disable_web_page_preview = True,
            reply_markup=InlineKeyboardMarkup([[  
                #⚠️ don't change source code & source link ⚠️ #
                InlineKeyboardButton("❣️ Sᴏᴜʀᴄᴇ Cᴏᴅᴇ", url="https://t.me/Minato_Assist_Bot/")
                ],[
                InlineKeyboardButton("🔒 Cʟᴏꜱᴇ", callback_data = "close"),
                InlineKeyboardButton("⛔ Bᴀᴄᴋ", callback_data = "start")
            ]]) 
        )    
    elif data == "about":
        await query.message.edit_text(
            text=Txt.ABOUT_TXT.format(client.mention),
            disable_web_page_preview = True,
            reply_markup=InlineKeyboardMarkup([[
                #⚠️ don't change source code & source link ⚠️ #
                InlineKeyboardButton("❣️ Sᴏᴜʀᴄᴇ Cᴏᴅᴇ", url="https://t.me/Minato_Assist_Bot/")
                ],[
                InlineKeyboardButton("🔒 Cʟᴏꜱᴇ", callback_data = "close"),
                InlineKeyboardButton("⛔ Bᴀᴄᴋ", callback_data = "start")
            ]])            
        )
    elif data == "admins":
        await query.message.edit_text(
            text=Txt.ABMINS_TXT,
            disable_web_page_preview=True,
            reply_markup=InlineKeyboardMarkup([[
                #⚠️ don't change source code & source link ⚠️ #
                InlineKeyboardButton("❣️ Sᴏᴜʀᴄᴇ Cᴏᴅᴇ", url="https://t.me/Minato_Assist_Bot/")
                ],[
                InlineKeyboardButton("🔒 Cʟᴏꜱᴇ", callback_data = "close"),
                InlineKeyboardButton("⛔ Bᴀᴄᴋ", callback_data = "start")
            ]])          
        ) 
    elif data == "close":
        try:
            await query.message.delete()
            await query.message.reply_to_message.delete()
            await query.message.continue_propagation()
        except:
            await query.message.delete()
            await query.message.continue_propagation()
