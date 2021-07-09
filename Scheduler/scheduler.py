import time
from Core.core import main
from Logger.logger import logger
from Config.settings import config
from Scheduler.tools import time_in_work, min_sleep

def cruise():
    now = time.localtime(time.time())
    WorkTimeStart = config.settings("Scheduler", "START_TIME")
    start_hour = int(WorkTimeStart[:2])
    logger.info("Daily Task Initialized Successfully")
    if now.tm_wday - 1 < 5: # 如果是工作日
        logger.info("Working Day")
        if time_in_work(): # 执行当日任务时间
            main()
        elif now.tm_hour < start_hour: # 今日任务未开始
            logger.info("Waiting to Start")
            now_str_time = "{}-{}-{} {}:{}".format(now.tm_year, now.tm_mon, now.tm_mday, now.tm_hour, now.tm_min)
            end_time = "{}-{}-{} {}".format(now.tm_year, now.tm_mon, now.tm_mday, WorkTimeStart)
            min_sleep(now_str_time, end_time)
        else: # 今日任务已结束
            logger.info("Today's Mission Completed")
            now_str_time = "{}-{}-{} {}:{}".format(now.tm_year, now.tm_mon, now.tm_mday, now.tm_hour, now.tm_min)
            end_time = "{}-{}-{} {}".format(now.tm_year, now.tm_mon, now.tm_mday+1, WorkTimeStart)
            min_sleep(now_str_time, end_time)
    else: # 周末
        logger.info("Over The Weekend")
        if now.tm_wday == 5: # 周六
            now_str_time = "{}-{}-{} {}:{}".format(now.tm_year, now.tm_mon, now.tm_mday, now.tm_hour, now.tm_min)
            end_time = "{}-{}-{} {}".format(now.tm_year, now.tm_mon, now.tm_mday+2, WorkTimeStart)
            min_sleep(now_str_time, end_time)
        if now.tm_wday == 6: # 周日
            # logger.info("Over The Weekend")
            now_str_time = "{}-{}-{} {}:{}".format(now.tm_year, now.tm_mon, now.tm_mday, now.tm_hour, now.tm_min)
            end_time = "{}-{}-{} {}".format(now.tm_year, now.tm_mon, now.tm_mday+1, WorkTimeStart)
            min_sleep(now_str_time, end_time)

def schedule():
    while True:
        cruise()
