#!/usr/bin/env python
# _*_ coding: utf-8 _*_
import csv
from crm.config import globalparam
import codecs

user_info_path = globalparam.CSV_USER_PATH
by_login_loc_path = globalparam.CSV_LOGIN_BY_PATH
by_home_loc_path = globalparam.CSV_HOME_BY_PATH
by_guest_loc_path = globalparam.CSV_GUEST_BY_PATH
guest_search_keyword_path = globalparam.CSV_GUEST_SEARCH_KEYWORD_PATH

"""
  获取账号密码数据csv文件中某单元格
"""


def read_user_data(i, param):
    with open(user_info_path, 'rb') as csv_file:
        print("path1:", user_info_path)
        reader = csv.DictReader(csv_file)
        rows = [row for row in reader]
    dict1 = rows[i]
    print(dict1[param])
    return dict1[param]


"""
 获取登录定位数据csv文件中某单元格
"""


def read_login_by_data(i):
    with open(by_login_loc_path, 'rb') as csv_file:
        print("path1:", by_login_loc_path)
        reader = csv.DictReader(csv_file)
        rows = [row for row in reader]
    dict1 = rows[i]
    print(dict1["location"])
    return dict1["location"]


"""
 获取首页定位数据csv文件中某单元格
"""


def read_home_by_data(i):
    with open(by_home_loc_path, 'rb') as csv_file:
        print("path1:", by_home_loc_path)
        reader = csv.DictReader(csv_file)
        rows = [row for row in reader]
    dict1 = rows[i]
    print(dict1["location"])
    return dict1["location"]


"""
 获取客户列表定位数据csv文件中某单元格
"""


def read_guest_by_data(i):
    with open(by_guest_loc_path, 'rb') as csv_file:
        print("path1:", by_guest_loc_path)
        reader = csv.DictReader(csv_file)
        rows = [row for row in reader]
    dict1 = rows[i]
    print(dict1["location"])
    return dict1["location"]


"""获取搜索关键词"""


def read_guest_keyword_data(i, param):
    # file1 = open(guest_search_keyword_path, 'rb')
    # print "行数：", len(file1.readlines())
    with open(guest_search_keyword_path, 'rb') as csv_file:
        print("path_key:", guest_search_keyword_path)
        reader = csv.DictReader(csv_file)
        rows = [row for row in reader]
    dict1 = rows[i]
    print(dict1[param])
    return dict1[param]
