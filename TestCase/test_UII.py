from  selenium import webdriver
import time

from selenium.webdriver.support.select import Select

driver=webdriver.Chrome("../chromedriver/chromedriver.exe")
driver.get("http://192.168.60.146:8080/demo1.html")
driver.find_element_by_xpath('//input[@type="text"]').clear()
time.sleep(2)
driver.find_element_by_xpath('//input[@type="text"]').send_keys('你好')
time.sleep(2)
driver.find_element_by_xpath('//input[@id="file1"]').clear()
driver.find_element_by_xpath('//input[@id="file1"]').send_keys('C:/Users/Administrator/Pictures')
time.sleep(2)
driver.find_element_by_xpath('//input[@type="radio"][1]').click()
driver.find_element_by_xpath('//input[@type="radio"][2]').click()
time.sleep(2)
driver.find_element_by_xpath('//input[@type="checkbox"][1]').click()
driver.find_element_by_xpath('//input[@type="checkbox"][2]').click()
driver.find_element_by_xpath('//input[@type="checkbox"][3]').click()
driver.find_element_by_xpath('//input[@type="button"]').click()
time.sleep(2)
driver.switch_to.alert.send_keys("不知道")
time.sleep(2)
# 警告框确定
driver.switch_to.alert.accept()
# 警告框取消
# driver.switch_to.alert.dismiss()
time.sleep(2)
driver.find_element_by_xpath('//input[@type="password"]').send_keys('123456')
driver.find_element_by_xpath('//input[@type="number"]').send_keys('123456')
driver.find_element_by_xpath('//textarea').send_keys('你是哪个')
# 下拉框操作
mm=driver.find_element_by_xpath('//select')
time.sleep(2)
Select(mm).select_by_value('z1')
time.sleep(2)
Select(mm).select_by_visible_text('周龙2')

time.sleep(2)
# 超链接操作
driver.find_element_by_link_text('问问度娘')
time.sleep(2)
# 后退
driver.back()
time.sleep(2)
# 前进
driver.forward()
time.sleep(2)
# 刷新
driver.refresh()
# 进入iframe框
driver.switch_to.frame('driver.find_element_by_xpath('')')
# 退出ifram框
driver.switch_to.default_content()


time.sleep(3)
driver.quit()


