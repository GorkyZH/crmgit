#!/usr/bin/env python
# _*_ coding: utf-8 _*_
from crm.testcase.models import myunit
from crm.testcase.page_obj.loginPage import Login
from crm.testcase.page_obj.homePage import Home
from crm.config import globalparam
from crm.testcase.models import function
import time


class HomeTest(myunit.MyTest):
    """数据看板页面测试"""

    def user_login_verify(self, username="root", password="111111"):
        Login(self.driver).user_login(username, password)

    def switch_to_right_frame(self):
        Home(self.driver).switch_iframe()

    def test_007_home_verify_menu(self):
        """验证菜单标题"""
        self.user_login_verify()
        po = Home(self.driver)
        self.assertEqual(po.get_text(Home.menu1_loc), globalparam.MENU_SJKB_NAME)
        self.assertEqual(po.get_text(Home.menu2_loc), globalparam.MENU_KHGL_NAME)
        """
        self.assertEqual(Home(self.driver).get_text(Home.menu2_1_loc), globalparam.MENU_KHLB_NAME)
        self.assertEqual(Home(self.driver).get_text(Home.menu2_2_loc), globalparam.MENU_BQGL_NAME)
        self.assertEqual(Home(self.driver).get_text(Home.menu2_3_loc), globalparam.MENU_KHQX_NAME)
        """
        self.assertEqual(po.get_text(Home.menu3_loc), globalparam.MENU_KQDC_NAME)

        """
        self.assertEqual(Home(self.driver).get_text(Home.menu3_1_loc), globalparam.MENU_KQGL_NAME)
        """
        function.insert_img(self.driver, "verify_menu_name.jpg")

    def test_008_home_verify_title(self):
        """验证页面右侧文字标题"""
        self.user_login_verify()
        self.switch_to_right_frame()
        po = Home(self.driver)
        self.assertEqual(po.get_text(Home.title_loc), globalparam.HOME_PAGE_TITLE)   # 检验页面标题
        # self.assertEqual(Home(self.driver).get_text(Home.update_time_loc), globalparam.HOME_PAGE_TITLE + Login.gl_time)  # 检验数据更新时间
        self.assertEqual(po.get_text(Home.guest_title_loc), globalparam.HOME_GUEST_NUM_TITLE)         # 检验客户总数标题
        self.assertEqual(po.get_text(Home.customer_title_loc), globalparam.HOME_CUSTOMER_NUM_TITLE)   # 检验客群总数标题
        self.assertEqual(po.get_text(Home.push_title_loc), globalparam.HOME_PUSH_NUM_TITLE)           # 检验推送总数标题
        self.assertEqual(po.get_text(Home.guest_fx_loc), globalparam.HOME_GUEST_FX_TITLE)             # 检验客户分析标题
        self.assertEqual(po.get_text(Home.guest_gc_loc), globalparam.HOME_GUEST_GC_TITLE)             # 检验客户构成标题
        self.assertEqual(po.get_text(Home.guest_gc_ly_loc), globalparam.HOME_GUEST_LY_TITLE)          # 检验客户来源标题
        self.assertEqual(po.get_text(Home.guest_gc_zt_loc), globalparam.HOME_GUEST_ZT_TITLE)          # 检验客户状态标题
        self.assertEqual(po.get_text(Home.guest_gc_sx_loc), globalparam.HOME_GUEST_SX_TITLE)          # 检验客户属性标题
        self.assertEqual(po.get_text(Home.guest_trend_loc), globalparam.HOME_GUEST_QS_TITLE)          # 检验客户数据趋势标题
        self.assertEqual(po.get_text(Home.customer_fx_loc), globalparam.HOME_CUSTOMER_FX_TITLE)       # 检验客群分析标题
        self.assertEqual(po.get_text(Home.push_fx_loc), globalparam.HOME_PUSH_FX_TITLE)               # 检验推送分析标题

    def test_009_home_goto_guest(self):
        """点击客户总数跳转到客户列表页面"""
        self.user_login_verify()
        self.switch_to_right_frame()
        po = Home(self.driver)
        po.click_text(Home.guest_num_loc)
        time.sleep(3)
        self.assertEqual(po.get_text(Home.guest_page_title_loc), globalparam.GUEST_PAGE_TITLE)        # 检验当前页面是否为客户列表页面

    def test_010_home_goto_customer(self):
        """点击客群总数跳转到客群管理页面"""
        self.user_login_verify()
        self.switch_to_right_frame()
        po = Home(self.driver)
        po.click_text(Home.customer_title_loc)
        time.sleep(3)
        self.assertEqual(po.get_text(Home.guest_page_title_loc), globalparam.CUSTOMER_PAGE_TITLE)     # 检验当前页面是否为客群管理页面






