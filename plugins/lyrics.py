
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton 
import requests 
from info import *
from plugins.fsub import get_fsub

API = "https://apis.xditya.me/lyrics?song="

@Client.on_message(filters.text & filters.command(["lyrics"]))
async def sng(bot, message):
        if FSUB:
            client = bot
            is_participant = await get_fsub(client, message)
            if not is_participant:
                return
        if not message.reply_to_message:
          await message.reply_text("Please reply to a message")
        else:          
          mee = await message.reply_text("`Searching 🔎`")
          song = message.reply_to_message.text
          chat_id = message.from_user.id
          rpl = lyrics(song)
          await mee.delete()
          try:
            await mee.delete()
            await bot.send_message(chat_id, text = rpl, reply_to_message_id = message.id, reply_markup = InlineKeyboardMarkup([[InlineKeyboardButton("DEV ", url = f"t.me/the_ds_official")]]))
          except Exception as e:                            
             await message.reply_text(f"I Can't Find A Song With `{song}`", quote = True, reply_markup = InlineKeyboardMarkup([[InlineKeyboardButton("Dev", url = f"t.me/the_ds_official")]]))


def search(song):
        r = requests.get(API + song)
        find = r.json()
        return find
       
def lyrics(song):
        fin = search(song)
        text = f'**🎶 Sᴜᴄᴄᴇꜱꜰᴜʟʟy Exᴛʀᴀᴄᴛᴇᴅ Lyɪʀɪᴄꜱ Oꜰ {song}**\n\n'
        text += f'`{fin["lyrics"]}`'
        text += '\n\n\n**Made By Artificial Intelligence**'
        return text



