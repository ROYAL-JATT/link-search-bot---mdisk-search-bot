import os


class Config(object):
    API_ID = int(os.environ.get("API_ID", 28280795))
    API_HASH = os.environ.get("API_HASH", "3f02c2df6069de8c1a2abf623da0a4b8")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "6435441332:AAHgIrWtZsZmESb7v9Q15vDCVeNWZ5uv1bA")
    BOT_SESSION_NAME = os.environ.get("BOT_SESSION_NAME", "LinkSearchBot")
    USER_SESSION_STRING = os.environ.get("USER_SESSION_STRING", "BQF4fgoAvKQ36UtrGDOoWntMttIDofOPb8EoJ6LIQeEOCn-YnNZvRyTrZuWXZ_BQF0sQ4mJ39jUOA-roHv0v7jyE3KGdheQ5OD7kAlYOO0kCfp6eVej2MQRYhxGAAMXAKbAXdMx3nL_q2yuF7yWM17oTKfRZ9kxWlJiBTtR4Q9XC46TXDB7cPrswBXFtrVPc-X2HvtL-RwZbdnZ2YyoMFUeiLn5fnf2X1WQDFosQ6gPo0X-X5ciAxLn6_xP8S1shxop-skFp6timP8a5tqZGLRhHdBnjRR25fj3Pz59mjKYYw6-d6wvdmzGoeBmLyzI7DwfFaJ-8oU301z23xnwCuuD5tpe_rwAAAAF1aAloAA")
    CHANNEL_ID = int(os.environ.get("CHANNEL_ID", -1001907163330))
    BOT_USERNAME = os.environ.get("BOT_USERNAME", "Lisa_Auto_Filter_Pro_Bot")
    NAME = os.environ.get("NAME", "Anyname")
    BOT_OWNER = int(os.environ.get("BOT_OWNER", "6651109872"))
    DATABASE_URL = os.environ.get("DATABASE_URL", "mongodb+srv://Jk:0@cluster0.em2cobu.mongodb.net/?retryWrites=true&w=majority")
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

