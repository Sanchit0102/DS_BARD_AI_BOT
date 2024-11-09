from pyrogram import Client, filters
from pyrogram.types import Message
from pyrogram.enums import ChatAction
import requests
import urllib.parse
import asyncio
from info import *
from plugins.fsub import *
from helper.database import *

def ask_query(query, model=None):
    default_model = 'mistralai/Mixtral-8x7B-Instruct-v0.1'
    system_prompt = """You are a helpful assistant. Your name is DS BARD AI BOT, and your owner's name is Sanchit, known as @THE_DS_OFFICIAL"""

    model = model or default_model

    if model == default_model:
        query = f"{system_prompt}\n\nUser: {query}"

    encoded_query = urllib.parse.quote(query)
    url = f"https://darkness.ashlynn.workers.dev/chat/?prompt={encoded_query}&model={model}"

    response = requests.get(url)

    if response.status_code == 200:
        return response.json().get("response", "😕 Sorry, no response found.")
    else:
        return f"⚠️ Error fetching response from API. Status code: {response.status_code}"

@Client.on_message(filters.command("ask"))
async def ask_query_command(client, message):
    if FSUB:
        is_participant = await get_fsub(client, message)
        if not is_participant:
            return
    # Get the query from the message
    query = message.text.split(" ", 1)  # Split the command to get the query
    if len(query) > 1:
        user_query = query[1]  # Get the actual question part
        
        sticker_file_id = "CAACAgQAAx0CbdTo9gACTmpnI2yEAURPYqvzGLANhwapRXyHgwACbg8AAuHqsVDaMQeY6CcRoh4E"
        s = await message.reply_sticker(sticker_file_id)
        reply = ask_query(user_query)
        await send_typing_action(client, message.chat.id)
        await message.reply_text(
            text=f"ᴊᴀɪ sʜʀᴇᴇ ʀᴀᴍ {message.from_user.mention}. \nʏᴏᴜʀ ǫᴜᴇʀʏ : {user_query}\n\n[ʙᴀʀᴅ ᴀɪ](https://t.me/DS_BARD_AI_BOT) : \n{reply}",
            reply_markup=InlineKeyboardMarkup(
                            [
                                [
                                    InlineKeyboardButton(
                                        "Dᴇᴠᴇʟᴏᴘᴇʀ ❤",
                                        url=f"https://t.me/THE_DS_OFFICIAL",
                                    )
                                ]
                            ]
                        ),
                        disable_web_page_preview=True,
                    )
    
        await s.delete()
        await client.send_message(
                        LOG_CHANNEL,
                        text=f"<b>User:</b> @{message.from_user.username}\n\n<b>ID :</b> <code>{message.from_user.id}</code>\n\n<b>Asked to Ai:</b> {user_query}\n\n<b>Ai Responce:</b> {reply}", disable_web_page_preview=True,
        )
    else:
        await message.reply_text("📝 Please provide a query to ask DS BARD AI BOT! Don't be shy, let's chat! 🤖💬.")

@Client.on_message(filters.mentioned & filters.group)
async def handle_mention(client: Client, message: Message):
    if FSUB:
        is_participant = await get_fsub(client, message)
        if not is_participant:
            return

    # Extract the text to process
    user_text = message.reply_to_message.text.strip() if message.reply_to_message and message.reply_to_message.text else message.text.split(" ", 1)[1].strip()

    if user_text:
        # Send typing action to simulate a response delay
        sticker_file_id = "CAACAgQAAx0CbdTo9gACTmpnI2yEAURPYqvzGLANhwapRXyHgwACbg8AAuHqsVDaMQeY6CcRoh4E"
        s = await message.reply_sticker(sticker_file_id)
        reply = ask_query(user_text)
        await send_typing_action(client, message.chat.id)
        await message.reply_text(
            text=f"ᴊᴀɪ sʜʀᴇᴇ ʀᴀᴍ {message.from_user.mention}. \nʏᴏᴜʀ ǫᴜᴇʀʏ : {user_text}\n\n[ʙᴀʀᴅ ᴀɪ](https://t.me/DS_BARD_AI_BOT) : \n{reply}",
            reply_markup=InlineKeyboardMarkup(
                            [
                                [
                                    InlineKeyboardButton(
                                        "Dᴇᴠᴇʟᴏᴘᴇʀ ❤",
                                        url=f"https://t.me/THE_DS_OFFICIAL",
                                    )
                                ]
                            ]
                        ),
                        disable_web_page_preview=True,
                    )
    
        await s.delete()
        await client.send_message(
                        LOG_CHANNEL,
                        text=f"<b>User:</b> @{message.from_user.username}\n\n<b>ID :</b> <code>{message.from_user.id}</code>\n\n<b>Asked to Ai in #Group:</b> {user_text}\n\n<b>Ai Responce:</b> {reply}", disable_web_page_preview=True,
        )
    else:
        await message.reply("👋 Please ask a question after mentioning me! I’m here to help! 😊")

# Simulate Typing Action
async def send_typing_action(client, chat_id, duration=1):
    """
    Simulate typing action.
    """
    await client.send_chat_action(chat_id, ChatAction.TYPING)  # Use ChatAction enum
    await asyncio.sleep(duration)  # Wait for the specified duration
