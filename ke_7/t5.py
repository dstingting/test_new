# coding=utf-8
import json
from time import sleep
from selenium import webdriver
import chardet
from selenium.webdriver import ActionChains


#初始化浏览器
driver =  webdriver.Chrome()

#driver = webdriver.Firefox(executable_path = "e:\\geckodriver")
# driver = webdriver.Ie(executable_path = "e:\\IEDriverServer")


#定义全局遍变量url
url = "https://www.jd.com"


def login_cookie():
    #打开浏览器
    driver.get(url)
    # 浏览器最大化
    driver.maximize_window()
    #定位登录button
    driver.find_element_by_xpath('//a[@class = "link-login"]').click()
    #定位账户登录
    driver.find_element_by_xpath('//a[text()="账户登录"]').click()
    #定位账号框，并输入账号
    driver.find_element_by_xpath('//input[@name="loginname"]').send_keys("16602759069")
    #定位密码框，并输入密码
    driver.find_element_by_xpath('//input[@type="password"]').send_keys("duanshuo123")
    #点击登录button
    driver.find_element_by_xpath('//a[@id="loginsubmit"]').click()
    sleep(10)
    #需要手动滑动图片，通过校验

    #获取cookie
    my_cookie = driver.get_cookies()
    print(my_cookie)
    data_cookie = json.dumps(my_cookie)
    with open("jd_coolies","w") as fp:
        fp.write(data_cookie)

#使用cookies
def get_url_with_cookies():
    # 访问网站，清空旧cookies信息
    driver.get(url)
    driver.delete_all_cookies()
    #获取cookies文件
    with open("jd_coolies","r") as fp:
        jd_cookies = fp.read()
    #加载cookies信息
    jd_cookies_dict = json.loads(jd_cookies)
    for cookie in jd_cookies_dict:
        driver.add_cookie(cookie)
    #验证是否登录成功
    driver.get(url)
    assert '退出' in driver.page_source
    print(url)


# 添加购物车
def shopping():
    driver.get('https://www.jd.com/')
    # 定位搜索框，并输入：Python自动化
    driver.find_element_by_xpath("//input[@clstag='h|keycount|head|search_c']").send_keys('Python自动化')
    # 定位“搜索”button,并点击
    driver.find_element_by_xpath('//button[@clstag="h|keycount|head|search_a"]/i').click()
    # 获取当前窗口句柄
    now_handle = driver.current_window_handle
    # 打印当前窗口句柄
    print("添加购物车窗口")
    print(now_handle)

    #判断 不是 当前窗口句柄
    # 获取所有窗口句柄
    all_handles = driver.window_handles
    # 循环遍历所有新打开的窗口句柄，也就是说不包括主窗口
    for handle in all_handles:
        if handle != now_handle:
            # 切换窗口
            driver.switch_to.window(handle)
            sleep(5)
            # 点击加入购物车
            driver.find_element_by_xpath("//div[@class='itemInfo-wrap']/div/div/a[contains(@onclick,'加入购物车')]").click()
            # 调用driver的page_source属性获取页面源码
            pageSource = driver.page_source
            # 断言页面源码中是否包含“商品已成功加入购物车”关键字，以此判断页面内容是否正确
            assert "商品已成功加入购物车" in pageSource
            print("商品已成功加入购物车")


def payOrder():
    # # 获取当前窗口句柄
    current_handle = driver.current_window_handle
    # 打印当前窗口句柄
    print(current_handle)
    print("点击购物车")
    # 点击“我的购物车”
    driver.find_element_by_xpath("//a[text()='我的购物车']").click()
    sleep(2)
    all_handles = driver.window_handles
    # 循环遍历所有新打开的窗口句柄，也就是说不包括主窗口
    for handle in all_handles:
        if handle != current_handle:
            # 切换窗口
            driver.switch_to.window(handle)
    sleep(5)
    # 点击“去结算”button
    driver.find_element_by_xpath("//div[@id='cart-floatbar']/div/div/div/div[2]/div[4]/div[1]/div/div[1]").click()
    # driver.find_element_by_xpath("//a[contains(text(),'去结算')]").click()
    sleep(2)
    # 点击“提交订单”button
    driver.find_element_by_xpath("//button[@id='order-submit']").click()
    # 调用driver的page_source属性获取页面源码
    pageSource = driver.page_source
    # 断言页面源码中是否包含“商品已成功加入购物车”关键字，以此判断页面内容是否正确
    assert "订单提交成功，请尽快付款" in pageSource




if __name__== "__main__":
    login_cookie()
    get_url_with_cookies()
    shopping()
    payOrder()