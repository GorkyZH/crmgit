#!/usr/bin/env python
# _*_ coding: utf-8 _*_

from selenium import webdriver
import os
import sys
reload(sys)
sys.setdefaultencoding('utf8')
# 封装了截图的操作方法


def insert_img(driver, file_name):
    base_dir = os.path.dirname(os.path.dirname(__file__))
    base_dir = str(base_dir)
    base_dir = base_dir.replace('\\', '/')
    print('base_dir:', base_dir)
    # base = base_dir.split('/test_case')[0]

    base = base_dir[:-9]
    print('base:', base)
    file_path = base + "/report/image/" + file_name
    print('file_path:', file_path)
    driver.get_screenshot_as_file(file_path)


if __name__ == '__main__':
    driver = webdriver.Chrome()
    driver.get("http://www.baidu.com")
    insert_img(driver, 'bd.jpg')
    driver.quit()
