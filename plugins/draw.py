from pyrogram import Client, filters
import requests, aiohttp
from info import *
from plugins.fsub import get_fsub

# Generate a detailed prompt for image creation
def generate_long_query(query):
    base_query = f"{query}."
    return base_query

@Client.on_message(filters.command(["draw", "generate"]))
async def draw_image(client, message):
    if FSUB:
        is_participant = await get_fsub(client, message)
        if not is_participant:
            return
    if len(message.command) < 2:
        await message.reply_text("**Please provide a query to generate an image.** 😊")
        return

    # Generate a long query for better image results
    user_query = message.text.split(" ", 1)[1]
    query = generate_long_query(user_query)

    # Send initial message
    wait_message = await message.reply_text("**Generating image, please wait...** ⏳")

    # Generate image URL using the API
    #url = f"https://text2img.codesearch.workers.dev/?prompt={query}"
    url = f"https://nexlynx.ashlynn.workers.dev/api/image?prompt={query}"
    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(url) as response:
                if response.status == 200:
                    image_data = await response.json()
                    if image_data.get("status") and image_data.get("image_urls"):
                        image_urls = image_data["image_urls"]
                        if image_urls:
                            await wait_message.delete()
                            await message.reply_photo(photo=image_urls[0], caption=f"Generated Image for: {user_query} 🖼️")
                        else:
                            await wait_message.edit_text("No images were returned. Please try again. ❌")
                    else:
                        await wait_message.edit_text("Failed to retrieve image URL. Please try again. ❌")
                else:
                    await wait_message.edit_text("Error: Unable to generate image at this time. Please try later. 🚫")
    except Exception as e:
        await wait_message.edit_text(f"An error occurred: {e} ⚠️")
