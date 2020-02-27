'''
登录页面，写登录方法
每一个动作可用一个函数表示
'''
# coding=utf-8
from common.base import Base
from selenium import webdriver
import time

class LoginPage(Base):
    # 定位
    loc_user=("id","account")
    loc_pwd=("css selector","[name='password']")
    loc_keeplogin=("id","keepLoginon")
    loc_login=("id","submit")
    loc_forgetpwd=("link text","忘记密码")
    #loc_get_user=("xpath",".//*[@id='userMenu']/a")
    loc_get_user=("css selector","#userMenu>a")
    #输入账号
    def input_user(self,user):
        self.sendKeys(self.loc_user,user)
    #输入密码
    def input_pwd(self,pwd):
        self.sendKeys(self.loc_pwd, pwd)
    #保持登录
    def keepLogin(self):
        self.click(self.loc_keeplogin)
    #点击登录
    def clicklogin(self):
        self.click(self.loc_login)
    #忘记密码
    def input_forgetpwd(self):
        self.click(self.loc_forgetpwd)

    # 获取text
    def get_login_name(self):
        user=self.get_text(self.loc_get_user)
        return user

    def is_alert_exist(self):
        time.sleep(2)
        a=self.is_alert()
        if a:
            a.accept()

if __name__=="__main__":
    driver=webdriver.Chrome()
    driver.get("http://127.0.0.1:81/zentao/user-login.html")
    time.sleep(2)
    login=LoginPage(driver)
    login.input_user("admin")
    login.input_pwd("")
    login.clicklogin()
    login.is_alert_exist()
    driver.delete_all_cookies()
    driver.refresh()
    driver.quit()
