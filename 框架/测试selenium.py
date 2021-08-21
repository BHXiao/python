import time
from selenium import webdriver
#  还要单独装浏览器的调用驱动

#  指定driver 的绝对路径，如果加入全局变量就不需要指定
# driver = webdriver.Chrome(executable_path='')
driver = webdriver.Chrome(executable_path='./chromedriver.exe')
driver.get('http://www.qiye.163.com/login/')
# print()
driver.find_element_by_id("switchNormalCtrl").click()   # 切换到用户名密码登陆
driver.find_element_by_id('accname').send_keys('ben.xiao@medcaptain.com')
driver.find_element_by_id('accpwd').send_keys('nihao,8090')
driver.find_element_by_class_name("loginbtn").click()   # 点击登陆
#  elements  怎么用？？
# driver.find_elements_by_xpath('//*[@id="loginBlock"]/div[2]/form[1]/div[5]/button').click()   # 点击登陆
# driver.find_element_by_xpath('//*[@id="loginBlock"]/div[2]/form[1]/div[5]/button').click()  # 点击登陆
# //*[@id="loginBlock"]/div[2]/form[1]/div[5]/button
# url = []
# url = driver.current_url()
# 打印页面的标题
# print(url)
print(driver.title)
driver.window

time.sleep(3)

# 退出模拟浏览器
# driver.quit()  # 一定要退出！不退出会有残留进程

