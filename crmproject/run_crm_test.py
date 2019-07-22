#!/usr/bin/env python
# _*_ coding: utf-8 _*_

from packages.HTMLTestRunnerCh import HTMLTestRunner
from email.mime.text import MIMEText
from email.header import Header
import smtplib
import unittest
import time
import os
import sys
reload(sys)
sys.setdefaultencoding('utf8')


def send_mail(file_new):
    f = open(file_new, 'rb')
    mail_body = f.read()
    f.close()

    msg = MIMEText(mail_body, 'html', 'utf-8')
    # msg = MIMEText('请查看附件内容！', 'plain', 'utf-8')
    msg['Subject'] = Header("自动化测试报告", 'utf-8')
    msg['From'] = '***<*****@163.com>'
    msg['To'] = '*******@qq.com'

    smtp = smtplib.SMTP()
    smtp.connect("smtp.163.com")
    smtp.login("******@163.com", "*********")
    smtp.sendmail('*******@163.com', '********8@qq.com', msg.as_string())
    smtp.quit()
    print("the email has send out!")


def new_report(report_dir):
    lists = os.listdir(report_dir)
    print(lists)
    lists.sort(key=lambda fn: os.path.getatime(report_dir + "\\" + fn))
    print("The latest report is:" + lists[-1])

    file_new = os.path.join(report_dir, lists[-1])
    print(file_new)
    return file_new


if __name__ == "__main__":
    now = time.strftime("%Y%m%d%H%M%S")
    filename = './crm/report/' + now + 'result.html'
    fp = open(filename, 'wb')
    runner = HTMLTestRunner(stream=fp, title=str('自动化测试报告'), description=str('环境: windows 7 浏览器: chrome'))
    discover = unittest.defaultTestLoader.discover('./crm/testcase/test_suit/', pattern='home_sta.py')
    runner.run(discover)
    fp.close()
    file_path = new_report('./crm/report/')
    send_mail(file_path)
