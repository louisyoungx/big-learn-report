from Core.core import main
from Logs.logs import log
from Scheduler.scheduler import schedule
from Settings.settings import DEBUG, SCHEDULER
from Server.server import server
from threading import Thread

def running():
    if SCHEDULER == False:
        thread_main = Thread(target=main)
        thread_main.start()
    else: # 调度器开启后main函数将被scheduler调度器代理，开启定时执行main
        thread_scheduler = Thread(target=schedule)
        thread_scheduler.start()

    thread_server = Thread(target=server)
    thread_server.start()

if __name__ == "__main__":
    if DEBUG == True:
        log.update("Core", "===== DEBUG MODE =====")
        main()
    else:
        running()

