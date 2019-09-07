import time
from selenium import webdriver

browser = webdriver.Chrome()
browser.get('http://www.baidu.com')

element_kw = browser.find_element_by_id('kw')
element_kw.send_keys('Python')
element_su = browser.find_element_by_id('su')
element_su.click()

# time.sleep(3)
# browser.quit()
