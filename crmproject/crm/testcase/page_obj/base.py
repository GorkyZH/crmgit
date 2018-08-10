#!/usr/bin/env python
# _*_ coding: utf-8 _*_
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException
import selenium.webdriver.support.ui as ui
from selenium.webdriver.common.by import By
import sys
reload(sys)
sys.setdefaultencoding('utf8')


class Page(object):
    """
    页面基础类，用于所有页面的继承该类
    """

    crm_url = 'http://172.16.2.123:8081/crm2'

    def __init__(self, selenium_driver, base_url=crm_url, parent=None):
        self.base_url = base_url
        self.driver = selenium_driver
        self.timeout = 30
        self.parent = parent

    def _open(self, url):
        url = self.base_url + url
        self.driver.get(url)
        print "----------------:", url
        assert self.on_page(), 'Did not land on %s' % url

    def find_element(self, *loc):
        try:
            WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(loc))
            return self.driver.find_element(*loc)
        except NoSuchElementException:
            print "%s 页面中未能找到 %s 元素" % (self, loc)

    def find_elements(self, *loc):
        return self.driver.find_elements(*loc)

    def open(self):
        self._open(self.url)

    def on_page(self):
        print("current_url:", self.driver.current_url)
        print("url:", self.base_url + self.url)
        return self.driver.current_url == self.base_url + self.url

    def script(self, src):
        return self.driver.execute_script(src)

    def switch_frame(self, loc):
        return self.driver.switch_to.frame(loc)

    def click_text(self, loc):
        self.find_element(*loc).click()

    def get_text(self, loc):
        return self.find_element(*loc).text

    # 重写定义send_keys方法
    def send_keys(self, loc, vaule="", clear_first=True, click_first=True):
        try:
            loc = getattr(self, "_%s" % loc)  # getattr相当于实现self.loc
            if click_first:
                self.find_element(*loc).click()
            if clear_first:
                self.find_element(*loc).clear()
                self.find_element(*loc).send_keys(vaule)
        except AttributeError:
            print "%s 页面中未能找到 %s 元素" % (self, loc)

    # 一直等待某元素可见，默认超时10秒
    def is_visible(self, locator, timeout=10):
        try:
            ui.WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located((By.XPATH, locator)))
            return True
        except TimeoutException:
            return False

    # 一直等待某个元素消失，默认超时10秒
    def is_not_visible(self, locator, timeout=10):
        try:
            ui.WebDriverWait(self.driver, timeout).until_not(EC.visibility_of_element_located((By.XPATH, locator)))
            return True
        except TimeoutException:
            return False
