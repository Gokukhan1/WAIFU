import os
from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from telegram import Update
from telegram.ext import CallbackContext, CallbackQueryHandler
from telegram.ext import MessageHandler, filters
from telegram.ext import CommandHandler
from ROYEDITX import application 
from ROYEDITX import db, LOGGER_ID, OWNER_ID 
from ROYEDITX import IMG_URL, SUPPORT_CHAT, UPDATE_CHAT, BOT_USERNAME
import random

#####
AVISHA = [
"https://telegra.ph/file/262a5dd6406c4ee26bc63.jpg",
"https://telegra.ph/file/3515a6d10677b2dda6e3e.jpg",
"https://telegra.ph/file/039af07c725ba814a6d48.jpg",
]

####

collection = db['total_pm_users']


async def start(update: Update, context: CallbackContext) -> None:
    user_id = update.effective_user.id
    first_name = update.effective_user.first_name
    username = update.effective_user.username

    user_data = await collection.find_one({"_id": user_id})

    if user_data is None:
        
        await collection.insert_one({"_id": user_id, "first_name": first_name, "username": username})
        
        await context.bot.send_message(chat_id=LOGGER_ID, text=f"❖ <a href='tg://user?id={user_id}'>{first_name}</a> sᴛᴀʀᴛᴇᴅ ᴛʜᴇ ʙᴏᴛ", parse_mode='HTML')
    else:
        
        if user_data['first_name'] != first_name or user_data['username'] != username:
            
            await collection.update_one({"_id": user_id}, {"$set": {"first_name": first_name, "username": username}})

    

    if update.effective_chat.type== "private":
        
        
        caption = f"""
        ***❖ ʜᴇʏ {update.effective_user.first_name}, ᴡᴇʟᴄᴏᴍᴇ ʙᴀʙʏ ♥︎\n━━━━━━━━━━━━━━━━━━━━━━━━━━━━***
              
***● ɪ ᴀᴍ 『GOKU』x³『ᴀɴɪᴍᴇ』♡゙ ᴀɴᴅ ɪ ʜᴀᴠᴇ sᴘᴇᴄɪᴀʟ ғᴇᴀᴛᴜʀᴇs.\n\n● ᴀɴɪᴍᴇ ᴠᴇʀsɪᴏɴ ➥ M33.6/V16 \n● ᴘʏᴛʜᴏɴ ᴠᴇʀsɪᴏɴ ➥ 3.11.9 \n\n❖ ᴛʜɪs ɪs ᴍᴏsᴛ ᴘᴏᴡᴇʀғᴜʟʟ ᴀɴɪᴍᴇ ᴄʜᴀʀᴀᴄᴛᴇʀ ᴄᴏʟʟᴇᴄᴛ ʜᴀʀᴇᴍ ʙᴏᴛ.***
               """
        keyboard = [
            [InlineKeyboardButton("ᴀᴅᴅ ᴍᴇ ʙᴀʙʏ", url=f'http://t.me/GOKU_ANIME_HASBANDO_REBOT?startgroup=new')],
            [InlineKeyboardButton("Xeno_Kakarot", url=f'https://t.me/Xeno_Kakarot'),
             InlineKeyboardButton("sᴜᴘᴘᴏʀᴛ", url=f'https://t.me/lolpagalokigc')],
            [InlineKeyboardButton("ʜᴇʟᴘ ᴄᴏᴍᴍᴀɴᴅs", callback_data='help'),
             InlineKeyboardButton("creater", url=f'https://t.me/The_saiyans_prince')],
             [InlineKeyboardButton("repo",url=f'https://youtu.be/j_nJPCgxYS4?si=OT2IRBoExdbPqkJF')],
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)
        photo_url = random.choice(AVISHA)

        await context.bot.send_photo(chat_id=update.effective_chat.id, photo=photo_url, caption=caption, reply_markup=reply_markup, parse_mode='markdown')

    else:
        photo_url = random.choice(AVISHA)
        keyboard = [
            
            [InlineKeyboardButton("ʜᴇʟᴘ", callback_data='help'),
             InlineKeyboardButton("sᴜᴘᴘᴏʀᴛ", url=f'https://t.me/{SUPPORT_CHAT}')],
            
        ]
        
        reply_markup = InlineKeyboardMarkup(keyboard)
        await context.bot.send_photo(chat_id=update.effective_chat.id, photo=photo_url, caption="❖ ɪ ᴀᴍ ᴀʟɪᴠᴇ ʙᴀʙʏ !",reply_markup=reply_markup )

async def button(update: Update, context: CallbackContext) -> None:
    query = update.callback_query
    await query.answer()

    if query.data == 'help':
        help_text = """
    ***❖ ʜᴇʟᴘ ᴄᴏᴍᴍᴀɴᴅs sᴇᴄᴛɪᴏɴ ❖***
    
***⬤ /guess ➥ ᴛᴏ ɢᴜᴇss ᴄʜᴀʀᴀᴄᴛᴇʀ (ᴏɴʟʏ ᴡᴏʀᴋs ɪɴ ɢʀᴏᴜᴘ).***
***⬤ /fav ➥ ᴀᴅᴅ ʏᴏᴜʀ ғᴀᴠʀᴀᴛᴇ.***
***⬤ /trade ➥ ᴛᴏ ᴛʀᴀᴅᴇ ᴄʜᴀʀᴀᴄᴛᴇʀs.***
***⬤ /gift ➥ ɢɪᴠᴇ ᴀɴʏ ᴄʜᴀʀᴀᴄᴛᴇʀ ғʀᴏᴍ ʏᴏᴜʀ ᴄᴏʟʟᴇᴄᴛɪᴏɴ ᴛᴏ ᴀɴᴏᴛʜᴇʀ ᴜsᴇʀ (ᴏɴʟʏ ᴡᴏʀᴋs ɪɴ ɢʀᴏᴜᴘs).***
***⬤ /collection ➥ ᴛᴏ sᴇᴇ ʏᴏᴜʀ ᴄᴏʟʟᴇᴄᴛɪᴏɴ.***
***⬤ /topgroups ➥ sᴇᴇ ᴛᴏᴘ ɢʀᴏᴜᴘs, ᴘᴘʟ ɢᴜᴇssᴇs ᴍᴏsᴛ ɪɴ ᴛʜᴀᴛ ɢʀᴏᴜᴘs.***
***⬤ /top ➥ ᴛᴏᴏ sᴇᴇ ᴛᴏᴘ ᴜsᴇʀs.***
***⬤ /ctop ➥ ʏᴏᴜʀ ᴄʜᴀᴛ ᴛᴏᴘ.***
***⬤ /changetime ➥ ᴄʜᴀɴɢᴇ ᴄʜᴀʀᴀᴄᴛᴇʀ ᴀᴘᴘᴇᴀʀ ᴛɪᴍᴇ (ᴏɴʟʏ ᴡᴏʀᴋs ɪɴ ɢʀᴏᴜᴘs).***
   """
        help_keyboard = [[InlineKeyboardButton("ʙᴀᴄᴋ", callback_data='back')]]
        reply_markup = InlineKeyboardMarkup(help_keyboard)
        
        await context.bot.edit_message_caption(chat_id=update.effective_chat.id, message_id=query.message.message_id, caption=help_text, reply_markup=reply_markup, parse_mode='markdown')

    elif query.data == 'back':

        caption = f"""
        ***❖ ʜᴇʏ {update.effective_user.first_name}, ᴡᴇʟᴄᴏᴍᴇ ʙᴀʙʏ ♥︎\n━━━━━━━━━━━━━━━━━━━━━━━━━━━━***
              
***● ɪ ᴀᴍ 『GOKU』x³『ᴀɴɪᴍᴇ』♡゙  ᴀɴᴅ ɪ ʜᴀᴠᴇ sᴘᴇᴄɪᴀʟ ғᴇᴀᴛᴜʀᴇs.\n\n● ᴀɴɪᴍᴇ ᴠᴇʀsɪᴏɴ ➥ M33.6/V16\n● ᴘʏᴛʜᴏɴ ᴠᴇʀsɪᴏɴ ➥ 3.11.9\n\n❖ ᴛʜɪs ɪs ᴍᴏsᴛ ᴘᴏᴡᴇʀғᴜʟʟ ᴀɴɪᴍᴇ ᴄʜᴀʀᴀᴄᴛᴇʀ ᴄᴏʟʟᴇᴄᴛ ʜᴀʀᴇᴍ ʙᴏᴛ.***
               """
        keyboard = [
            [InlineKeyboardButton("ᴀᴅᴅ ᴍᴇ ʙᴀʙʏ", url=f'http://t.me/{BOT_USERNAME}?startgroup=new')],
            [InlineKeyboardButton("Xeno_Kakarot", url=f'https://t.me/Xeno_Kakarot'),
             InlineKeyboardButton("sᴜᴘᴘᴏʀᴛ", url=f'https://t.me/{SUPPORT_CHAT}')],
            [InlineKeyboardButton("ʜᴇʟᴘ ᴄᴏᴍᴍᴀɴᴅs", callback_data='help'),
             InlineKeyboardButton("creater", url=f'https://t.me/The_saiyans_prince')],
            [InlineKeyboardButton("repo", url=f'https://youtu.be/j_nJPCgxYS4?si=OT2IRBoExdbPqkJF')],
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)
        
        await context.bot.edit_message_caption(chat_id=update.effective_chat.id, message_id=query.message.message_id, caption=caption, reply_markup=reply_markup, parse_mode='markdown')

application.add_handler(CallbackQueryHandler(button, pattern='^help$|^back$', block=False))
start_handler = CommandHandler('start', start, block=False)
application.add_handler(start_handler)
      
