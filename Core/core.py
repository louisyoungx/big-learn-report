import random
import time

from BigLearn.biglearn import BigLearn
from ClassData.DataAPI import ClassExistsList, ClassGroupID
from Message.message import sendGroupMessage, sendFriendMessage
from Config.settings import config


def main():
    DEBUG = config.settings("Debug", "DEBUG")
    PORT = config.settings("Server", "PORT")
    SERVER_HOST = config.settings("Server", "SERVER_HOST")
    bigLearn = BigLearn()
    classList = ClassExistsList()
    changeInfoURL = "http://{}:{}/change.html".format(SERVER_HOST, PORT)
    for classID in classList:
        remindMessage = bigLearn.classDoNotList(classID) + "\n申请更改大学习信息:\n" + changeInfoURL
        groupID = ClassGroupID(classID)
        if groupID != "":
            if DEBUG:
                sendFriendMessage(remindMessage, 1462648167)  # 发送个人消息
            else:
                sendGroupMessage(remindMessage, groupID)
            time.sleep(random.randint(10,60))