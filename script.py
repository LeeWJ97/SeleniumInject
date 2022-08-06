from selenium import webdriver

def highlight(driver: webdriver.Chrome,ele):
    driver.execute_script("arguments[0].setAttribute('style',arguments[1]);",ele, "border:5px solid yellow;")



#在这里写动态selenium操作
def exec(driver: webdriver.Chrome):
    driver.implicitly_wait(3)
    highlight(driver, driver.find_element('id', 'kw'))
    driver.find_element('id', 'kw').clear()
    driver.find_element('id','kw').send_keys('Selenium')
    driver.find_element('id','su').click()

