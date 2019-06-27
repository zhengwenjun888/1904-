from selenium import webdriver
from selenium.webdriver import ActionChains




import time
import os


driver_path = os.path.join(os.path.dirname(__file__),"../chromedriver/chromedriver.exe")
# 打开浏览器
driver = webdriver.Chrome(driver_path)
driver.maximize_window()  # 最大化浏览器
driver.set_page_load_timeout(10)#网页加载超时为10s
driver.set_script_timeout(10)#js脚本运行超时10s
driver.implicitly_wait(10)

driver.get('https://detail.damai.cn/item.htm?spm=a2oeg.home.card_0.ditem_2.591b23e120RG1L&id=595388025824')
driver.find_element_by_xpath('//div[@class="select_right_list_item sku_item active"]').click()
time.sleep(2)
driver.find_element_by_xpath('//a[@class="cafe-c-input-number-handler cafe-c-input-number-handler-up"]').click()
time.sleep(2)
driver.find_element_by_xpath('//div[contains(text(),"立即预定")]').click()
time.sleep(2)

driver.switch_to.frame(driver.find_element_by_xpath('//iframe[@id="alibaba-login-box"]'))
time.sleep(2)
driver.find_element_by_xpath('//div[contains(text(),"短信登录")]').click()
time.sleep(2)
driver.find_element_by_id('fm-sms-login-id').clear()
time.sleep(2)
driver.find_element_by_id('fm-sms-login-id').send_keys('15281016620')

driver.find_element_by_xpath('//a[@class="send-btn-link"]').click()
time.sleep(2)
# driver.find_element_by_xpath('//input[@placeholder="请输入手机号"]').clear()
# time.sleep(2)
# driver.find_element_by_xpath('//input[@placeholder="请输入手机号"]').send_keys('')
# time.sleep(2)
action=ActionChains(driver)
action.drag_and_drop(driver.find_element_by_xpath('//span[@id="nc_2_n1z"]'),
driver.find_element_by_xpath('//span[contains(text(),"请按住滑块，拖动到最右边")]')).perform()


time.sleep(2)
driver.quit()






