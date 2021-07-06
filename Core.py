import random
import time
from Base import BigLearn
from ClassData.DataAPI import ClassExistsList, ClassGroupID
from Log import log
from Message import sendFriendMessage, sendGroupMessage
from Settings import SERVER_HOST, LOCAL_HOST, PORT, DEBUG, DEBUG_TOKEN, WorkTimeStart, WorkTimeEnd
from Server.server import server
from threading import Thread
from Scheduler import time_in_work, min_sleep


def main():
    bigLearn = BigLearn()
    classList = ClassExistsList()
    for classID in classList:
        remindMessage = bigLearn.classDoNotList(classID)
        groupID = ClassGroupID(classID)
        # send_user_message(bigLearn.classDoNotList(classID), 1462648167)  # 发送个人消息
        # time.sleep(5)
        # send_user_message(bigLearn.classDoNotList(classID), 304743174)  # 发送个人消息
        # time.sleep(5)
        if groupID != "":
            # sendFriendMessage(bigLearn.classDoNotList(classID), 1462648167)  # 发送个人消息
            sendGroupMessage(remindMessage, groupID)
            time.sleep(random.randint(10,60))

def cruise():
    now = time.localtime(time.time())
    start_hour = int(WorkTimeStart[:2])
    log.update("(Core): Daily Task Initialized Successfully")
    if now.tm_wday - 1 < 5: # 如果是工作日
        log.update("(Core): Working Day")
        if time_in_work(): # 执行当日任务时间
            main()
        elif now.tm_hour < start_hour: # 今日任务未开始
            log.update("(Core): Waiting to Start")
            now_str_time = "{}-{}-{} {}:{}".format(now.tm_year, now.tm_mon, now.tm_mday, now.tm_hour, now.tm_min)
            end_time = "{}-{}-{} {}".format(now.tm_year, now.tm_mon, now.tm_mday, WorkTimeStart)
            min_sleep(now_str_time, end_time)
        else: # 今日任务已结束
            log.update("(Core): Today's Mission Completed")
            now_str_time = "{}-{}-{} {}:{}".format(now.tm_year, now.tm_mon, now.tm_mday, now.tm_hour, now.tm_min)
            end_time = "{}-{}-{} {}".format(now.tm_year, now.tm_mon, now.tm_mday+1, WorkTimeStart)
            min_sleep(now_str_time, end_time)
    else: # 周末
        log.update("(Core): Over The Weekend")
        if now.tm_wday == 5: # 周六
            now_str_time = "{}-{}-{} {}:{}".format(now.tm_year, now.tm_mon, now.tm_mday, now.tm_hour, now.tm_min)
            end_time = "{}-{}-{} {}".format(now.tm_year, now.tm_mon, now.tm_mday+2, WorkTimeStart)
            min_sleep(now_str_time, end_time)
        if now.tm_wday == 6: # 周日
            # log.update("(Core): Over The Weekend")
            now_str_time = "{}-{}-{} {}:{}".format(now.tm_year, now.tm_mon, now.tm_mday, now.tm_hour, now.tm_min)
            end_time = "{}-{}-{} {}".format(now.tm_year, now.tm_mon, now.tm_mday+1, WorkTimeStart)
            min_sleep(now_str_time, end_time)

def run():
    while True:
        cruise()

def core():
    thread_core = Thread(target=run)
    thread_core.start()

    thread_server = Thread(target=server)
    thread_server.start()


if __name__ == "__main__":
    if DEBUG == True:
        log.update("(Core): ===== DEBUG MODE =====")
        main()
    else:
        core()
