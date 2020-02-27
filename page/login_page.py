# coding=utf-8
from common.base import Base
from selenium import webdriver
import time

url="http://127.0.0.1:81/zentao/user-login-L3plbnRhby8=.html"
class LoginPage(Base):
    # 定位登录
    loc_user = ("id", "account")
    loc_pwd = ("xpath", '//*[@id="login-form"]/form/table/tbody/tr[2]/td/input')
    loc_keep_login=("id","keepLoginon")
    loc_click = ("id", "submit")
    loc_foget_pwd=("link text","忘记密码")
    loc_get_name=("xpath",'//*[@id="userMenu"]/a')
    loc_fogert_pws=("xpath",'/html/body/div/div/div[2]/p/a')

    # 输入用户名
    def input_user(self,user="admin"):
        self.sendKeys(self.loc_user,user)

    #输入密码
    def input_psw(self,psw="123456"):
        self.sendKeys(self.loc_pwd,psw)

    # 保持登录
    def keep_login(self):
        self.click(self.loc_keep_login)

    #登录
    def click_login_button(self):
        self.click(self.loc_click)

    # 忘记密码
    def forget_psw(self):
        self.click(self.loc_foget_pwd)

    def get_login_name(self):
        user=self.get_text(self.loc_get_name)
        return user

    def is_alert_exist(self):
        time.sleep(2)
        a=self.is_alert()
        if a:
            print(a.text)
            a.accept()

    def is_refresh_exist(self):
        result=self.isElementExit1(self.loc_fogert_pws)
        return result

    def login(self,user="admin",pwd="123456",keep_login=False):
        self.driver.get("http://127.0.0.1:82/zentao/user-login.html")
        self.zentao.sendKeys(self.loc_ad,user)
        self.zentao.sendKeys(self.loc_pwd,pwd)
        if keep_login:self.zentao.click(self.loc_keep_login)
        self.zentao.click(self.loc_click)

if __name__ =="__main__":
    driver=webdriver.Chrome()
    driver.get(url)
    log=LoginPage(driver)
    log.input_user()
    log.input_psw()
    log.click_login_button()
