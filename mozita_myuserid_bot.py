import telepot
import time
from telepot.loop import MessageLoop
import json
from pathlib import Path

TOKEN="---NASCOSTO---"

#COPIARE E INCOLLARE DA QUI - IL TOKEN E' GIA' INSERITO

versione="1"
ultimoAggiornamento="24-11-2018"

def risposte(msg):
    type_msg="NO"
    if "text" in msg and "entities" in msg:
        text=str(msg['text'])
        if text=="/start" or text=="/myuserid":
            type_msg="OK"
    else:
        type_msg="NO"

    user_id=msg['from']['id']
    if not "chat" in msg:
        msg=msg["message"]
    chat_id=msg['chat']['id']

    if type_msg=="OK":
        userid=[]
        userid_path="userid_list.json"
        if Path(userid_path).exists():
            userid = json.loads(open(userid_path).read())
        bot.sendMessage(chat_id, "Il tuo userid è: "+str(user_id))
        print(f"Il tuo userid è: {user_id}")
        if not int(user_id) in userid:
            userid.append(int(user_id))
        try:
            with open(userid_path, "wb") as f:
                f.write(json.dumps(userid).encode("utf-8"))
        except Exception as e:
            print("Excep:01 -> "+str(e))

bot=telepot.Bot(TOKEN)
MessageLoop(bot, {'chat': risposte, 'callback_query': risposte}).run_as_thread()

while 1:
    time.sleep(1)
