import requests 
from Mangandi import ImageUploader
from pyrogram import Client, filters
from info import *
from plugins.fsub import get_fsub

api = "https://horridapi.onrender.com/search"

@Client.on_message(filters.command("scan_ph"))
async def scan_ph(client, message):
    if FSUB:
        is_participant = await get_fsub(client, message)
        if not is_participant:
            return
    reply = message.reply_to_message    
    if not reply:
        return await message.reply_text("**Reply to a photo to use this command!**")
    elif not reply.photo:
        return await message.reply_text("**Reply to a photo to use this command!**")
    elif reply.video:
        return await message.reply_text("**Reply to a photo to use this command!**")   
    query = message.text.split(" ", 1)[1] if len(message.text.split(" ")) > 1 else ""    
    if not query:
        await message.reply("**Provide query! like `/scan_ph tell me about of this image`**")
        return
    k = await message.reply_text(f"**Hey {message.from_user.mention}, Wait I am Checking **")
    media = await reply.download()
    m = await k.edit("**Successfully Checked Your query**")
    mag = ImageUploader(media)
    img_url = mag.upload()                   
    response = requests.get(f"{api}?img={img_url}&query={query}")   
    result = response.json()
    await m.edit(f"**Hey {message.from_user.mention},\n\n{result['response']}**")


    """
@Client.on_message(filters.command("scan_ph"))
async def telegraph_upload(client, message):
    if FSUB:
        is_participant = await get_fsub(client, message)
        if not is_participant:
            return
    if ONLY_SCAN_IN_GRP and message.chat.id != CHAT_GROUP:
        return await message.reply(
            text=f"<b>You can use this feature only in our support chat.</b>",
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
        )
    try:
        current_time = time.time()
        coolDownUser = message.from_user.id
        question = (
            message.text.split(" ", 1)[1]
            if len(message.text.split(" ", 1)) > 1
            else None
        )
        replied = message.reply_to_message
        if (
            coolDownUser in user_cooldowns
            and current_time - user_cooldowns[coolDownUser] < COOL_TIMER
        ):
            remaining_time = int(
                COOL_TIMER - (current_time - user_cooldowns[coolDownUser])
            )
            try:
                await message.react(emoji=random.choice(REACTIONS))
            except Exception:
                pass    
            remTimeMsg = await message.reply_text(
                f"<b>Please wait for {remaining_time} seconds before using /scan_ph again to prevent flooding. Thanks for your patience! 😊</b>"
            )
            await asyncio.sleep(remaining_time)
            await remTimeMsg.delete()
            return
        elif not replied:
            return await message.reply_text("<b>Replay a photo with this command !</b>")
        elif not (replied.photo):
            return await message.reply_text("<b>Please reply with valid image file</b>")
        elif replied.video:
            return await message.reply_text("Please reply with valid image file")
        question = message.text.split(" ", 1)[1] if " " in message.text else ""
        if not question:
            return await message.reply_text(
                "<b>Please provide a qustion after the /scan_ph command.\n\nExample Use:\n<code>/scan_ph tell me about this image ! </code>\n\nHope you got it.Try it now..</b>"
            )
        try:
            await message.react(emoji=random.choice(REACTIONS))
        except Exception:
            pass
        text = await message.reply_text(
            f"<b>Jai Shree Krishna {message.from_user.mention()},\nWᴀɪᴛ...😎</b>",
            disable_web_page_preview=True,
        )
        media = await replied.download()
        await text.edit_text(
            f"<b>ᴊᴀɪ sʜʀᴇᴇ ʀᴀᴍ {message.from_user.mention()},\nNᴏᴡ Iᴍ ᴄʜᴇᴄᴋɪɴɢ ʏᴏᴜʀ ɪᴍᴀɢᴇ...🤔</b>",
            disable_web_page_preview=True,
        )
        try:
            response = upload_file(media)
        except Exception as error:
            print(error)
            return await text.edit_text(
                text=f"Error :- {error}", disable_web_page_preview=True
            )
        try:
            os.remove(media)
        except Exception as error:
            print(error)
            return
        imgUrl = f"https://graph.org{response[0]}"
        try:
            url = f"https://bisal-ai-api.vercel.app/biisal/img?link={imgUrl}&question={question}"
            res = requests.get(url)
            if res.status_code == 200:
                response_json = res.json()
                airesponse = response_json.get("response")
            await text.edit_text(
                text=f"<b>Jai Shree Krishna {message.from_user.mention()},\n\n•{airesponse}</b>",
                reply_markup=InlineKeyboardMarkup(
                    [
                        [
                            InlineKeyboardButton(
                                "Dᴇᴠᴇʟᴏᴘᴇʀ ❤",
                                    url=f"https://t.me/THE_DS_OFFICIAL"
                            )
                        ]
                    ]
                ),
            )
            user_cooldowns[coolDownUser] = current_time
            return
        except Exception as e:
            await text.edit_text(f"<b>Sorry i Got Some error !!</b>")
            await asyncio.sleep(5)
            await text.delete()
            await replied.delete()
            await message.delete()
            return
    except Exception as e:
        print(f"I got this err to scan this img : {e}")
        await message.reply(f"I got this err to scan this img : {e}")"""
