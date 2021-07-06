import json
import requests

from Logs.logs import log


def sendFriendMessage(message, userid):
    try:
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

        # sender = requests.post(URL, params = params, data=json.dumps(body))
        sender = requests.post(URL, data=json.dumps(body))

        mes = message.replace("\n", " ")
        if len(mes) > 10:
            mes = mes[:10] + "···"
        log.update("Group Message", "Send {}".format(mes), "SUCCESS")


        # print(sender.request.url)
        # sender.raise_for_status()
        # print(sender.text)
        return True
    except:
        log.update("Group Message", "Message Send Failed", "ERROR")
        return False


def sendGroupMessage(message, groupid):
    try:
        URL = "www.louisyoung.site:8088"
        path = "sendGroupMessage"
        URL = "http://{}/{}".format(URL, path)

        body = {
            "sessionKey": "YourSession",
            "target": groupid,
            "messageChain": [
                {"type": "Plain", "text": message}
            ]
        }

        # sender = requests.post(URL, params = params, data=json.dumps(body))
        sender = requests.post(URL, data=json.dumps(body))
        mes = message.replace("\n", " ")
        if len(mes) > 10:
            mes = mes[:10] + "···"
        log.update("Group Message", "Send {}".format(mes), "SUCCESS")

        # print(sender.request.url)
        # sender.raise_for_status()
        # print(sender.text)
        return True
    except:
        log.update("Group Message", "Message Send Failed", "ERROR")
        return False
