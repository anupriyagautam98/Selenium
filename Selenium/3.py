from selenium import webdriver
import time


driver = webdriver.Chrome('/usr/local/bin/chromedriver')
driver.get('https://testpages.herokuapp.com/styled/frames/frames-test.html')
driver.maximize_window()

time.sleep(2)

driver.switch_to.frame("middle")
middlelist = driver.find_element_by_css_selector('#middle3')
print(middlelist.text)

driver.switch_to.parent_frame()


driver.switch_to.frame("left")
leftlistitem6 = driver.find_element_by_css_selector('#left6')
print(leftlistitem6.text)

driver.switch_to.parent_frame()

driver.switch_to.frame("right")
rightlistitem0 = driver.find_element_by_css_selector('#right0')
print(rightlistitem0.text)

rightlistitem1 = driver.find_element_by_xpath('//*[@id="right1"]')
print(rightlistitem1.text)


time.sleep(2)
driver.close()
