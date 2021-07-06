import datetime
import time
from Logs.logs import log
from Settings.settings import WorkTimeStart, WorkTimeEnd


def getTime():
    # time.localtime(time.time())
    # int tm_sec; /* 秒 – 取值区间为[0,59] */
    # int tm_min; /* 分 - 取值区间为[0,59] */
    # int tm_hour; /* 时 - 取值区间为[0,23] */
    # int tm_mday; /* 一个月中的日期 - 取值区间为[1,31] */
    # int tm_mon; /* 月份（从一月开始，0代表一月） - 取值区间为[0,11] */
    # int tm_year; /* 年份，其值等于实际年份减去1900 */
    # int tm_wday; /* 星期 – 取值区间为[0,6]，其中0代表星期一，1代表星期二，以此类推 */
    # int tm_yday; /* 从每年的1月1日开始的天数 – 取值区间为[0,365]，其中0代表1月1日，1代表1月2日，以此类推 */
    # int tm_isdst; /* 夏令时标识符，实行夏令时的时候，tm_isdst为正。不实行夏令时的时候，tm_isdst为0；不了解情况时，tm_isdst()为负。
    return time.localtime(time.time())

def dormancy(to_time):
    pass

def min_sleep(startTime, endTime):
    '''计算两个时间点之间的分钟数'''
    # 处理格式,加上秒位
    startTime1 = startTime + ':00'
    endTime1 = endTime + ':00'
    # 计算分钟数
    startTime2 = datetime.datetime.strptime(startTime1, "%Y-%m-%d %H:%M:%S")
    endTime2 = datetime.datetime.strptime(endTime1, "%Y-%m-%d %H:%M:%S")
    seconds = (endTime2 - startTime2).seconds
    # 来获取时间差中的秒数。注意，seconds获得的秒只是时间差中的小时、分钟和秒部分的和，并没有包含时间差的天数（既是两个时间点不是同一天，失效）
    total_seconds = (endTime2 - startTime2).total_seconds()
    # 来获取准确的时间差，并将时间差转换为秒
    log.update("Scheduler", "Sleeping -> Resume Work at {}".format(endTime2))
    time.sleep(total_seconds)
    return True

def time_in_work():
    '''判断当前时间是否触发'''
    # 范围时间
    start_time = datetime.datetime.strptime(str(datetime.datetime.now().date()) + WorkTimeStart, '%Y-%m-%d%H:%M')
    end_time = datetime.datetime.strptime(str(datetime.datetime.now().date()) + WorkTimeEnd, '%Y-%m-%d%H:%M')
    # 当前时间
    now_time = datetime.datetime.now()
    # 判断当前时间是否在范围时间内
    # print(end_time, now_time, start_time)
    if end_time > now_time > start_time:
        return True
    else:
        return False
