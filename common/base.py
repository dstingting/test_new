#coding=utf-8
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

class Base():
    def __init__(self,driver):
        self.driver = driver
        self.timeout=10
        self.t=1

    def findElement(self,locator):
        ele=WebDriverWait(self.driver,self.timeout,self.t).until(lambda driver : driver.find_element(*locator))
        return ele

    def sendKeys(self,locator,text):
        ele=self.findElement(locator)
        ele.send_keys(text)

    def click(self,locator):
        ele=self.findElement(locator)
        ele.click()

    def get_text(self,locator):
        try:
            t=self.findElement(locator).text
            return t
        except:
            print("获取text失败，返回''")
            return ""

    def is_alert(self):
        try:
            result=WebDriverWait(self.driver,self.timeout,self.t).until(EC.alert_is_present())
            return result
        except:
            return False

    def _is_text_in_element(self,locator,_text):
        '''返回bool值'''
        try:
            ele=WebDriverWait(self.driver,self.timeout,self.t).until(EC.text_to_be_present_in_element(locator,_text))
            return ele
        except:
            return False

    def isElementExit1(self,locator):
        try:
            self.findElement(locator)
            return  True
        except:
            False

if __name__=="__main__":
    driver=webdriver.Chrome()
    driver.get("http://127.0.0.1:81/zentao/user-login-L3plbnRhby8=.html")
    chandao=Base(driver)
    loc1=("id","account")
    loc2 = ("xpath", "//input[@type='password']")
    loc3 = ("id", "submit")
    chandao.sendKeys(loc1,"admin")
    chandao.sendKeys(loc2,"123456")
    chandao.click(loc3)
