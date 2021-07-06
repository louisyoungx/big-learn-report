import time
from Core.core import main
from Logs.logs import log
from Settings.settings import DEBUG, WorkTimeStart, WorkTimeEnd
from Scheduler.schedulerTools import time_in_work, min_sleep

def cruise():
    now = time.localtime(time.time())
    start_hour = int(WorkTimeStart[:2])
    log.update("Scheduler", "Daily Task Initialized Successfully")
    if now.tm_wday - 1 < 5: # 如果是工作日
        log.update("Scheduler", "Working Day")
        if time_in_work(): # 执行当日任务时间
            main()
        elif now.tm_hour < start_hour: # 今日任务未开始
            log.update("Scheduler", "Waiting to Start")
            now_str_time = "{}-{}-{} {}:{}".format(now.tm_year, now.tm_mon, now.tm_mday, now.tm_hour, now.tm_min)
            end_time = "{}-{}-{} {}".format(now.tm_year, now.tm_mon, now.tm_mday, WorkTimeStart)
            min_sleep(now_str_time, end_time)
        else: # 今日任务已结束
            log.update("Scheduler", "Today's Mission Completed")
            now_str_time = "{}-{}-{} {}:{}".format(now.tm_year, now.tm_mon, now.tm_mday, now.tm_hour, now.tm_min)
            end_time = "{}-{}-{} {}".format(now.tm_year, now.tm_mon, now.tm_mday+1, WorkTimeStart)
            min_sleep(now_str_time, end_time)
    else: # 周末
        log.update("Scheduler", "Over The Weekend")
        if now.tm_wday == 5: # 周六
            now_str_time = "{}-{}-{} {}:{}".format(now.tm_year, now.tm_mon, now.tm_mday, now.tm_hour, now.tm_min)
            end_time = "{}-{}-{} {}".format(now.tm_year, now.tm_mon, now.tm_mday+2, WorkTimeStart)
            min_sleep(now_str_time, end_time)
        if now.tm_wday == 6: # 周日
            # log.update("Scheduler", "Over The Weekend")
            now_str_time = "{}-{}-{} {}:{}".format(now.tm_year, now.tm_mon, now.tm_mday, now.tm_hour, now.tm_min)
            end_time = "{}-{}-{} {}".format(now.tm_year, now.tm_mon, now.tm_mday+1, WorkTimeStart)
            min_sleep(now_str_time, end_time)

def schedule():
    while True:
        cruise()
