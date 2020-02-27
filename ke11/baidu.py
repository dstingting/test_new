# coding=utf-8
from common.base import Base
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.select import Select

driver=webdriver.Chrome()
driver.get("http://www.baidu.com")
loc1=("link text","设置")
dudu=Base(driver)
mouse=dudu.findElement(loc1)
ActionChains(driver).move_to_element(mouse).perform()

loc2=("link text","搜索设置")
dudu.click(loc2)

loc3=("id","nr")
s=dudu.findElement(loc3)
Select(s).select_by_value("20")

