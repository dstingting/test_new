import unittest

class IntegerArithmeticTestCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        # 执行用例前，只执行一次
        print("555555")

        # 执行用例后，只执行一次
    @classmethod
    def tearDownClass(cls):
        print("66666666")

    # def setUp(self):
    #     # 执行测试用例前都执行一次
    #     print("11111")
    #
    # def tearDown(self):
    #     # 执行测试用例后都执行一次
    #     print("2222")

    def testAdd(self):  # test method names begin with 'test'
        '''用例说明AAAAA'''
        self.assertEqual((1 + 2), 3)
        self.assertEqual(0 + 1, 1)

    def testMultiply(self):
        '''用例说明AAAAA'''
        self.assertEqual((0 * 10), 0)
        self.assertEqual((5 * 8), 40)


if __name__ == '__main__':
    unittest.main()