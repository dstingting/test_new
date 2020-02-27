import unittest
from common import HTMLTestRunner_cn

 # 用例的路径
casePath="F:\\workplace\\PycharmProjects\\demo\\case"
rule="test*.py"
discover=unittest.defaultTestLoader.discover(start_dir=casePath,pattern=rule)
print(discover)

reportPath="F:\\workplace\\PycharmProjects\\demo\\report\\"+"report.html"
fp=open(reportPath,"wb")
runner=HTMLTestRunner_cn.HTMLTestRunner(stream=fp,
                                  title="报告的title",
                                  description="描述你的报告干什么用的")
runner.run(discover)
fp.close()




