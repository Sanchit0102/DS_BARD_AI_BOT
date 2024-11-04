from pyrogram import Client, filters
from pyrogram.types import Message
import asyncio


IKKA_STRINGS = (
    "CAACAgUAAxkBAAIDUmIN8bqiD5DYQLjQzUwH7-1AsH0eAAJGBAAClj7wVxJlL3v8QuaoHgQ",
    "CAACAgUAAxkBAAIDVmIN8cCiVJZl05m0wiggUJaOvYarAAL5BAACo7lRVClze9Et3bCJHgQ",
    "CAACAgUAAxkBAAIDV2IN8cSKz20_0T-f7BlHVQfQYPu_AAKfAwACA4rwV01BOgyNllX1HgQ",
    "CAACAgUAAxkBAAIDWGIN8coT1jTnXpetiFOKVGZVCX78AAJLBAACrXgAAVTcB_E8ndEu0h4E",
    "CAACAgUAAxkBAAIDWWIN8c-GSo6HX8bmIvJOwDXG1pJ-AAJkBAACbYZIVIF7psBskaRiHgQ",
    "CAACAgUAAxkBAAIDWmIN8dfwrILfwAABBczAR4DoYxpkvAACvwUAAlNOSFRraTuQ8L5Qzx4E",
    "CAACAgUAAxkBAAIDXGIN8eN4RRZPSvKW5OcDhBGnF_qIAAJtBQACwq0JVAnAmIgTMZr6HgQ",
    "CAACAgUAAxkBAAIDeGIN8ke0Qm7S8rWAp5XRHtG21RP1AAJzBQACg5tAVL8bVAS2wafYHgQ",
    "CAACAgUAAxkBAAIDfGIN8lvvH0C9VGSLMV7fvxJ9L_r9AAIlBgACf4hJVA_SXDgpTipeHgQ",
    "CAACAgUAAxkBAAIDf2IN8nL54y-xsW_PGMX5T96e_ErnAAJiAwACjh3YV6f4T7ZwQqExHgQ",
    "CAACAgUAAxkBAAIDgmIN8oZFf70SfKUOl9nnk0Q0uIGPAAJjAwAC3-lRVqPrbp8AAeUBch4E",
    "CAACAgUAAxkBAAIDj2IN86K_5xEpxc00sVRoFLgNgvh_AALeAgACh49oVh2VB0KUEX3zHgQ",
    "CAACAgUAAxkBAAIDkmIN87LWn-56jo9wHTdifHsdBCAiAAJPAwACK4yZVlCyU1tXbk2YHgQ",
) 


@Client.on_message(filters.command("dice"))
async def roll_dice(bot, message):
    await bot.send_dice(message.chat.id, "🎲")

@Client.on_message(filters.command("arrow"))                                      
async def roll_arrow(bot, message):
    await bot.send_dice(message.chat.id, "🎯")

@Client.on_message(filters.command("goal"))
async def roll_goal(bot, message):
    await bot.send_dice(message.chat.id, "⚽️")

@Client.on_message(filters.command("luck"))
async def roll_luck(bot, message):
    await bot.send_dice(message.chat.id, "🎰")

@Client.on_message(filters.command("throw"))
async def roll_throw(bot, message):
    await bot.send_dice(message.chat.id, "🏀")

@Client.on_message(filters.command(["bowling", "tenpins"]))
async def roll_bowling(bot, message):
    await bot.send_dice(message.chat.id, "🎳")

@Client.on_message(filters.command("brain", ".") & filters.me)
async def pijtau(client: Client, message: Message):
    if message.forward_from:
        return
    animation_interval = 1
    animation_ttl = range(0, 14)
    await message.edit("brain")
    animation_chars = [          
              "YOᑌᖇ ᗷᖇᗩIᑎ ➡️ 🧠\n\n🧠         <(^_^ <)🗑",
              "YOᑌᖇ ᗷᖇᗩIᑎ ➡️ 🧠\n\n🧠       <(^_^ <)  🗑",
              "YOᑌᖇ ᗷᖇᗩIᑎ ➡️ 🧠\n\n🧠     <(^_^ <)    🗑",
              "YOᑌᖇ ᗷᖇᗩIᑎ ➡️ 🧠\n\n🧠   <(^_^ <)      🗑",
              "YOᑌᖇ ᗷᖇᗩIᑎ ➡️ 🧠\n\n🧠 <(^_^ <)        🗑",
              "YOᑌᖇ ᗷᖇᗩIᑎ ➡️ 🧠\n\n🧠<(^_^ <)         🗑",
              "YOᑌᖇ ᗷᖇᗩIᑎ ➡️ 🧠\n\n(> ^_^)>🧠         🗑",
              "YOᑌᖇ ᗷᖇᗩIᑎ ➡️ 🧠\n\n  (> ^_^)>🧠       🗑",
              "YOᑌᖇ ᗷᖇᗩIᑎ ➡️ 🧠\n\n    (> ^_^)>🧠     🗑",
              "YOᑌᖇ ᗷᖇᗩIᑎ ➡️ 🧠\n\n      (> ^_^)>🧠   🗑",
              "YOᑌᖇ ᗷᖇᗩIᑎ ➡️ 🧠\n\n        (> ^_^)>🧠 🗑",
              "YOᑌᖇ ᗷᖇᗩIᑎ ➡️ 🧠\n\n          (> ^_^)>🧠🗑",
              "YOᑌᖇ ᗷᖇᗩIᑎ ➡️ 🧠\n\n           (> ^_^)>🗑",
              "YOᑌᖇ ᗷᖇᗩIᑎ ➡️ 🧠\n\n           <(^_^ <)🗑",
          ]
    for i in animation_ttl:
        	
            await asyncio.sleep(animation_interval)
            await message.edit(animation_chars[i %14 ])
		
