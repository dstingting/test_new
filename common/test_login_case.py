import unittest
from selenium import webdriver
from page.login_page import LoginPage,url

'''
1.输入admin，输入密码123456，点击登录
2.输入admin，输入密码   ，点击登录
3.输入admin，输入密码123456，点击保持登录按钮，点击登录
4.忘记密码
'''
class LaginPageCase(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver=webdriver.Chrome()
        cls.tingting=LoginPage(cls.driver)

    def setUp(self):
        self.driver.get(url)
        self.tingting.is_alert_exist()
        self.driver.delete_all_cookies()
        self.driver.refresh()

    def test_01(self):
        '''输入admin，输入密码123456，点击登录 '''
        self.tingting.input_user()
        self.tingting.input_psw()
        self.tingting.click_login_button()
        # 断言
        result = self.tingting.get_login_name()
        print(result)
        self.assertTrue(result == "admin")

    def test_04(self):
        '''输入admin，输入密码   ，点击登录'''
        self.tingting.input_user()
        self.tingting.input_psw("")
        self.tingting.click_login_button()
        # 断言
        result = self.tingting.get_login_name()
        print(result)
        self.assertTrue(result == "")

    def test_02(self):
        '''输入admin，输入密码123456，点击保持登录按钮，点击登录'''
        self.tingting.input_user()
        self.tingting.input_psw()
        self.tingting.keep_login()
        self.tingting.click_login_button()
        #断言
        result = self.tingting.get_login_name()
        print(result)
        self.assertTrue(result == "admin")


    def test_03(self):
        '''忘记密码'''
        self.tingting.forget_psw()
        # 断言
        result=self.tingting.is_refresh_exist()
        self.assertTrue(result)

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

if __name__ =="__main__":
    unittest.main()
