import random
import time

from BigLearn.biglearn import BigLearn
from ClassData.DataAPI import ClassExistsList, ClassGroupID
from Message.message import sendGroupMessage, sendFriendMessage
from Settings.settings import DEBUG, SERVER_HOST, PORT


def main():
    bigLearn = BigLearn()
    classList = ClassExistsList()
    changeInfoURL = "http://{}:{}/changeInfo".format(SERVER_HOST, PORT)
    for classID in classList:
        remindMessage = bigLearn.classDoNotList(classID) + "\n申请更改大学习信息:\n" + changeInfoURL
        groupID = ClassGroupID(classID)
        if groupID != "":
            if DEBUG:
                sendFriendMessage(remindMessage, 1462648167)  # 发送个人消息
            else:
                sendGroupMessage(remindMessage, groupID)
            time.sleep(random.randint(10,60))