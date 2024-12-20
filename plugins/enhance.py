from pyrogram import Client, filters
from pyrogram.types import Message
import requests
from HorridAPI.core import Core
from io import BytesIO
from info import *
from plugins.fsub import get_fsub

@Client.on_message(filters.command(["enhance", "upscale"]))
async def enhance_photo(client: Client, message: Message):   
    if FSUB:
        is_participant = await get_fsub(client, message)
        if not is_participant:
            return
    if not message.reply_to_message or not message.reply_to_message.photo:
        await message.reply("Please reply to a photo to enhance it.")
        return

    replied = message.reply_to_message    
    media = await replied.download()
    gfile = Core.upload(media)    
    mes = await message.reply_text("`Uploading...`")
    response = requests.get(gfile)
    image_data = BytesIO(response.content)

    # api url
    api = requests.post("https://horridapi.onrender.com/enhance", files={"image": image_data})

    bio = BytesIO(api.content)

    bio.seek(0)
    
    await message.reply_document(document=bio, file_name="photo.png", caption="**Successfully Uploaded**")
    await mes.delete()
