import os
from os import getenv
from dotenv import load_dotenv

if os.path.exists("local.env"):
    load_dotenv("local.env")

API_ID = int(getenv("API_ID", "25250723"))  # added
API_HASH = getenv("API_HASH", "a58ea01e1ca590324243f3964a5d837d")  # added

SUDO_USERS = list(map(int, getenv("SUDO_USERS", "").split()))
OWNER_ID = int(getenv("OWNER_ID", "7211157842"))  # added
MONGO_URL = getenv("MONGO_URL")

BOT_TOKEN = getenv("BOT_TOKEN", "8380213264:AAETF8fr8vz-6aIwf6kwaRrFJtk7XzUj7jw")  # added

ALIVE_PIC = getenv("ALIVE_PIC", "https://telegra.ph/file/3c52a01057865f7511168.jpg")
ALIVE_TEXT = getenv("ALIVE_TEXT")

PM_LOGGER = getenv("PM_LOGGER")
LOG_GROUP = getenv("LOG_GROUP")

GIT_TOKEN = getenv("GIT_TOKEN")  # personal access token
REPO_URL = getenv("REPO_URL", "https://github.com/ITZ-ZAID/ZAID-USERBOT")
BRANCH = getenv("BRANCH", "master")  # don't change

STRING_SESSION1 = getenv("STRING_SESSION1", "BQGBS6MAPi3tCM6XGWLxCH_sd4Q0SXaoF9Bx1BH51oREUnXF92AgPZEfLXrlQ8hbxRNCw3pL0yslDlMVBkNQjiR2d7FE2A-wmLI_9rOShdakNGgzguim4BGN33YPpWbmovTfaoDoXfhcQ8sh-HZL3zeHj1lk--XrW43R-hFh_yyBEjZPe9JkUgyKj1ckUA-YiJSPkanq3JbP5UpuhYzav2ooFfqU6xvYXi8pnzbNEI6F35ABtVQ5nbM4JJfrb5VhSckCRgO2WhD1QbA-sPzASCtAn8Rw51S1q91U7aF4KMQ2vvBgp9Y4P_FbKz40EOF4H0Eg0pd3jsILUfQpwwj_3n7YnwhWHAAAAAHHf1D6AA")

STRING_SESSION2 = getenv("STRING_SESSION2", "")
STRING_SESSION3 = getenv("STRING_SESSION3", "")
STRING_SESSION4 = getenv("STRING_SESSION4", "")
STRING_SESSION5 = getenv("STRING_SESSION5", "")
STRING_SESSION6 = getenv("STRING_SESSION6", "")
STRING_SESSION7 = getenv("STRING_SESSION7", "")
STRING_SESSION8 = getenv("STRING_SESSION8", "")
STRING_SESSION9 = getenv("STRING_SESSION9", "")
STRING_SESSION10 = getenv("STRING_SESSION10", "")
