import json
import requests
import time

from ClassData.DataAPI import ClassExistsList, ClassInfoData, nameFormatter
from Logger.logger import logger
from Config.settings import config
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

class BigLearn:
    BASE_DEBUG = False
    URL_login = config.settings("BigLearn", "URL_Login")  # 登录的URL
    URL_records = config.settings("BigLearn", "URL_Records")  # 查询的URL
    URL_courseList = config.settings("BigLearn", "URL_CourseList")  # 查询的URL
    username = config.settings("BigLearn", "USERNAME")  # 用户名
    password = config.settings("BigLearn", "PASSWORD")  # 密码
    config_agent = config.settings("Spider", "Chrome_Agent")  # 爬虫请求头
    config_headless = config.settings("Spider", "Headless_Chrome")  # 是否开启无头
    DEBUG = config.settings("Debug", "DEBUG")
    DEBUG_TOKEN = config.settings("Debug", "TOKEN")

    if DEBUG:
        config_headless = True

    chrome_options = Options()
    chrome_options.add_argument(config_agent)
    chrome_options.add_argument("--profile-directory=Default")
    chrome_options.add_argument("--whitelisted-ips")
    chrome_options.add_argument("--start-maximized")
    chrome_options.add_argument("--disable-extensions")
    chrome_options.add_argument("--disable-plugins-discovery")

    if config_headless == True:
        # 此处开启后为无头浏览器
        chrome_options.add_argument('--headless')
        chrome_options.add_argument('--no-sandbox')
        chrome_options.add_argument('--disable-dev-shm-usage')
        chrome_options.add_argument('blink-settings=imagesEnabled=false')
        chrome_options.add_argument('--disable-gpu')

    chrome_options = chrome_options
    if DEBUG == True and DEBUG_TOKEN != "":
        token = DEBUG_TOKEN
    else:
        token = None

    def __init__(self, course_id=""):
        if self.DEBUG == True and self.DEBUG_TOKEN != "":  # 启动Selenium获取Token
            logger.info("DEBUG_TOKEN: {}".format(self.DEBUG_TOKEN))
        else:
            self.getToken()
        if course_id == "":
            self.getCourseID()
        else:
            self.course_id = course_id
        logger.info("Course ID {}".format(self.course_id))
        self.getTotalList()
        self.doNotList()

    def getToken(self):
        logger.info("Get Token -> {}".format(self.URL_login))
        driver = webdriver.Chrome('/usr/local/bin/chromedriver', options=self.chrome_options)
        driver.get(self.URL_login)
        driver.maximize_window()

        # 如网速速度不快需要开启以下两项
        # logger.info("(5s)Loading······")
        # time.sleep(5)

        # 自动输入用户名
        driver.find_element_by_xpath("//input[@name='account']").send_keys(self.username)
        # 自动输入密码
        driver.find_element_by_xpath("//input[@name='password']").send_keys(self.password)
        driver.find_element_by_xpath("//button[@lay-filter='LAY-user-login-submit']").click()
        time.sleep(3)
        js = 'return localStorage.getItem("pc_accessToken")'
        self.token = driver.execute_script(js)  # 调用js方法，同时执行javascript脚本
        driver.quit()
        logger.info("access_token: {}".format(self.token))
        return self.token

    def getCourseID(self):
        parameters = {
            "pageSize": 99,
            "pageNum": 1,
            "desc": "startTime",
            "type": "网上主题团课",
            "accessToken": self.token
        }
        headers = {
            "User-Agent": self.config_agent[11:]
        }
        response = requests.get(self.URL_courseList, params=parameters, headers=headers)
        info = json.loads(response.text)
        self.course_id = info["result"]["list"][0]["id"]
        return self.course_id


    def getTotalList(self):
        logger.info("Getting the Total Info List······")
        self.totalDoList = []
        page = 1
        parameters = {
            "pageSize": 20,
            "pageNum": page,
            "desc": "createTime",
            "nid": "N001300081008",
            "course": self.course_id,
            "accessToken": self.token
        }
        headers = {
            "User-Agent": self.config_agent[11:]
        }
        response = requests.get(self.URL_records, params=parameters, headers=headers)
        info = json.loads(response.text)
        #log.update(info)
        if self.BASE_DEBUG == True: # 测试模式，加载一页数据用于测试
            self.totalDoList += info["result"]["list"]
            logger.info("{}".format(info["result"]["list"]))
        else: # 生产模式加载全部JSON数据
            while info["result"]["list"] != []:
                if self.DEBUG:
                    sign_left = int(page)*"=" + ">"
                    sign_right = (49-int(page))*"·"
                    logger.info("Page-{} [{}{}]".format(page, sign_left, sign_right))
                self.totalDoList += info["result"]["list"]
                page += 1
                parameters = {
                    "pageSize": 20,
                    "pageNum": page,
                    "desc": "createTime",
                    "nid": "N001300081008",
                    "course": self.course_id,
                    "accessToken": self.token
                }
                try:
                    response = requests.get(self.URL_records, params=parameters, headers=headers)
                except:
                    logger.info("<ERROR> 403 Forbidden - Too Fast")
                    page -= 1
                info = json.loads(response.text)
                # time.sleep(1)
        if info["status"] == 403:
            logger.info("<ERROR> 403 Forbidden - Token Invalid")
            self.getToken()
            return self.getTotalList()
        logger.info("Already Get the Total Data")
        return self.totalDoList

    def doList(self):
        nameList = []
        totalNum = 0
        for item in self.totalDoList:
            if item["branchs"][3] in ClassExistsList():
                totalNum += 1
                thisName = item["cardNo"]
                thisClass = item["branchs"][3]
                classInfo = ClassInfoData(thisClass)
                ID_Name = nameFormatter(thisName, classInfo)
                if ID_Name != "":
                    nameList.append(ID_Name)
        return nameList

    def doNotList(self):
        self.totalDoNotList = ClassInfoData()
        for item in self.totalDoList:
            if item["branchs"][3] in ClassExistsList():
                thisName = item["cardNo"]
                thisClass = item["branchs"][3]
                classInfo = ClassInfoData(thisClass)
                ID_Name = nameFormatter(thisName, classInfo)
                if ID_Name != "":
                    for eachClass in self.totalDoNotList:
                        if eachClass["ClassID"] == thisClass:
                            try:
                                eachClass["MemberList"].remove(ID_Name)
                            except:
                                #DEBUG log.update("Base.doNotList", "ERROR with ID-Name -> {}".format(ID_Name))
                                pass
        return self.totalDoNotList

    def classDoNotList(self, classID):
        DoNotList = []
        for eachClass in self.totalDoNotList:
            if eachClass["ClassID"] == classID:
                DoNotList = eachClass["MemberList"]
                break
        DoNotStr = ""
        for mem in DoNotList:
            DoNotStr = DoNotStr + mem + "\n"
        totalNum = len(ClassInfoData(classID))
        DoNotNum = len(DoNotList)
        DoNum = totalNum - DoNotNum
        Time = time.strftime("%Y-%m-%d", time.localtime())
        remindMessage = '{}班共{}人\n' \
              '已完成{}人，未完成{}人\n\n' \
              '未完成\n' \
              '{}\n' \
              '{}'.format(classID, totalNum, DoNum, DoNotNum, Time, DoNotStr)
        return str(remindMessage)


