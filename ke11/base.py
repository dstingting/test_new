# coding=utf-8
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

class Base():

    def __init__(self,driver):
        self.driver=driver
        self.timeout=10
        self.t=0.5

    def findElementNew(self,locator):
        ele=WebDriverWait(self.driver,self.timeout,self.t).until(EC.presence_of_element_located(locator))
        return ele

    def findElement(self,locator):
        ele=WebDriverWait(self.driver,self.timeout,self.t).until(lambda x : x.find_element(*locator))
        return ele


    def findElements(self,locator):
        try:
            eles=WebDriverWait(self.driver,self.timeout,self.t).until(lambda x : x.find_elements(*locator))
            return eles
        except:
            return []

    def sendKeys(self,locator,text):
        ele=self.findElement(locator)
        ele.send_keys(text)

    def click(self,locator):
        ele=self.findElement(locator)
        ele.click()

    def isElementExit1(self,locator):
        try:
            self.findElement(locator)
            return  True
        except:
            False

    def isElementExit2(self,locator):
        eles=self.findElements(locator)
        n=len(eles)
        if n==0:
            return False
        elif n==1:
            return True
        else:
            print("有元素个数%s"%n)
            return  True

    def is_title(self,_title):
        '''返回bool值'''
        try:
            ele=WebDriverWait(self.driver,self.timeout,self.t).until(EC.title_is(_title))
            return ele
        except:
            return  False


    def is_title_conditions(self,_title):
        '''返回bool值'''
        try:
            ele=WebDriverWait(self.driver,self.timeout,self.t).until(EC.title_contains(_title))
            return ele
        except:
            return False

    def _is_text_in_element(self,locator,_text):
        '''返回bool值'''
        try:
            ele=WebDriverWait(self.driver,self.timeout,self.t).until(EC.text_to_be_present_in_element(locator,_text))
            return ele
        except:
            return False

    def _is_value_in_element(self,locator,_value):
        '''返回bool值,value为空字符串，返回false'''
        try:
            ele=WebDriverWait(self.driver,self.timeout,self.t).until(EC.text_to_be_present_in_element_value(locator,_value))
            return ele
        except:
            return False

    def is_alert(self):
        try:
            result=WebDriverWait(self.driver,self.timeout,self.t).until(EC.alert_is_present())
            return result
        except:
            return False


if __name__ == "__main__":
    from selenium import webdriver
    driver=webdriver.Chrome()
    driver.get("http://127.0.0.1:82/zentao/user-login-L3plbnRhby8=.html")
    chandao=Base(driver)
    loc1=("id","account")
    loc2=("xpath",'//*[@id="login-form"]/form/table/tbody/tr[2]/td/input')
    loc3=("id","submit")

    chandao.sendKeys(loc1,"admin")
    chandao.sendKeys(loc2,"123456")
    chandao.click(loc3)