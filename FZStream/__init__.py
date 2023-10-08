from os import getenv
from time import time
from dotenv import load_dotenv
from pyrogram import Client
from pyrogram.enums import ParseMode
from logging import getLogger, FileHandler, StreamHandler, INFO, ERROR, basicConfig
from uvloop import install

install()
basicConfig(format="[%(asctime)s] [%(levelname)s] - %(message)s", #  [%(filename)s:%(lineno)d]
            datefmt="%d-%b-%y %I:%M:%S %p",
            handlers=[FileHandler('log.txt'), StreamHandler()],
            level=INFO)

getLogger("pyrogram").setLevel(ERROR)
LOGGER = getLogger(__name__)

load_dotenv('config.env', override=True)
BOT_START = time()
__version__ = 1.0.0

class Config:
    BOT_TOKEN = getenv('BOT_TOKEN', '')
    API_HASH  = getenv('API_HASH', '')
    API_ID    = getenv('API_ID', '')
    if BOT_TOKEN == '' or API_HASH == '' or API_ID == '':
        LOGGER.critical('ENV Missing. Exiting Now...')
        exit(1)
    AUTH_CHATS     = getenv('AUTH_CHATS', '').split()
    OWNER_ID       = int(getenv('OWNER_ID', 0))
    FILES_CHANNEL  = int(getenv('FILES_CHANNEL'))
    PORT           = int(getenv('PORT', 8080))
    BIND_ADRESS    = str(getenv('BIND_ADRESS', '0.0.0.0'))
    PING_INTERVAL  = int(environ.get("PING_INTERVAL", "1200"))
    HIDE_PORT      = bool(getenv('HIDE_PORT', False))
    FQ_DOMAIN      = str(getenv('FQ_DOMAIN', BIND_ADRESS))
    ENABLE_SSL     = bool(getenv('ENABLE_SSL', False))
    STREAM_URL     = f"http{'s' if ENABLE_SSL else ''}://{FQ_DOMAIN.strip('/')}/"

Stream = Client("FZ", api_id=Config.API_ID, api_hash=Config.API_HASH, bot_token=Config.BOT_TOKEN, plugins=dict(root="FZBypass/plugins"), parse_mode=ParseMode.HTML)
