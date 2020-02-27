# coding=utf-8
from selenium import webdriver
import time
driver=webdriver.Chrome()
driver.get("https://account.cnblogs.com/signin?returnUrl=https%3A%2F%2Fwww.cnblogs.com%2F")
# 添加cookies
c1={u'domain':u'.cnblogs.com',
    u'name':u'CNBlogsCookies',
    u'value':u'CfDJ8Nf-Z6tqUPlNrwu2nvfTJEj-ZsUjqfNAUvmYAP7ymM6pSfDwG6KPUbsYE9YhPAeyq-FdFuL7jNqsi-YSvXvU6KRmgTXyxXtHZXwjMjkJOYnMNVyuQZXCRLWQQ2gt8fIo5VSNN-Iz-HNvQNmeyFbi8rgwhbGtvP_Pq-o9BHdV6a9XugZx_-x292f_r7feZp_h0Rgil-UM2trDzEyg5ktOUfcFmmDlTqW96YChFLgAEkJ_UA9xM3BqYQuLa92aajK1cDCNjd5URbZGAPTyp55iJBInYRp3_4hNthknSzE5V8Bz9DqMqDY4_-Ha-EbQvM788q9VA0dfRb3yfDAote4VkOaWz_gDCGpV-V12QseS9gzUKX1asGzQJgWHL_O5ObBi0gXvUZrMJTEpdTZ8_k6WolW4TITYNZ6poHXVf2kZ2ASp9OcmZEKug7iKl71SqmCYYUr3F6g_kB58GapXYIXiqWDdEYzMYP21JMjcbym85RPghQezjRhAKeOeoEuIa1KPRKcoloJ96hZLN91G5bcTkgMYLCJBDeziprZD10ibpvucFpQDU__pyXsLom6hMKMGbA',
    u'expiry':1645018207,
    u'path':u'/',
    u'httpOnly':True,
    u'secure':False
}

c2={u'domain':u'.cnblogs.com',
    u'name':u'Cnblogs.AspNetCore.Cookies',
    u'value':u'16B2D455B7D15BF8D29B9E232842EF66586FF96D13DF881B895AA2670669B1DB063D1C29FE687B6295F4F2C262EC34CB90E247AAB3BD17576EA98A003D925799C4B449D57133C8EF4DAC7EA42E444F054C684604',
    u'expiry':1645018207,
    u'path':u'/',
    u'httpOnly':True,
    u'secure':False
}

driver.add_cookie(c1)
driver.add_cookie(c2)
time.sleep(3)
driver.refresh()