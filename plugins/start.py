from datetime import date as date_
import datetime
import os
from pyrogram.errors.exceptions.bad_request_400 import UserNotParticipant
import time
from pyrogram import Client, filters
from pyrogram.types import (
    InlineKeyboardButton, InlineKeyboardMarkup, CallbackQuery)
import humanize
from helper.progress import humanbytes

from helper.database import insert, find_one, used_limit, usertype, uploadlimit, addpredata, total_rename, total_size
from pyrogram.file_id import FileId
from helper.database import daily as daily_
from helper.date import check_expi
from text import Text
import os

CHANNEL = os.environ.get('CHANNEL', "")
STRING = os.environ.get("STRING", "")
ADMIN = int(os.environ.get("ADMIN", 1484670284))
bot_username = os.environ.get("BOT_USERNAME","GangsterBaby_renamer_BOT")
log_channel = int(os.environ.get("LOG_CHANNEL", ""))
token = os.environ.get('TOKEN', '')
botid = token.split(':')[0]
FLOOD = 500
LAZY_PIC = os.environ.get("LAZY_PIC", "")


# Part of Day --------------------
currentTime = datetime.datetime.now()

if currentTime.hour < 12:
    wish = "❤️ Gᴏᴏᴅ Mʀɴɢ Mʏ SᴡᴇᴇᴛHᴇᴀʀᴛ ❤️"
elif 12 <= currentTime.hour < 12:
    wish = '🤍 Gᴏᴏᴅ Aғᴛᴇʀɴᴏᴏɴ Mʏ Lᴏᴠᴇᴇ 🤍'
else:
    wish = '🦋 Gᴏᴏᴅ Eᴠᴇɴɢ Bᴀᴇᴇ 🦋'

# -------------------------------

#help command 
@Client.on_message(filters.private & filters.command(["help"]))

async def start(client,message):

	
        await message.reply_photo(photo=LAZY_PIC,

                                caption=txt,

                                reply_markup=InlineKeyboardMarkup([[

                #⚠️ don't change source code & source link ⚠️ #

                InlineKeyboardButton("❣️ Sᴏᴜʀᴄᴇ Cᴏᴅᴇ", url="https://github.com/TEAM-PYRO-BOTZ/PYRO-RENAME-BOT")

                ],[

                InlineKeyboardButton("❤️‍🔥 Hᴏᴡ Tᴏ Uꜱᴇ❤️‍🔥", url='https://youtu.be/4ZfvMSDXBVg')

                ],[

                InlineKeyboardButton("🔒 Cʟᴏꜱᴇ", callback_data = "close"),

                InlineKeyboardButton("◀️ Bᴀᴄᴋ", callback_data = "start")

            ]])            

        )
	
@Client.on_message(filters.private & filters.command(["start"]))
async def start(client, message):
    old = insert(int(message.chat.id))
    try:
        id = message.text.split(' ')[1]
    except:
        txt=f"""Hᴇʟʟᴏ {wish} {message.from_user.first_name } \n\n
        I Aᴍ Sɪᴍᴘʟᴇ Rᴇɴᴀᴍᴇ Bᴏᴛ Wɪᴛʜ Sᴏᴍᴇ Usᴇғᴜʟ Fᴇᴀᴛᴜʀᴇs Cʜᴄᴋ Oᴜᴛ Hᴇʟᴘ Bᴜᴛᴛᴏɴ Fᴏʀ Mᴏʀᴇ Iɴғᴏʀᴍᴀᴛɪᴏɴ ↓↓"""
        await message.reply_photo(photo=LAZY_PIC,
                                caption=txt,
                                reply_markup = InlineKeyboardMarkup([[
        InlineKeyboardButton("👨‍💻 Aʙᴏᴜᴛ Oᴡɴᴇʀ 💻", callback_data='dev')
        ],[
        InlineKeyboardButton('📯 Uᴩᴅᴀᴛᴇꜱ', url='https://t.me/PeterXClouD'),
        InlineKeyboardButton('💁‍♂️ Sᴜᴩᴩᴏʀᴛ', url='https://t.me/PeterXClouD_Chat')
        ],[
        InlineKeyboardButton('🎛️ Aʙᴏᴜᴛ', callback_data='about'),
        InlineKeyboardButton('🛠️ Hᴇʟᴩ', callback_data='help')
    ]]))
        return
    if id:
        if old == True:
            try:
                await client.send_message(id, "** Lᴏʟ 😂 Yᴏᴜʀ Fʀɪᴇɴᴅ Is Aʟʀᴇᴅʏ Usɪɴɢ Oᴜʀ BᴏT**")
                await message.reply_photo(photo=LAZY_PIC,
                                         caption=txt,
                                         reply_markup = InlineKeyboardMarkup([[
        InlineKeyboardButton("👨‍💻 Aʙᴏᴜᴛ Oᴡɴᴇʀ 💻", callback_data='dev')
        ],[
        InlineKeyboardButton('📯 Uᴩᴅᴀᴛᴇꜱ', url='https://t.me/PeterXClouD'),
        InlineKeyboardButton('💁‍♂️ Sᴜᴩᴩᴏʀᴛ', url='https://t.me/PeterXClouD_Chat')
        ],[
        InlineKeyboardButton('🎛️ Aʙᴏᴜᴛ', callback_data='about'),
        InlineKeyboardButton('🛠️ Hᴇʟᴩ', callback_data='help')
    ]]))
            except:
                return
        else:
            await client.send_message(id, "Congrats! You Won 100MB Upload limit")
            _user_ = find_one(int(id))
            limit = _user_["uploadlimit"]
            new_limit = limit + 104857600
            uploadlimit(int(id), new_limit)
            await message.reply_text(text=f"""Hᴇʟʟᴏ {wish} {message.from_user.first_name } \n\n
        I Aᴍ Sɪᴍᴘʟᴇ Rᴇɴᴀᴍᴇ Bᴏᴛ Wɪᴛʜ Sᴏᴍᴇ Usᴇғᴜʟ Fᴇᴀᴛᴜʀᴇs Cʜᴄᴋ Oᴜᴛ Hᴇʟᴘ Bᴜᴛᴛᴏɴ Fᴏʀ Mᴏʀᴇ Iɴғᴏʀᴍᴀᴛɪᴏɴ ↓↓
	""", reply_to_message_id=message.id,
                                     reply_markup = InlineKeyboardMarkup([[
        InlineKeyboardButton("👨‍💻 Aʙᴏᴜᴛ Oᴡɴᴇʀ 👨‍💻", callback_data='dev')
        ],[
        InlineKeyboardButton('📯 Uᴩᴅᴀᴛᴇꜱ', url='https://t.me/PeterXClouD'),
        InlineKeyboardButton('💁‍♂️ Sᴜᴩᴩᴏʀᴛ', url='https://t.me/PeterXClouD_Chat')
        ],[
        InlineKeyboardButton('🎛️ Aʙᴏᴜᴛ', callback_data='about'),
        InlineKeyboardButton('🛠️ Hᴇʟᴩ', callback_data='help')
    ]]))
    
#callbacks-------------
@Client.on_callback_query()
async def cb_handler(client, query: CallbackQuery):
    data = query.data 
    if data == "start":
        await query.message.edit_text(
            text=Text.START_TXT.format(query.from_user.mention),
            disable_web_page_preview=True,
            reply_markup = InlineKeyboardMarkup([[
                InlineKeyboardButton("👨‍💻 Aʙᴏᴜᴛ Oᴡɴᴇʀ 👨‍💻", callback_data='dev')
                ],[
                InlineKeyboardButton('📯 Uᴩᴅᴀᴛᴇꜱ', url='https://t.me/PYRO_BOTZ'),
                InlineKeyboardButton('💁‍♂️ Sᴜᴩᴩᴏʀᴛ', url='https://t.me/PYRO_BOTZ_CHAT')
                ],[
                InlineKeyboardButton('🎛️ Aʙᴏᴜᴛ', callback_data='about'),
                InlineKeyboardButton('🛠️ Hᴇʟᴩ', callback_data='help')
            ]])
        )
    elif data == "help":
        await query.message.edit_text(
            text=Text.HELP_TXT,
            disable_web_page_preview=True,
            reply_markup=InlineKeyboardMarkup([[
                #⚠️ don't change source code & source link ⚠️ #
                InlineKeyboardButton("❣️ Sᴏᴜʀᴄᴇ Cᴏᴅᴇ", url="https://github.com/TEAM-PYRO-BOTZ/PYRO-RENAME-BOT")
                ],[
                InlineKeyboardButton("❤️‍🔥 Hᴏᴡ Tᴏ Uꜱᴇ❤️‍🔥", url='https://youtu.be/4ZfvMSDXBVg')
                ],[
                InlineKeyboardButton("🔒 Cʟᴏꜱᴇ", callback_data = "close"),
                InlineKeyboardButton("◀️ Bᴀᴄᴋ", callback_data = "start")
            ]])            
        )
    elif data == "about":
        await query.message.edit_text(
            text=Text.ABOUT_TXT.format(client.mention),
            disable_web_page_preview = True,
            reply_markup=InlineKeyboardMarkup([[
                #⚠️ don't change source code & source link ⚠️ #
                InlineKeyboardButton("❣️ Sᴏᴜʀᴄᴇ Cᴏᴅᴇ", url="https://github.com/TEAM-PYRO-BOTZ/PYRO-RENAME-BOT")
                ],[
                InlineKeyboardButton("🖥️ Hᴏᴡ Tᴏ Mᴀᴋᴇ", url="https://youtu.be/GfulqsSnTv4")
                ],[
                InlineKeyboardButton("🔒 Cʟᴏꜱᴇ", callback_data = "close"),
                InlineKeyboardButton("◀️ Bᴀᴄᴋ", callback_data = "start")
            ]])            
        )
    elif data == "dev":
        await query.message.edit_text(
            text=Text.DEV_TXT,
            disable_web_page_preview=True,
            reply_markup=InlineKeyboardMarkup([[
                #⚠️ don't change source code & source link ⚠️ #
                InlineKeyboardButton("❣️ Sᴏᴜʀᴄᴇ Cᴏᴅᴇ", url="https://github.com/TEAM-PYRO-BOTZ/PYRO-RENAME-BOT")
                ],[
                InlineKeyboardButton("🖥️ Hᴏᴡ Tᴏ Mᴀᴋᴇ", url="https://youtu.be/GfulqsSnTv4")
                ],[
                InlineKeyboardButton("🔒 Cʟᴏꜱᴇ", callback_data = "close"),
                InlineKeyboardButton("◀️ Bᴀᴄᴋ", callback_data = "start")
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
				  

@Client.on_message((filters.private & (filters.document | filters.audio | filters.video)) | filters.channel & (filters.document | filters.audio | filters.video))
async def send_doc(client, message):
    update_channel = CHANNEL
    user_id = message.from_user.id
    if update_channel:
        try:
            await client.get_chat_member(update_channel, user_id)
        except UserNotParticipant:
            _newus = find_one(message.from_user.id)
            user = _newus["usertype"]
            await message.reply_text("**Yᴏᴜ Aʀᴇ Nᴏᴛ Sᴜʙsᴄʀɪʙᴇᴅ Mʏ Cʜᴀɴɴᴇʟ Kɪɴᴅʟʏ Sᴜʙsᴄʀɪʙᴇ Mʏ Cʜᴀɴɴᴇʟ Tᴏ Usᴇ Mᴇʜ** ",
                                     reply_to_message_id=message.id,
                                     reply_markup=InlineKeyboardMarkup(
                                         [[InlineKeyboardButton("🔺 Uᴘᴅᴀᴛᴇs Cʜᴀɴɴᴇʟ 🔺", url=f"https://t.me/{update_channel}")]]))
            await client.send_message(log_channel,f"🦋 #GangsterBaby_LOGS 🦋,\n\n**ID** : `{user_id}`\n**Name**: {message.from_user.first_name} {message.from_user.last_name}\n**User-Plan** : {user}\n\n ",
                                                                                                       reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("🔺 Restrict User ( **pm** ) 🔺", callback_data="ceasepower")]]))
            return

    try:
        bot_data = find_one(int(botid))
        prrename = bot_data['total_rename']
        prsize = bot_data['total_size']
        user_deta = find_one(user_id)
    except:
        await message.reply_text(text=f"**Bʀᴜʜ {message.from_user.first_name}**")
    try:
        used_date = user_deta["date"]
        buy_date = user_deta["prexdate"]
        daily = user_deta["daily"]
        user_type = user_deta["usertype"]
    except:
        await message.reply_text(text=f"**Sᴏʀʀʏ Bʀᴜʜ Wᴇ'ʀᴇ Cᴜʀʀᴇɴʟʏ Fᴀᴄɪɴɢ Sᴇᴠᴇʀ Issᴜᴇs Pʟᴇᴀsᴇ Tʀʏ Lᴀᴛᴇʀ ᴏʀ Tʀʏ Iɴ Yᴏᴜʀ Aʟᴛᴇʀɴᴀᴛɪᴠᴇ Tᴇʟᴇɢʀᴀᴍ Iᴅ**")
        return 

    c_time = time.time()

	
	
	
	
	
	
    if user_type == "Free":
        LIMIT = 600
    else:
        LIMIT = 50
    then = used_date + LIMIT
    left = round(then - c_time)
    conversion = datetime.timedelta(seconds=left)
    ltime = str(conversion)
    if left > 0:
        await message.reply_text(f"**Sorry Bruh I Am Not only For You \n Flood Control Is Active So Please Wait Untill <u>{ltime}</u>**", reply_to_message_id=message.id)
    else:
        # Forward a single message
        media = await client.get_messages(message.chat.id, message.id)
        file = media.document or media.video or media.audio
        dcid = FileId.decode(file.file_id).dc_id
        filename = file.file_name
        value = 2147483648
        used_ = find_one(message.from_user.id)
        used = used_["used_limit"]
        limit = used_["uploadlimit"]
        expi = daily - int(time.mktime(time.strptime(str(date_.today()), '%Y-%m-%d')))
        if expi != 0:
            today = date_.today()
            pattern = '%Y-%m-%d'
            epcho = int(time.mktime(time.strptime(str(today), pattern)))
            daily_(message.from_user.id, epcho)
            used_limit(message.from_user.id, 0)
        remain = limit - used
        if remain < int(file.file_size):
            await message.reply_text(f"**100%  Dᴀɪʟʏ <u>{humanbytes(limit)}</u> Dᴀᴛᴀ Qᴜᴏᴛᴀ Exʜᴀᴜsᴛᴇᴅ.\n\nFɪʟᴇ Sɪᴢᴇ Dᴇᴛᴇᴄᴛᴇᴅ <u>{humanbytes(file.file_size)}</u>\nUsᴇᴅ Dᴀɪʟʏ Lɪᴍɪᴛ <u>{humanbytes(used)}</u>\nYᴏᴜ ʜᴀᴠᴇ ᴏɴʟʏ <u>{humanbytes(remain)}</u>Lᴇғᴛ Oɴ Yᴏᴜʀ Aᴄᴄᴏᴜɴᴛ.\n\nIғ U Wᴀɴᴛ Tᴏ Rᴇɴᴀᴍᴇ Lᴀʀɢᴇ Fɪʟᴇ Uᴘɢʀᴀᴅᴇ Yᴏᴜʀ Pʟᴀɴ Nᴏᴡ **", reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("Uᴘɢʀᴀᴅᴇ 💰💳", callback_data="upgrade")]]))
            return
        if value < file.file_size:
            
            if STRING:
                if buy_date == None:
                    await message.reply_text(f" **Yᴏᴜ Cᴀɴ'ᴛ Uᴘʟᴏᴀᴅ Mᴏʀᴇ Tʜᴇɴ <u>{humanbytes(limit)} </u> Usᴇᴅ Dᴀɪʟʏ Lɪᴍɪᴛ<u>{humanbytes(used)}</u> **", reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("Uᴘɢʀᴀᴅᴇ 💰💳", callback_data="upgrade")]]))
                    return
                pre_check = check_expi(buy_date)
                if pre_check == True:
                    await message.reply_text(f"""**What Do You Want Me To Do With This File?!**\n**File Name** : {filename}\n**File Size** :- {humanize.naturalsize(file.file_size)}\n**Dc ID** :- {dcid}""", reply_to_message_id=message.id, reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("📝 Rename", callback_data="rename"), InlineKeyboardButton("✖️ Cancel", callback_data="cancel")]]))
                    total_rename(int(botid), prrename)
                    total_size(int(botid), prsize, file.file_size)
                else:
                    uploadlimit(message.from_user.id, 1288490188)
                    usertype(message.from_user.id, "Free")

                    await message.reply_text(f'Your Plan Expired On {buy_date}', quote=True)
                    return
            else:
                await message.reply_text("Can't upload files bigger than 2GB ")
                return
        else:
            if buy_date:
                pre_check = check_expi(buy_date)
                if pre_check == False:
                    uploadlimit(message.from_user.id, 1288490188)
                    usertype(message.from_user.id, "Free")

            filesize = humanize.naturalsize(file.file_size)
            fileid = file.file_id
            total_rename(int(botid), prrename)
            total_size(int(botid), prsize, file.file_size)
            await message.reply_text(f"""__What do you want me to do with this file?__\n**File Name** :- {filename}\n**File Size** :- {filesize}\n**Dc ID** :- {dcid}""", reply_to_message_id=message.id, reply_markup=InlineKeyboardMarkup(
                [[InlineKeyboardButton("📝 Rename", callback_data="rename"),
                  InlineKeyboardButton("✖️ Cancel", callback_data="cancel")]]))
