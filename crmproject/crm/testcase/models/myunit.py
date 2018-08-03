#!/usr/bin/env python
# _*_ coding: utf-8 _*_

from .driver import browser
import unittest
import sys
reload(sys)
sys.setdefaultencoding('utf8')
# 封装浏览器的启动和关闭操作


class MyTest(unittest.TestCase):

    def setUp(self):
        self.driver = browser()
        self.driver.implicitly_wait(10)
        self.driver.maximize_window()

    def tearDown(self):
        self.driver.quit()
        print("teardown")


if __name__ == "__main__:":
    unittest.main()
