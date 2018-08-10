#!/usr/bin/env python
# _*_ coding: utf-8 _*_
import base
from selenium.webdriver.common.by import By
from crm.common.readcsv import read_guest_by_data
from crm.common.readcsv import read_home_by_data


class Guest(base.Page):
    """客户管理-客户列表"""

    # 元素定位
    guest_frame_loc = (By.ID, read_home_by_data(7))                # 定位iframe
    guest_menu1_loc = (By.XPATH, read_guest_by_data(1))             # 客户管理菜单
    guest_menu1_1_loc = (By.XPATH, read_guest_by_data(2))           # 客户列表菜单
    guest_list_page_title_loc = (By.XPATH, read_guest_by_data(3))   # 定位页面标题

    guest_client_name_loc = (By.NAME, read_guest_by_data(4))        # 定位客户姓名
    guest_client_phone_loc = (By.NAME, read_guest_by_data(5))       # 定位客户号码
    guest_client_begindate_loc = (By.NAME, read_guest_by_data(6))   # 定位登记开始时间
    guest_client_enddate_loc = (By.NAME, read_guest_by_data(7))     # 定位登记结束时间
    guest_client_source_loc = (By.NAME, read_guest_by_data(8))      # 定位数据来源

    guest_client_search_loc = (By.XPATH, read_guest_by_data(9))     # 定位查询按钮
    guest_client_reset_loc = (By.XPATH, read_guest_by_data(10))     # 定位重置按钮

    # 列表字段定位
    guest_list_name_loc = (By.XPATH, read_guest_by_data(11))        # 客户姓名

    def get_loc(self):
        self.driver.find_element_by_xpath("//div[@id='customerListPage']/table/tbody/tr[%d]/td[1]" % i)

    # 切换窗口
    def switch_iframe(self):
        self.switch_frame("myFrame")

    # 录入关键词
    def input_value(self, value_name):
        # self.send_keys(self.guest_client_name_loc, value_name, False, True)
        self.find_element(*self.guest_client_name_loc).clear()
        self.find_element(*self.guest_client_name_loc).send_keys(value_name)

