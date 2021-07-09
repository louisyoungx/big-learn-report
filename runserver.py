from Core.core import main
from Logger.logger import logger
from Scheduler.scheduler import schedule
from Config.settings import config
from Server.server import server
from threading import Thread

def running():
    SCHEDULER = config.settings("Scheduler", "START_USING")
    if SCHEDULER == False:
        thread_main = Thread(target=main)
        thread_main.start()
    else: # 调度器开启后main函数将被scheduler调度器代理，开启定时执行main
        thread_scheduler = Thread(target=schedule)
        thread_scheduler.start()

    thread_server = Thread(target=server)
    thread_server.start()

if __name__ == "__main__":
    DEBUG = config.settings("Debug", "DEBUG")
    if DEBUG == True:
        logger.info("\n===== DEBUG MODE =====")
        main()
    else:
        running()

