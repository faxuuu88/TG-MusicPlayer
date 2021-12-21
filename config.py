import os
from dotenv import load_dotenv
from pyrogram import Client, filters
from pytgcalls import PyTgCalls

# For Local Deploy
if os.path.exists(".env"):
    load_dotenv(".env")
    
# Necessary Vars
API_ID = int(os.getenv("API_ID", "15020379"))
API_HASH = os.getenv("API_HASH", "36dc7ea1b7abc3ef395e3ce4908a7d77")
SESSION = os.getenv("SESSION", "AQCOSB-a6sJ1dw2d8QSbVjIr8uKxkdcNj2EIFDg1R790RAbMI0cBwqbpAYkfo2jxKI6t9DaSw2D2p-EUI6sBMnN_flsotKDevY0u0riYxdSK-XTTsqu9On_OR9N3icRVCd6b24DR7EXV319kkUFR7Hi1Sd-n2hsUAEjFKEed7r_onHao-yQH029K27R3eHevd4YJZ7hUiXUMECEaPLHnl-gpYpsicZnhK6w4X2fU8iNVmKFCMzNL2YtImYC533xFkdLWb32hkzm6KUtBOmUhxe5ivoAQRH3Skigqz-ww0drdyKUEpF9-Q-v1abuCJghOfNs48mOulUAjTUlSfdtlaCBufnwMwwA")
HNDLR = os.getenv("HNDLR", "!")
GROUP_MODE = os.getenv("GROUP_MODE", "False")


contact_filter = filters.create(
    lambda _, __, message:
    (message.from_user and message.from_user.is_contact) or message.outgoing
)


if GROUP_MODE == ("True" or "true"):
    grp = True
else:
    grp = False

GRPPLAY = grp
bot = Client(SESSION, API_ID, API_HASH, plugins=dict(root="VCBot"))
call_py = PyTgCalls(bot)
