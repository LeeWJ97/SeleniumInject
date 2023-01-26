import time,importlib,os,traceback
from selenium import webdriver
from selenium.webdriver import ChromeOptions
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager   #自动下载匹配本机的Chromedriver



option = ChromeOptions()
option.add_argument('log-level=3')
option.add_experimental_option('excludeSwitches', ['enable-automation'])
#option.add_argument('--proxy-server=http://127.0.0.1:1080')
option.add_argument('--disable-gpu')
option.add_argument('--start-maximized')  # 最大化
option.add_argument('--incognito')  # 无痕隐身模式
option.add_argument("disable-cache")
option.add_argument('disable-infobars')
option.add_argument('log-level=3')
option.add_argument(
    f'user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36')
option.add_argument('--no-sandbox')
#driver = webdriver.Chrome('c:/chromedriver.exe', options=option)
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=option)
driver.implicitly_wait(5)

if __name__ == "__main__":
    driver.get('https://baidu.com')
    while 1:

        try:
            script = importlib.reload(importlib.import_module('script'))
            script.exec(driver)
        except Exception as e:
            print(traceback.print_exc())
        os.system('pause')

