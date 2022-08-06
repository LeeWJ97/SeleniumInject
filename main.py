import time,importlib,os,traceback
from selenium import webdriver

options = webdriver.ChromeOptions()
options.add_argument('log-level=3')
options.add_experimental_option('excludeSwitches', ['enable-automation'])

driver = webdriver.Chrome('c:/chromedriver.exe')
driver.implicitly_wait(5)

if __name__ == "__main__":
    driver.get('http://baidu.com')
    while 1:
        os.system('pause')
        try:
            script = importlib.reload(importlib.import_module('script'))
            script.exec(driver)
        except Exception as e:
            print(traceback.print_exc())

