#  coding=utf-8
from  selenium import webdriver
import time

driver=webdriver.Chrome()
url="http://127.0.0.1:81/zentao/user-login-L3plbnRhby8=.html"
driver.get(url)
driver.find_element_by_id("account").send_keys("admin")
driver.find_element_by_xpath("//input[@type='password']").send_keys("123456")
time.sleep(2)

driver.find_element_by_id("submit").click()

