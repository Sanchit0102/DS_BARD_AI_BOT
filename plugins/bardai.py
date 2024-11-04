import requests, asyncio, random, time
from pyrogram import filters, Client, enums
from pyrogram.types import *
from info import *
from plugins.fsub import get_fsub
from info import *
from helper.database import *
from .fsub import get_fsub

user_cooldowns = {}


async def send_typing_action(client, chat_id, duration=1):
    await client.send_chat_action(chat_id, enums.ChatAction.TYPING)
    await asyncio.sleep(duration)


async def bardandgemini(_: Client, message: Message):
    if FSUB:
        client = _
        is_participant = await get_fsub(client, message)
        if not is_participant:
            return
    if len(message.command) < 2:
        return await message.reply_text("Abey Gadhe Command k baad kuch likh!!")

    query = " ".join(message.command[1:])    
    sticker_file_id = "CAACAgQAAx0CbdTo9gACTmpnI2yEAURPYqvzGLANhwapRXyHgwACbg8AAuHqsVDaMQeY6CcRoh4E"
    s = await message.reply_sticker(sticker_file_id)
    await send_typing_action(_, message.chat.id, duration=2)
    app = f"https://horridapi.onrender.com/bard?query={query}"
    response = requests.get(app)
    data = response.json()
    api = data['text']
    await message.reply_text(
        text=f"ᴊᴀɪ sʜʀᴇᴇ ʀᴀᴍ {message.from_user.mention}. \nʏᴏᴜʀ ǫᴜᴇʀʏ : {query}\n\n[ʙᴀʀᴅ ᴀɪ](https://t.me/DS_BARD_AI_BOT) : \n{api}",
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
    await _.send_message(
                    LOG_CHANNEL,
                    text=f"<b>User:</b> @{message.from_user.username}\n\n<b>ID :</b> <code>{message.from_user.id}</code>\n\n<b>Asked to #Bard Ai :</b> {query}\n\n<b>Ai Responce:</b> {api}", disable_web_page_preview=True,
                )


async def ai_res(client, message, query):
    try:
        userMention = message.from_user.mention()
        DS = f"You are a helpful assistant. Your name is Cypher."
        obj = {'query' : query ,'bot_name' : BOT_NAME , 'bot_admin'  :ADMIN_NAME , 'system_prompt' : DS }
        url = f"https://bisal-ai-api.vercel.app/biisal"  # dont try to change anything here ⚠️
        res = requests.post(url , data=obj)
        if res.status_code == 200:
            response_json = res.json()
            api_response = response_json.get("response")
            if len(query) <= 280:
                await message.reply_text(
                    text=f"<b>ᴊᴀɪ sʜʀᴇᴇ ʀᴀᴍ {userMention}\nʏᴏᴜʀ ǫᴜᴇʀʏ : <code>{query}</code>\n\n{BOT_NAME} :\n{api_response}</b>",
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
            else:
                cut_query_str = query[:77]
                await message.reply_text(
                    text=f"<b>ᴊᴀɪ sʜʀᴇᴇ ʀᴀᴍ {userMention}\nʏᴏᴜʀ ǫᴜᴇʀʏ : <code>{cut_query_str}</code>\n\n{BOT_NAME} :\n{api_response}</b>",
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
                await client.send_message(
                    LOG_CHANNEL,
                    text=f"<b>User:</b> {userMention}\n\n<b>Asked to Ai :</b> {query}\n\n<b>Ai Res:</b> {api_response}",
                )

    except Exception as e:
        print(f"i got this err : {e}")
        await message.reply_text(f"sry i got this err : {e}")
    return


@Client.on_message(filters.command(["bard", "bardai"]))
async def grp_res(client, message):
    if FSUB:
        is_participant = await get_fsub(client, message)
        if not is_participant:
            return
    grp_query = (
        message.text.split(" ", 1)[1] if len(message.text.split(" ", 1)) > 1 else None
    )
    print(grp_query)
    if not grp_query:
        return await message.reply_text(
            "<b>Abe gadhe /bard k baad kuch likh to le !!.\n\nExample Use:\n<code>/bard Who is lord krshna??</code>\n\nHope you got it.Try it now..</b>"
        )
    '''
    current_time = time.time()
    coolDownUser = message.from_user.id
    if (
        coolDownUser in user_cooldowns
        and current_time - user_cooldowns[coolDownUser] < COOL_TIMER
    ):
        remaining_time = int(COOL_TIMER - (current_time - user_cooldowns[coolDownUser]))
        try:
            await message.react(emoji="😢")
        except Exception:
            pass
        remTimeMsg = await message.reply_text(
            f"<b>Nope..!! Spaming not allowed bro...\nPlease wait {remaining_time} seconds before sending new message...</b>"
        )
        await asyncio.sleep(remaining_time)
        await remTimeMsg.delete()
        return
    try:
        await message.react(emoji=random.choice(REACTIONS))
    except Exception:
        pass
        '''
    sticker_file_id = "CAACAgQAAx0CbdTo9gACTmpnI2yEAURPYqvzGLANhwapRXyHgwACbg8AAuHqsVDaMQeY6CcRoh4E"
    thinkStc = await message.reply_sticker(sticker_file_id)
    await send_typing_action(client, message.chat.id, duration=2)
    await ai_res(message, grp_query)
    # user_cooldowns[coolDownUser] = current_time
    await thinkStc.delete()
    return


@Client.on_message(filters.text & filters.private)
async def AiMsgHanDl(client, message):
    if message.text.startswith("/"):
        return
    if FSUB:
        is_participant = await get_fsub(client, message)
        if not is_participant:
            return
    current_time = time.time()
    coolDownUser = message.from_user.id
    if (
        coolDownUser in user_cooldowns
        and current_time - user_cooldowns[coolDownUser] < COOL_TIMER
    ):
        remaining_time = int(COOL_TIMER - (current_time - user_cooldowns[coolDownUser]))
        try:
            await message.react(emoji="😢")
        except Exception:
            pass
        remTimeMsg = await message.reply_text(
            f"<b>Nope..!! Spaming not allowed bro...\nPlease wait {remaining_time} seconds before sending new message...</b>"
        )
        await asyncio.sleep(remaining_time)
        await remTimeMsg.delete()
        return
    try:
        await message.react(emoji=random.choice(REACTIONS))
    except Exception:
        pass
    sticker_file_id = "CAACAgQAAx0CbdTo9gACTmpnI2yEAURPYqvzGLANhwapRXyHgwACbg8AAuHqsVDaMQeY6CcRoh4E"
    thinkStc = await message.reply_sticker(sticker_file_id)
    await send_typing_action(client, message.chat.id, duration=2)
    private_query = message.text
    await ai_res(message, private_query)
    user_cooldowns[coolDownUser] = current_time
    await thinkStc.delete()
    return
