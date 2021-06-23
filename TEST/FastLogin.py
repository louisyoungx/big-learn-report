import time
from scrapy import Selector
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from Settings import USERNAME, PASSWORD


class AutoLogin(object):
    # Chrome请求头
    Chrome_Agent = 'user-agent=Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.83 Safari/537.36'

    # selenium是否开启无头浏览器
    Headless_Chrome = False
    chrome_options = Options()
    chrome_options.add_argument("--profile-directory=Default")
    chrome_options.add_argument("--whitelisted-ips")
    chrome_options.add_argument("--start-maximized")
    chrome_options.add_argument("--disable-extensions")
    chrome_options.add_argument("--disable-plugins-discovery")

    if Headless_Chrome == True:
        # 此处开启后为无头浏览器
        chrome_options.add_argument('--headless')
        chrome_options.add_argument('--no-sandbox')
        chrome_options.add_argument('--disable-dev-shm-usage')
        chrome_options.add_argument('blink-settings=imagesEnabled=false')
        chrome_options.add_argument('--disable-gpu')

    chrome_options.add_argument(Chrome_Agent)
    site = 'https://jxtw.h5yunban.cn/jxtw-qndxx/admin/login.php'

    def __init__(self):
        pass

    def Selenium(self, username, password):
        print(self.site)
        print('======================================================')
        print('--------------  selenium  start  ---------------------')
        print('======================================================')

        driver = webdriver.Chrome('/usr/local/bin/chromedriver', options=self.chrome_options)
        driver.get(self.site)
        driver.maximize_window()

        # 如VPN速度不快需要开启以下两项
        # print("(5s)页面加载中······")
        # time.sleep(5)

        # 自动输入用户名
        driver.find_element_by_xpath("//input[@name='account']").send_keys(username)
        # 自动输入密码
        driver.find_element_by_xpath("//input[@name='password']").send_keys(password)
        driver.find_element_by_xpath("//button[@lay-filter='LAY-user-login-submit']").click()
        time.sleep(3)
        driver.get("https://jxtw.h5yunban.cn/jxtw-qndxx/admin/tzb/record.php")
        time.sleep(3)

        # TODO 此处业务处理

        res = Selector(text=driver.page_source)
        InfoList = res.xpath("//td[@data-field='cardNo']//div/span/text()").extract()

        try:
            # next page
            driver.find_element_by_xpath("//a[@class='layui-laypage-next']").click()
            time.sleep(1.5)
            res = Selector(text=driver.page_source)
            InfoList += res.xpath("//td[@data-field='cardNo']//div/span/text()").extract()
        except:
            pass


        for mem in InfoList:
            print(mem)

        js = 'return localStorage.getItem("pc_accessToken")'
        access_token = driver.execute_script(js)  # 调用js方法，同时执行javascript脚本
        print("access_token:" + access_token)

        print("Selenium Done!")
        print('======================================================')
        print('--------------  selenium  Over  ----------------------')
        print('======================================================')
        time.sleep(1000)
        driver.quit()
        return InfoList

if __name__ == '__main__':
    auto = AutoLogin()
    auto.Selenium(USERNAME, PASSWORD)