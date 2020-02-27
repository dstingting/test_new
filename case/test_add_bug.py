# coding=utf-8
from selenium import webdriver
import unittest
import time
from case.add_bug import ZenTaoBug

class Test_Add_Bug(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver =webdriver.Chrome()
        cls.bug=ZenTaoBug(cls.driver)
        cls.bug.login()
        cls.driver.maximize_window()

    def test_add_bug(self):
        timestr =time.strftime("%Y_%m_%d_%H_%M_%S")
        title ="ceshi " +timestr
        self.bug.addBug(title)
        result =self.bug.is_add_sucess(title)
        print(result)
        self.assertTrue(result)

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

if __name__ == "__main__":
    unittest.main()