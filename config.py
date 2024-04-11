from os import getenv

API_ID = int(getenv("API_ID", "13335263"))
API_HASH = getenv("API_HASH", "")
BOT_TOKEN = getenv("BOT_TOKEN", "")
OWNER_ID = int(getenv("OWNER_ID", ""))
STRING_SESSION = getenv("STRING_SESSION", "")
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "6458155947").split()))
ALIVE_PIC = getenv("ALIVE_PIC", "https://telegra.ph/file/bc7eda1dd7ea382b57bfb.jpg")
REPO_URL = getenv("REPO_URL", "https://github.com/ITS-LUCKY-BOY/Romeo-UserBot")
BRANCH = getenv("BRANCH", "main")
