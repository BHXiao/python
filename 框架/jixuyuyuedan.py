#!/usr/bin/env python
# -*- coding: utf-8 -*-
import datetime
from time import sleep
from selenium import webdriver
from selenium.webdriver.support.select import Select


# def qiangwei():

driver = webdriver.Chrome()
driver.get('https://ppt.mfa.gov.cn/appo/index.html')
# driver.maximize_window()
driver.find_element_by_xpath('//*[@id="body"]/div[9]/div[3]/div/button/span').click()
driver.find_element_by_link_text('继续未完成的申请预约').click()
sleep(0.1)
driver.find_element_by_id('recordNumberHuifu').send_keys('202106220186627')
Select(driver.find_element_by_id('questionIDHuifu')).select_by_value('1193724fcf8041a4b627467826ebd77b')
driver.find_element_by_id('answerHuifu').send_keys('liujie')
driver.find_element_by_xpath('//*[@id="body"]/div[5]/div[3]/div/button[1]/span').click()
sleep(0.5)
print(driver.current_url)
driver.find_element_by_id("myButton").click()
sleep(1)
while True:
    if len(driver.window_handles) == 2:
        print(driver.current_url)
        print(driver.window_handles)
        # driver.find_element_by_xpath('//*[@id="calendar"]/table/tbody/tr/td[3]/span').click()
        # driver.find_element_by_xpath('//*[@id="calendar"]/div/div/div[1]/div[3]/div').click()
        # sleep(0.5)
        # driver.switch_to.window(driver.window_handles[1])
        # driver.find_element_by_xpath('//*[@id="itable"]/tbody/tr[6]/td[5]/input').click()
        # a = driver.find_element_by_xpath('//*[@id="itable"]/tbody/tr[6]/td[5]/input')
        # print(a.text)
        # print(driver.page_source)

        # print(driver.current_url)
        # print(driver.window_handles)
        # //*[@id="calendar"]/div/div/div[1]/div[1]/div
        # //*[@id="calendar"]/div/div/div[1]/div[2]/div
        # //*[@id="calendar"]/div/div/div[1]/div[3]/div
        # //*[@id="calendar"]/div/div/div[1]/div[4]/div
        # //*[@id="calendar"]/div/div/div[1]/div[7]/div
        # //*[@id="calendar"]/div/div/div[1]/div[8]/div
        # //*[@id="calendar"]/div/div/div[1]/div[3]
        sleep(10)
        driver.quit()
#
# time = "2021-06-25 15:34:00"
# while True:
#     now = datetime.datetime.now()
#
#     if now.strftime('%Y-%m-%d %H:%M:%S') == time:
#         qiangwei()
#         break
