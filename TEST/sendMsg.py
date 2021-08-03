import json

import requests


def sendFriendMessage(message, userid):
    URL = "www.louisyoung.site:8088"
    path = "sendFriendMessage"
    URL = "http://{}/{}".format(URL, path)

    body = {
        "sessionKey": "YourSession",
        "target": userid,
        "messageChain": [
            {"type": "Plain", "text": message}
        ]
    }
    sender = requests.post(URL, data=json.dumps(body))

    mes = message.replace("\n", " ")
    if len(mes) > 10:
        mes = mes[:10] + "···"
    print("Send {}".format(mes))

if __name__ == '__main__':
    sendFriendMessage("hh", 1462648167)
