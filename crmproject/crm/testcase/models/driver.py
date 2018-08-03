#!/usr/bin/env python
# _*_ coding: utf-8 _*_

from selenium.webdriver import Remote
from selenium import webdriver
import sys
reload(sys)
sys.setdefaultencoding('utf8')
# 启动浏览器


def browser():
    driver = webdriver.Chrome()
    """
    host = '127.0.0.1:4444'
    dc = {'browserName': 'chrome'}
    driver = Remote(command_executor='http://' + host + '/wd/hub', desired_capabilities=dc)
    """

    return driver


if __name__ == '__main__':
    dr = browser()
    dr.get("http:www.baidu.com")
    dr.quit()
