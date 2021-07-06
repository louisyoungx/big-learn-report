PROGRAM = "Big Learn Report"
AUTHOR = "Louis Young"


DEBUG = False # 开启DEBUG后只会执行Core.core.main函数中代码
DEBUG_TOKEN = "" # DEBUG = True and DEBUG_TOKEN != "" 就会强制启动Selenium获取Token

URL_Login = "https://jxtw.h5yunban.cn/jxtw-qndxx/admin/login.php"
URL_Records = "https://jxtw.h5yunban.cn/jxtw-qndxx/cgi-bin/branch-api/course/records"
URL_CourseList = "https://jxtw.h5yunban.cn/jxtw-qndxx/cgi-bin/branch-api/course/list"

USERNAME = "csygdgcxy_100886"
PASSWORD = "cgtw00"

# Chrome请求头
Chrome_Agent = 'user-agent=Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.83 Safari/537.36'

# selenium是否开启无头浏览器（开启DEBUG后此项失效，默认为True）
Headless_Chrome = True

SERVER_HOST = 'louisyoung.work'
LOCAL_HOST = "0.0.0.0"
PORT = 12007

QQBotUID = 2782594859

LOG_LENGTH = 100 # 记录100条数据

SERVER_LOG = False # 开启HTTP Server的log记录
SCHEDULER = True # 是否开启定时执行，调度器开启后main函数将被scheduler调度器代理，开启定时执行main
WorkTimeStart = '18:00' # 任务开启时间
WorkTimeEnd = '18:05' # 任务结束时间
