#!/usr/bin/env python
# _*_ coding: utf-8 _*_
from crm.testcase.models import myunit
from crm.testcase.page_obj.loginPage import Login
from crm.testcase.page_obj.guestPage import Guest
from crm.testcase.models import function
from crm.common.readcsv import read_guest_keyword_data
import unittest
import time
from crm.config import globalparam
import sys
reload(sys)
sys.setdefaultencoding('utf8')


class GuestTest(myunit.MyTest):

    def user_login_verify(self, username="root", password="111111"):
        Login(self.driver).user_login(username, password)

    def switch_to_right_frame(self):
        Guest(self.driver).switch_iframe()

    """
    点击菜单“客户管理-客户列表”，进入客户列表页面
    """
    def goto_guest_list(self):
        self.user_login_verify()
        js = "var q=document.getElementsByClassName('fakeloader')[0];q.style.display='none';"
        po = Guest(self.driver)
        po.script(js)
        po.click_text(Guest.guest_menu1_loc)
        po.click_text(Guest.guest_menu1_1_loc)
        time.sleep(5)
        po.switch_iframe()
        self.assertEqual(po.get_text(Guest.guest_list_page_title_loc), globalparam.GUEST_LIST_PAGE_TITLE)

    def read_table(self, keyword):
        table_rows = self.driver.find_element_by_tag_name('tr')
        # table_cols = self.driver.find_element_by_tag_name('td')
        for i in range(1, 11):
            name = table_rows[i].find_elements_by_tag_name('td')[0].text
            print "客户姓名：", name
            self.assertIn(keyword, name)

    """
    查询
    """
    def test_011_guest_search_01(self):
        self.goto_guest_list()
        # print "loc: ", Guest.guest_client_name_loc
        # print "keyword: ", read_guest_keyword_data(0, "keyname")
        po = Guest(self.driver)
        po.input_value(read_guest_keyword_data(1, "keyname"))
        po.click_text(Guest.guest_client_search_loc)
        self.read_table("li")
        """
        for i in range(4):
            po.input_value(read_guest_keyword_data(i, "keyname"))
            po.click_text(Guest.guest_client_search_loc)
            time.sleep(10)
            
            function.insert_img(self.driver, 'search_name%d.jpg' % i)
            time.sleep(5)
        """


if __name__ == "__main__":
    unittest.main()
