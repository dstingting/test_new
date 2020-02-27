import unittest
from selenium import webdriver
from page.login_page import LoginPage,url
import ddt
from common.read_excel import ExcelUtil
import os
'''
1.输入admin，输入密码123456，点击登录
2.输入admin，输入密码   ，点击登录
3.输入admin111，输入密码123456，点击登录
'''
# testdatas=[
#     {"user": "admin","psw": "123456","expect": "admin"},
#     {"user": "admin","psw": "","expect": ""},
#     {"user": "admin111","psw": "123456","expect": ""}
#           ]
propath=os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
filepath=os.path.join(propath,"common","datas.xlsx")
print(filepath)
# filepath="F:\\workplace\\PycharmProjects\\demo\\common\\datas.xlsx"
data=ExcelUtil(filepath)
testdatas=data.dict_data()
print(testdatas)


@ddt.ddt
class LaginPageCase(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver=webdriver.Chrome()
        cls.tingting=LoginPage(cls.driver)

    def setUp(self):
        self.driver.get(url)

    def login_case(self,user,psw,expect):
        self.tingting.input_user(user)
        self.tingting.input_psw(psw)
        self.tingting.click_login_button()
        # 断言
        result = self.tingting.get_login_name()
        print(result)
        self.assertTrue(result == expect)

    @ddt.data(*testdatas)
    def test_01(self,data):
        '''输入admin，输入密码123456，点击登录 '''
        print("测试数据“%s" % data)
        self.login_case(data["user"],data["psw"],data["expect"])

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    def tearDown(self):
        self.tingting.is_alert_exist()
        self.driver.delete_all_cookies()
        self.driver.refresh()

if __name__ =="__main__":
    unittest.main()

