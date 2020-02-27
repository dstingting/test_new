# coding=utf-8
from selenium import webdriver
import time
import json
jg_url = "https://www.jd.com"

def login_jd():
    time.sleep(2)
    driver.find_element_by_link_text("你好，请登录").click()
    driver.find_element_by_link_text("账户登录").click()
    driver.find_element_by_id("loginname").send_keys("16602759069")
    driver.find_element_by_id("nloginpwd").send_keys("duanshuo123")
    driver.find_element_by_id("loginsubmit").click()
    # 基此处需要手动，进行图片验证

    # 获取cookies
    my_cookies=driver.get_cookies()
    print(my_cookies)
    data_cookies=json.dump(my_cookies)
    with open("jd_cookies","w") as fp:
        fp.write("data_cookies")

# 使用cookies
def get_url_with_cookies():
    driver.get(jg_url)
    driver.delete_all_cookies()
    # 获取cookies文件
    with open("jd_cookies","r") as fp:
        jd_cookies=fp.read()
    # 加载cookies信息
    jd_cookies_dict=json.loads(jd_cookies)
    for cookie in jd_cookies_dict:
        driver.add_cookie(cookie)
    driver.get(jg_url)
    assert "退出" in driver.page_source


if __name__ =="__main__":
    driver = webdriver.Chrome()
    driver.get(jg_url)
    driver.maximize_window()
    login_jd()