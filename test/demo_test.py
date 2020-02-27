# coding=utf-8
# import unittest
# class Test(unittest.Case())

class Love():
    def forever(self,a=10):
        if a>0:
            print("我爱你哦!")
        else:
            print("I Love You!")

if __name__=="__main__":
    shuoshuo=Love()
    print("亲爱的，请输入一个整数")
    shuoshuo.forever(int(input()))




