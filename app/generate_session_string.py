import os
try:
  import telethon
except:
  os.system("pip3 install -U -r requirements.txt")



from telethon.sync import TelegramClient
from telethon.sessions import StringSession

api_id = 1064864
api_hash = "5f3eeab0e6108731551e6a93598b654c"

with TelegramClient(StringSession(), api_id, api_hash) as client:
    print(client.session.save())
