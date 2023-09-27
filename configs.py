import os


class Config(object):
    API_ID = int(os.environ.get("API_ID", 12345))
    API_HASH = os.environ.get("API_HASH", "")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "")
    BOT_SESSION_NAME = os.environ.get("BOT_SESSION_NAME", "LinkSearchBot")
    USER_SESSION_STRING = os.environ.get("USER_SESSION_STRING", "")
    CHANNEL_ID = int(os.environ.get("CHANNEL_ID", -100))
    BOT_USERNAME = os.environ.get("BOT_USERNAME")
    BOT_OWNER = int(os.environ.get("BOT_OWNER"))
    DATABASE_URL = os.environ.get("DATABASE_URL")
    UPDATES_CHANNEL = os.environ.get("UPDATES_CHANNEL", None)
    ABOUT_BOT_TEXT = """<b>This is Link Search Bot.
    
    
    
🤖 Mʏ Nᴀᴍᴇ:<a href='https://t.me/MOVIES_VILLA_UPDATE'>Mᴏᴠɪᴇs ᴠɪʟʟᴀ</a>

📝 Lᴀɴɢᴜᴀɢᴇ : <a href='https://www.python.org'> Pʏᴛʜᴏɴ V𝟹</a>

📚 Lɪʙʀᴀʀʏ: <a href='https://docs.pyrogram.org'> Pʏʀᴏɢʀᴀᴍ</a>

📡 Sᴇʀᴠᴇʀ: <a href='heroku.com'>Hᴇʀᴏᴋᴜ</a>

👨‍💻 Cʀᴇᴀᴛᴇᴅ Bʏ: <a href='https://t.me/MOVIES_VILLA_UPDATE'>Mᴏᴠɪᴇs ᴠɪʟʟᴀ</a></b>
"""

    ABOUT_HELP_TEXT = """<b>👨‍💻 Cʀᴇᴀᴛᴏʀ : <a href='https://t.me/ROYAL_GAGAN_DEEP_SINGH_MEHRA'>Mᴏᴠɪᴇs ᴠɪʟʟᴀ</a>
Iғ Yᴏᴜ Wᴀɴᴛ Yᴏᴜʀ Oᴡɴ Bᴏᴛ Lɪᴋᴇ Tʜɪs Tʜᴇɴ Yᴏᴜ Cᴀɴ Cᴏɴᴛᴀᴄᴛ Oᴜʀ Cʀᴇᴀᴛᴏʀ.</b>
"""

    HOME_TEXT = """
<b>Hᴇʏ! {}😅,

I'ᴍ Lɪɴᴋ Sᴇᴀʀᴄʜ Bᴏᴛ.🤖

I Cᴀɴ Sᴇᴀʀᴄʜ 🔍 Wʜᴀᴛ Yᴏᴜ Wᴀɴᴛ❗

<a>Mᴀᴅᴇ Wɪᴛʜ ❤ Bʏ <a href='https://t.me/ROYAL_GAGAN_DEEP_SINGH_MEHRA'>Oᴡɴᴇʀ</a></b>
"""


    START_MSG = """
<b>Hᴇʏ! {}😅,

I'ᴍ Lɪɴᴋ Sᴇᴀʀᴄʜ Bᴏᴛ.🤖

I Cᴀɴ Sᴇᴀʀᴄʜ 🔍 Wʜᴀᴛ Yᴏᴜ Wᴀɴᴛ❗

<a>Mᴀᴅᴇ Wɪᴛʜ ❤ Bʏ <a href='https://t.me/ROYAL_GAGAN_DEEP_SINGH_MEHRA'>Oᴡɴᴇʀ</a></b>
"""

