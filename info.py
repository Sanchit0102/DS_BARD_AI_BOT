import re
import os
from os import environ

id_pattern = re.compile(r'^.\d+$')

BOT_TOKEN = os.environ.get("BOT_TOKEN", "8081707060:AAFhCq5hM8btuDu1i17FGiTQUAqYonk8YyE")
API_ID = int(os.environ.get("API_ID", "16536417"))
API_HASH = os.environ.get("API_HASH", "f6e58a549da642d7b765744a2f82c6d9")
PICS = os.environ.get("PICS", "https://envs.sh/_bC.jpg").split()
ADMIN = [int(admin) if id_pattern.search(admin) else admin for admin in environ.get('ADMINS', '1562935405').split()]
DB_URL = os.environ.get("DB_URL", "mongodb+srv://trumbot:trumbot@cluster0.cfkaeno.mongodb.net/?retryWrites=true&w=majority")
DB_NAME = os.environ.get("DB_NAME", "DSBardAI")
RemoveBG_API = os.environ.get("RemoveBG_API", "8js65jxBvtyywyLJTGFVzWiV")
IBB_API = os.environ.get("IBB_API", "843ceb81c0fe834bd1db328e68c32a87")
AUTH_CHANNEL = int(os.environ.get("AUTH_CHANNEL", "-1002104350566"))  
FSUB = os.environ.get("FSUB", True)
REACTIONS = ["❤️‍🔥", "⚡", "🔥"]
COOL_TIMER = 20 
ADMIN_NAME = os.environ.get("ADMIN_NAME", "Sanchit")
BOT_NAME = os.environ.get("BOT_NAME", "DS BARD AI BOT")
PORT = os.environ.get('PORT', '8080')          
LOG_CHANNEL = int(environ.get('LOG_CHANNEL', '-1002419311285'))
LOG_TEXT = """<i><u>👁️‍🗨️USER DETAILS</u>

○ ID : <code>{id}</code>
○ DC : <code>{dc_id}</code>
○ First Name : <code>{first_name}<code>
○ UserName : @{username}

By = {bot}</i>"""
