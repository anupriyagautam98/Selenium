from selenium import webdriver
import time


driver = webdriver.Chrome('/usr/local/bin/chromedriver')
driver.get('https://xndev.com/display-image/')

driver.maximize_window()

driver.find_element_by_xpath('//*[@id="post-2554"]/div/input').send_keys('/home/anupriya/Documents/Assignment/UI_Automation_Day4_Assessment/upload.txt')

time.sleep(10)
driver.close()
