import pyrogram, asyncio, random, time, os
from pyrogram import Client, filters, enums
from pyrogram.types import *
from helper.database import adds_user, db
from info import *
from helper.text import txt
from plugins.fsub import get_fsub

@Client.on_message(filters.private & filters.command("start"))
async def start_message(bot, message):
    if not await db.is_user_exist(message.from_user.id):
        await db.add_user(message.from_user.id)
        if LOG_CHANNEL is not None:            
            await bot.send_message(LOG_CHANNEL,
                text=LOG_TEXT.format(id=message.from_user.id,
                    dc_id=message.from_user.dc_id,
                    first_name=message.from_user.first_name,
                    username=message.from_user.username,
                    bot=bot.mention)
            )
    if FSUB:
        client = bot
        is_participant = await get_fsub(client, message)
        if not is_participant:
            return
    button = InlineKeyboardMarkup([[            
           InlineKeyboardButton("⚡ ʜᴇʟᴩ", callback_data="help"),
           InlineKeyboardButton("📃 ᴀʙᴏᴜᴛ", callback_data="about") 
               ],[
           InlineKeyboardButton("Dᴇᴠᴇʟᴏᴘᴇʀ ❤", url="https://t.me/THE_DS_OFFICIAL")
              ]])

    await message.reply_photo(
        photo=random.choice(PICS),
        caption=txt.STAT.format(message.from_user.mention),
        reply_markup=button,
        parse_mode=enums.ParseMode.HTML
    )
                                              
@Client.on_message(filters.command(["id", "info"]))
async def media_info(bot, m): 
    message = m
    if FSUB:
        client = bot
        is_participant = await get_fsub(client, message)
        if not is_participant:
            return
    ff = m.from_user
    md = m.reply_to_message
    if md:
       try:
          if md.photo:
              await m.reply_text(text=f"**ʏᴏᴜʀ ᴘʜᴏᴛᴏ ɪᴅ ɪs **\n\n`{md.photo.file_id}`") 
          if md.sticker:
              await m.reply_text(text=f"**ʏᴏᴜʀ sᴛɪᴄᴋᴇʀ ɪᴅ ɪs**\n\n`{md.sticker.file_id}`")
          if md.video:
              await m.reply_text(text=f"**ʏᴏᴜʀ ᴠɪᴅᴇᴏ ɪᴅ ɪs**\n\n`{md.video.file_id}`")
          if md.document:
              await m.reply_text(text=f"**ʏᴏᴜʀ ᴅᴏᴄᴜᴍᴇɴᴛ ɪᴅ ɪs**\n\n`{md.document.file_id}`")
          if md.audio:
              await m.reply_text(text=f"**ʏᴏᴜʀ ᴀᴜᴅɪᴏɴ ɪᴅ ɪs**\n\n`{md.audio.file_id}`")
          if md.text:
              await m.reply_text("**ʜᴇʏ ʙʀᴏᴛʜᴇʀ ᴘʟᴇᴀsᴇ ʀᴇᴘʟʏ ᴡɪᴛʜ ( ᴘʜᴏᴛᴏ, ᴠɪᴅᴇᴏ, sᴛɪᴄᴋᴇʀ, ᴅᴏᴄᴜᴍᴇɴᴛs, ᴇᴛᴄ...) ᴏɴʟʏ ᴍᴇᴅɪᴀ**")  
          else:
              await m.reply_text("[404] ᴇʀʀᴏʀ..🤖")                                                                                      
       except Exception as e:
          print(e)
          await m.reply_text(f"[404] Error {e}")
                                        
    if not md:
        buttons = [[
            InlineKeyboardButton("Dᴇᴠᴇʟᴏᴘᴇʀ ❤", url="https://t.me/THE_DS_OFFICIAL")
        ]]       
        ds = await m.reply("please wait....")
        if ff.photo:
           user_dp = await bot.download_media(message=ff.photo.big_file_id)
           await m.reply_photo(
               photo=user_dp,
               caption=txt.INFO_TXT.format(id=ff.id, dc=ff.dc_id, n=ff.first_name, u=ff.username),
               reply_markup=InlineKeyboardMarkup(buttons),
               quote=True,
               parse_mode=enums.ParseMode.HTML,
               disable_notification=True
           )          
           os.remove(user_dp)
           await ds.delete()
        else:  
           await m.reply_text(
               text=txt.INFO_TXT.format(id=ff.id, dc=ff.dc_id, n=ff.first_name, u=ff.username),
               reply_markup=InlineKeyboardMarkup(buttons),
               quote=True,
               parse_mode=enums.ParseMode.HTML,
               disable_notification=True
           )

 
