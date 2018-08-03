#!/usr/bin/env python
# _*_ coding: utf-8 _*_

import unittest
import random
from crm.testcase.models import myunit, function
from crm.testcase.page_obj.loginPage import Login
from crm.common.readcsv import read_user_data
import sys
sys.path.append("./models")
sys.path.append("./page_obj")
reload(sys)
sys.setdefaultencoding('utf8')


class LoginTest(myunit.MyTest):
    """登录测试"""

    def user_login_verify(self, username=read_user_data(0, "username"),
                          password=read_user_data(0, "password")):
        Login(self.driver).user_login(username, password)

    def test_001_login_user_pwd_empty(self):
        """账号密码均为空"""
        self.user_login_verify()
        print "提示语：", Login(self.driver).error_hint()
        self.assertEqual(Login(self.driver).error_hint(), "请输入账号")
        function.insert_img(self.driver, "user_pwd_empty.jpg")

    def test_002_login_pwd_empty(self):
        """密码为空"""
        self.user_login_verify(username=read_user_data(1, "username"),
                               password=read_user_data(1, "password"))
        po = Login(self.driver)
        self.assertEqual(po.error_hint(), "请输入密码")
        function.insert_img(self.driver, "pwd_empty.jpg")

    def test_003_login_user_empty(self):
        """账号为空"""
        self.user_login_verify(username=read_user_data(2, "username"),
                               password=read_user_data(2, "password"))
        po = Login(self.driver)
        self.assertEqual(po.error_hint(), "请输入账号")
        function.insert_img(self.driver, "user_empty.jpg")

    def test_004_login_pwd_success(self):
        """账号不正确,密码正确"""
        num = random.choice('1234567890')
        username = read_user_data(3, "username")+num
        self.user_login_verify(username=username, password=read_user_data(3, "password"))
        po = Login(self.driver)
        self.assertEqual(po.error_hint(), "您输入的账号或密码不正确，请重新输入！")
        function.insert_img(self.driver, "user_error.jpg")

    def test_005_login_user_success(self):
        """账号正确,密码不正确"""
        self.user_login_verify(username=read_user_data(4, "username"), password=read_user_data(4, "password"))
        po = Login(self.driver)
        self.assertEqual(po.error_hint(), "您输入的账号或密码不正确，请重新输入！")
        function.insert_img(self.driver, "pwd_error.jpg")

    def test_006_login_user_pwd_success(self):
        """账号正确,密码正确"""
        self.user_login_verify(username=read_user_data(5, "username"), password=read_user_data(5, "password"))
        po = Login(self.driver)
        self.assertEqual(po.success_hint(), read_user_data(5, "username"))
        function.insert_img(self.driver, "login_success.jpg")


if __name__ == "__main__":
    unittest.main()
