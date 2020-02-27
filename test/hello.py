# coding=utf-8
import unittest
from selenium import webdriver

class  Hello(unittest.TestCase):
    def setUp(self):
        self.driver=webdriver.Chrome()
        self.driver.get("http://127.0.0.1:82/zentao/user-login-L3plbnRhby8=.html")

    def test_1(self):
        self.driver.find_element_by_id("account").send_keys("admin")
        self.driver.find_element_by_xpath("//input[@type='password']").send_keys("123456")
        self.driver.find_element_by_id("submit").click()
        # 断言
        result=self.driver.find_element_by_css_selector("#userMenu>a").text
        print(result)
        self.assertTrue(result=="admin")

if __name__=="__main__":
    unittest.main()
