from pyrogram import Client, filters, enums
import requests
import urllib.parse
import asyncio
from info import *
import os

# Replace with your Hugging Face API token
headers = {"Authorization": "Bearer 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"}

# API URL for the model
API_URL = "https://api-inference.huggingface.co/models/google/gemma-2-2b"

def query(payload):
    response = requests.post(API_URL, headers=headers, json=payload)
    return response.json()

@Client.on_message(filters.command("jio"))
async def handle_gpt_command(bot, message):
    # Extract the question from the command
    question = message.text.split(" ", 1)[1]  # Get text after "gpt"

    # Send a request to the Hugging Face API
    output = query({"inputs": question})

    # Extract the response from Hugging Face
    response_text = output[0]["generated_text"].strip()

    # Send the response to the user
    await bot.send_message(message.chat.id, response_text)



'''
# Function to query the AI API
def ask_query(query):
    try:
        # Encode the user query for safe URL handling
        encoded_query = urllib.parse.quote(query)
    #    url = f"https://chatwithai.codesearch.workers.dev/?chat={encoded_query}&model={model}"
        url = f"https://lord-apis.ashlynn.workers.dev/?question={encoded_query}&mode=Gemini"

        # Send the request to the API
        response = requests.get(url)
        if response.status_code == 200:
            # Return the response or a fallback message if no result is found
            return response.json().get("result", "I couldn't find an answer to that.")
        else:
            return f"⚠️ Could not retrieve data from the API. (Status code: {response.status_code})"
    except Exception as e:
        return f"⚠️ An unexpected error occurred: {e}"

# Function to simulate typing action for an enhanced user experience
async def send_typing_action(client: Client, chat_id: int, duration: int = 1):
    await client.send_chat_action(chat_id, enums.ChatAction.TYPING)
    await asyncio.sleep(duration)

# Handler for the "/gemini" command
@Client.on_message(filters.command("gemini"))
async def handle_query(client, message):
    # Check if a query was provided by the user
    if len(message.command) < 2:
        await message.reply_text("💡 <b>Kindly provide a question to proceed.</b>")
        return

    # Get the user's question and mention
    user_query = message.text.split(maxsplit=1)[1]
    user_mention = message.from_user.mention

    # Simulate typing to enhance the user experience
    await send_typing_action(client, message.chat.id, duration=2)

    # Query the AI API for a response
    response = ask_query(user_query)

    # Send the response with user mention
    await message.reply_text(
        f"{user_mention}, <b>{response}</b>"
    )
'''



