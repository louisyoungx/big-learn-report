import random
import time

from BigLearn.biglearn import BigLearn
from ClassData.DataAPI import ClassExistsList, ClassGroupID
from Message.message import sendGroupMessage, sendFriendMessage
from Settings.settings import DEBUG


def main():
    bigLearn = BigLearn()
    classList = ClassExistsList()
    for classID in classList:
        remindMessage = bigLearn.classDoNotList(classID)
        groupID = ClassGroupID(classID)
        if groupID != "":
            if DEBUG:
                sendFriendMessage(bigLearn.classDoNotList(classID), 1462648167)  # 发送个人消息
            else:
                sendGroupMessage(remindMessage, groupID)
            time.sleep(random.randint(10,60))