import json
import time
import requests

from Log import log
from Settings import QQBotUID


def send_user_message(message, touseruid):
    try:
        URL = "http://www.louisyoung.site:8088/v1/LuaApiCaller"
        params = {
            'qq': QQBotUID,  #bot的QQ
            'funcname':'SendMsgV2', #调用方法类型
            }

        body = {
            "ToUserUid":touseruid,
            "SendToType":1,
            "SendMsgType":"TextMsg",
            "Content":message
            }

        r = requests.post(URL, params=params, data=json.dumps(body))
        mes = message.replace("\n", " ")
        if len(mes) > 10:
            mes = mes[:10] + "···"
        log.update("(Group Message): Send {} <SUCCESS>".format(mes))
        # print(r.request.url)
        # r.raise_for_status()
        # print(r.text)
        return True
    except:
        log.update("(Group Message)：Message Send Failed <ERROR>")
        return False

def send_group_message(message, GroupID):
    try:
        URL = "http://www.louisyoung.site:8088/v1/LuaApiCaller"
        params = {
            'qq': QQBotUID,  #bot的QQ
            'funcname':'SendMsgV2', #调用方法类型
            }

        body = {
            "ToUserUid": GroupID,
            "SendToType": 2,
            "SendMsgType": "TextMsg",
            "Content": message
        }

        # body = {
        #     "toUser":groupid,  #发到哪个QQ或者群号
        #     "sendToType":1,   #自己选择对应会话的数值
        #     "sendMsgType":"TextMsg",
        #     "content":message,   #要发送的文字内容
        #     "groupid":groupid,  #群号
        # }

        r = requests.post(URL, params = params, data=json.dumps(body))
        mes = message.replace("\n", " ")
        if len(mes) > 10:
            mes = mes[:10] + "···"
        log.update("(Group Message): Send {} <SUCCESS>".format(mes))
        # print(r.request.url)
        # r.raise_for_status()
        # print(r.text)
        return True
    except:
        print("(Group Message)：Message Send Failed <ERROR>")
        return False

def send_group_user_message(message, touseruid):
    try:
        URL = "http://www.louisyoung.site:8088/v1/LuaApiCaller"
        params = {
            'qq': QQBotUID,  #bot的QQ
            'funcname':'SendMsgV2', #调用方法类型
            }

        body = {
            "ToUserUid": touseruid,
            "GroupID": 791031608,
            "SendToType": 3,
            "SendMsgType": "TextMsg",
            "Content": message
        }


        # body = {
        #       "toUser":1462648167,  #发到哪个QQ或者群号
        #       "sendToType":1,   #自己选择对应会话的数值
        #       "sendMsgType":"TextMsg",
        #       "content":message,   #要发送的文字内容
        #       "groupid":791031608,  #群号
        #     }

        r = requests.post(URL, params=params, data=json.dumps(body))
        mes = message.replace("\n", " ")
        if len(mes) > 10:
            mes = mes[:10] + "···"
        log.update("(Group Message): Send {} <SUCCESS>".format(mes))
        # print(r.request.url)
        # r.raise_for_status()
        # print(r.text)
        return True
    except:
        print("(Group Message)：Message Send Failed <ERROR>")
        return False
