# coding=utf-8
from selenium import webdriver
from ke11.base import Base

driver=webdriver.Chrome()
driver.get("http://127.0.0.1:82/zentao/user-login-L3plbnRhby8=.html")

haha=Base(driver)
result=haha.is_title("用户登录 - 禅道23232")
print(result)


