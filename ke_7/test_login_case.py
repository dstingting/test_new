'''
1.用户名：admin  密码：123456   期望值：项目
2.用户名：       密码：123456   期望值：
3.用户名：admin123  密码：123456   期望值：
4.用户名：admin  密码：       期望值：项目
'''
# coding=utf-8
import unittest
from selenium import webdriver
from common.base import Base
from page.loginPage import LoginPage

class LoginPageCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()
        cls.login = LoginPage(cls.driver)

    def setUp(self):
        self.driver.get("http://127.0.0.1:81/zentao/user-login.html")
        self.login.get_login_name()

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    def tearDown(self):
        self.login.is_alert_exist()
        self.login.driver.delete_all_cookies()
        self.driver.refresh()

    def test_01(self):
        self.login.input_user("admin")
        self.login.input_pwd("123456")
        self.login.clicklogin()
        #断言ng started at 22:59 ...
        result=self.login.get_login_name()
        # print(result)
        self.assertTrue(result=="admin")

    def test_02(self):
        self.login.input_user("")
        self.login.input_pwd("123456")
        self.login.clicklogin()
        # 断言
        result=self.login.get_login_name()
        # print(result)
        self.assertTrue(result=="")

    def test_03(self):
        self.login.input_user("admin123")
        self.login.input_pwd("123456")
        self.login.clicklogin()
        # 断言
        result=self.login.get_login_name()
        self.assertTrue(result=="")

    def test_04(self):
        self.login.input_user("admin")
        self.login.input_pwd("")
        self.login.clicklogin()
        # 断言
        result=self.login.get_login_name()
        self.assertTrue(result=="")

if __name__ =="__main__":
    unittest.main()