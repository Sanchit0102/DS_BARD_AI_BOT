import asyncio, os, sys
from pyrogram import Client, filters
import requests, urllib.parse, asyncio
from pyrogram.types import Message
from info import *

@Client.on_message(filters.command('logs') & filters.user(ADMIN))
async def log_file(bot, message):
    """Send log file"""
    try:
        await message.reply_document('TELEGRAM BOT.LOG')
    except Exception as e:
        await message.reply(str(e))

@Client.on_message(filters.command("restart") & filters.user(ADMIN))
async def stop_button(bot, message):
    msg = await bot.send_message(text="🔄 𝙿𝚁𝙾𝙲𝙴𝚂𝚂𝙴𝚂 𝚂𝚃𝙾𝙿𝙴𝙳. 𝙱𝙾𝚃 𝙸𝚂 𝚁𝙴𝚂𝚃𝙰𝚁𝚃𝙸𝙽𝙶...", chat_id=message.chat.id)       
    await asyncio.sleep(3)
    await msg.edit("✅️ 𝙱𝙾𝚃 𝙸𝚂 𝚁𝙴𝚂𝚃𝙰𝚁𝚃𝙴𝙳. 𝙽𝙾𝚆 𝚈𝙾𝚄 𝙲𝙰𝙽 𝚄𝚂𝙴 𝙼𝙴")
    os.execl(sys.executable, sys.executable, *sys.argv)
