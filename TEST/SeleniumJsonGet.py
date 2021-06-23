import time
from scrapy import Selector
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from settings import Headless_Chrome, Chrome_Agent



class AutoSelenium(object):
    # Chrome请求头
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
        web = webdriver.Chrome('/usr/local/bin/chromedriver', options=self.chrome_options)
        try:
            web.get(self.site)
            web.maximize_window()

            # 如VPN速度不快需要开启以下两项
            # print("(5s)页面加载中······")
            # time.sleep(5)

            # 自动输入用户名
            web.find_element_by_xpath("//input[@name='account']").send_keys(username)
            # 自动输入密码
            web.find_element_by_xpath("//input[@name='password']").send_keys(password)
            web.find_element_by_xpath("//button[@lay-filter='LAY-user-login-submit']").click()
            time.sleep(3)
            web.get("https://jxtw.h5yunban.cn/jxtw-qndxx/admin/tzb/record.php")
            time.sleep(3)

            # TODO 此处业务处理
            res = Selector(text=web.page_source)
            InfoList = res.xpath("//td[@data-field='cardNo']//div/span/text()").extract()

            try:
                # next page
                web.find_element_by_xpath("//a[@class='layui-laypage-next']").click()
                time.sleep(1.5)
                res = Selector(text=web.page_source)
                InfoList += res.xpath("//td[@data-field='cardNo']//div/span/text()").extract()
            except:
                pass

            print(InfoList)

            print("Selenium Done!")
            print('======================================================')
            print('--------------  selenium  Over  ----------------------')
            print('======================================================')
            # time.sleep(1000)
            web.quit()
            return InfoList
        except:
            web.quit()
            print("ERROR")
            return "ERROR"

if __name__ == '__main__':
    auto = AutoSelenium()
    auto.Selenium("180851_102377", "466976")