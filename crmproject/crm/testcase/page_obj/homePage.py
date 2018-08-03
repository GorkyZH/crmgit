#!/usr/bin/env python
# _*_ coding: utf-8 _*_
import base
from selenium.webdriver.common.by import By
from crm.common.readcsv import read_home_by_data


class Home(base.Page):
    """首页-数据总览页面"""

    """
    菜单定位
    """
    menu1_loc = (By.XPATH, read_home_by_data(0))                # 菜单：数据看板
    menu2_loc = (By.XPATH, read_home_by_data(1))                # 菜单：客户管理
    menu2_1_loc = (By.XPATH, read_home_by_data(2))              # 菜单：客户列表
    menu2_2_loc = (By.XPATH, read_home_by_data(3))              # 菜单：标签管理
    menu2_3_loc = (By.XPATH, read_home_by_data(4))              # 菜单：客户清洗
    menu3_loc = (By.XPATH, read_home_by_data(5))                # 菜单：客群洞察
    menu3_1_loc = (By.XPATH, read_home_by_data(6))              # 菜单：客群管理

    """
    iframe窗口定位
    """
    myframe_loc = (By.ID, read_home_by_data(7))

    """
    数据看板元素定位
    """
    title_loc = (By.XPATH, read_home_by_data(8))                    # 页面标题定位
    update_time_loc = (By.XPATH, read_home_by_data(9))              # 更新数据时间定位
    guest_num_loc = (By.ID, read_home_by_data(10))                  # 客户总数数量定位
    guest_title_loc = (By.XPATH, read_home_by_data(11))             # 客户总数标题定位
    customer_num_loc = (By.ID, read_home_by_data(12))               # 客群总数数量定位
    customer_title_loc = (By.XPATH, read_home_by_data(13))          # 客群总数标题定位
    push_num_loc = (By.ID, read_home_by_data(14))                   # 推送总数数量定位
    push_title_loc = (By.XPATH, read_home_by_data(15))              # 推送总数标题定位

    guest_fx_loc = (By.XPATH, read_home_by_data(16))                # 客户分析标题定位
    guest_gc_loc = (By.XPATH, read_home_by_data(17))                # 客户构成标题定位
    guest_gc_ly_loc = (By.XPATH, read_home_by_data(18))             # 客户构成-数据来源标题定位
    guest_gc_zt_loc = (By.XPATH, read_home_by_data(19))             # 客户构成-客户状态标题定位
    guest_gc_sx_loc = (By.XPATH, read_home_by_data(20))             # 客户构成-客户属性标题定位
    guest_trend_loc = (By.XPATH, read_home_by_data(21))             # 客户数据趋势标题定位
    customer_fx_loc = (By.XPATH, read_home_by_data(22))             # 客群分析标题定位
    push_fx_loc = (By.XPATH, read_home_by_data(23))                 # 推送分析标题定位

    guest_page_title_loc = (By.XPATH, read_home_by_data(24))        # 客户列表页面标题

    # 获取菜单
    def get_text(self, loc):
        return self.find_element(*loc).text

    # 切换窗口
    def switch_iframe(self):
        self.switch_frame(self.myframe_loc)

    # 点击事件
    def click_text(self, loc):
        self.find_element(*loc).click()
