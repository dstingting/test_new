# coding=utf-8
from selenium import webdriver
import time
import unittest

class LoginTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()

    def setUp(self):
        self.driver.get("http://127.0.0.1:82/zentao/user-login-L3plbnRhby8=.html")

    def tearDown(self):
        # 清空cookies
        #self.delete_all_cookies()
        self.is_alert_exist()
        self.driver.delete_all_cookies()
        self.driver.refresh()

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    # 判断是否登录成功
    def get_login_name(self):
        try:
            time.sleep(3)
            t = self.driver.find_element_by_xpath('//*[@id="userMenu"]/a').text
            print(t)
            return t
        except:
            return ""

    # 没有登录成功，出现alert
    def is_alert_exist(self):
        try:
            alert=self.driver.switch_to.alert
            t=alert.text
            print(t)
            alert.accept()
        except:
            pass


    def test_01(self):
        self.driver.find_element_by_id("account").send_keys("admin")
        self.driver.find_element_by_xpath('//*[@id="login-form"]/form/table/tbody/tr[2]/td/input').send_keys("123456")
        self.driver.find_element_by_xpath(".//*[@id='submit']").click()
        # 判断是否登录成功
        t=self.get_login_name()
        print("获取的结果：%s"%t)
        self.assertTrue(t=="admin")

    def test_02(self):
        self.driver.find_element_by_id("account").send_keys("admin123")
        self.driver.find_element_by_xpath('//*[@id="login-form"]/form/table/tbody/tr[2]/td/input').send_keys("")
        self.driver.find_element_by_xpath(".//*[@id='submit']").click()

        # 判断是否登录成功
        time.sleep(3)
        t=self.get_login_name()
        print("获取登录结果%s"%t)
        self.assertTrue(t=="")

if __name__=="__main__":
    unittest.main()