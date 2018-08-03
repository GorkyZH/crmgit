#!/usr/bin/env python
# _*_ coding: utf-8 _*_

from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import base
from crm.common.readcsv import read_login_by_data


class Login(base.Page):
    """
    用户登录页面
    """
    url = '/'

    # 定位元素

    login_username_loc = (By.ID, read_login_by_data(0))
    login_password_loc = (By.ID, read_login_by_data(1))
    login_button_loc = (By.CLASS_NAME, read_login_by_data(2))

    error_hint_loc = (By.XPATH, read_login_by_data(3))
    print(error_hint_loc)
    success_hint_loc = (By.XPATH, read_login_by_data(4))
    print(success_hint_loc)

    """
    login_username_loc = (By.ID, "operId")
    login_password_loc = (By.ID, "operPwd")
    login_button_loc = (By.CLASS_NAME, "submit")

    error_hint_loc = (By.XPATH, "//form/div[@class='DmpFine-login-box-body']/div[3]")
    print(error_hint_loc)
    """

    # 操作元素
    def login_username(self, username):
        self.find_element(*self.login_username_loc).send_keys(username)

    def login_password(self, password):
        self.find_element(*self.login_password_loc).send_keys(password)

    def login_button(self):
        self.find_element(*self.login_button_loc).click()

    # 定义统一的登录入口
    def user_login(self, username="root", password="111111"):

        self.open()
        # self.bbs_login()
        self.login_username(username)
        self.login_password(password)
        self.login_button()
        # gl_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(time.time()))
        time.sleep(3)

    # 错误提示
    def error_hint(self):
        return self.find_element(*self.error_hint_loc).text

    # 正确提示
    def success_hint(self):
        return self.find_element(*self.success_hint_loc).text
