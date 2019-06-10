from selenium import webdriver
import time
import os



driver_path = os.path.join(os.path.dirname(__file__),"../chromedriver/chromedriver.exe")
# 打开浏览器
driver = webdriver.Chrome(driver_path)
driver.maximize_window()  # 最大化浏览器
driver.set_page_load_timeout(10)#网页加载超时为10s
driver.set_script_timeout(10)#js脚本运行超时10s
driver.implicitly_wait(10)

driver.get('http://192.168.60.146:8080/demo1.html')
driver.find_element_by_xpath('//input[@type="text"]').clear()
time.sleep(2)
driver.find_element_by_xpath('//input[@type="text"]').send_keys('你好')
time.sleep(5)


driver.quit()






