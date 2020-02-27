# coding=utf-8
from common.base import Base
from selenium import webdriver
import time

class ZenTaoBug():

    # 定位登录
    loc_ad=("id","account")
    loc_pwd=("xpath",'//*[@id="login-form"]/form/table/tbody/tr[2]/td/input')
    loc_click=("id","submit")
    # 定位添加bug
    loc_test=("link text","测试")
    loc_bug=("link text","Bug")
    loc_add_bug=("xpath",'//*[@id="createActionMenu"]/a')
    loc_version=("xpath",'//*[@id="openedBuild_chosen"]/ul')
    loc_version_trunk=("xpath",'//*[@id="openedBuild_chosen"]/div/ul/li')
    loc_title=("id","title")
    # 切换iframe
    loc_body=("class name",'article-content')
    loc_save=("id","submit")
    # 定位标题
    loc_ad_title=("xpath",'//*[@id="bugList"]/tbody/tr[1]/td[4]/a')

    def __init__(self,driver):
        self.driver = driver
        self.zentao = Base(self.driver)
       # 点击登录
    def login(self,user="admin",pwd="123456"):
        self.driver.get("http://127.0.0.1:82/zentao/user-login.html")
        self.zentao.sendKeys(self.loc_ad,user)
        self.zentao.sendKeys(self.loc_pwd,pwd)
        self.zentao.click(self.loc_click)

    def addBug(self,_title="ceshi",_text="i love tingting"):
        self.zentao.click(self.loc_test)
        self.zentao.click(self.loc_bug)
        self.zentao.click(self.loc_add_bug)
        self.zentao.click(self.loc_version)
        self.zentao.click(self.loc_version_trunk)
        self.zentao.sendKeys(self.loc_title,_title)
        # 切换iframe
        loc_iframe=("class name","ke-edit-iframe")
        frame=self.zentao.findElement(loc_iframe)
        self.driver.switch_to.frame(frame)
        self.zentao.sendKeys(self.loc_body,_text)
        self.driver.switch_to.default_content()
        js = "window.scrollTo(0,document.body.scrollHeight)"
        self.driver.execute_script(js)
        self.zentao.click(self.loc_save)

        # 判断是否添加成功
    def is_add_sucess(self,_text):
        return self.zentao._is_text_in_element(self.loc_ad_title,_text)


if __name__ =="__main__":
    driver=webdriver.Chrome()
    # 最大化
    driver.maximize_window()
    dudu=ZenTaoBug(driver)
    dudu.login( )
    timestr=time.strftime("%Y_%m_%d_%H_%M_%S")
    title="ceshi"+timestr
    dudu.addBug(title)
    result=dudu.is_add_sucess(title)
    print(result)

