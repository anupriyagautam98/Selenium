from selenium import webdriver
import time


driver = webdriver.Chrome('/usr/local/bin/chromedriver')
driver.get('https://testpages.herokuapp.com/styled/alerts/alert-test.html')
driver.maximize_window()

driver.find_element_by_xpath('//*[@id="alertexamples"]').click()
time.sleep(2)
action1 = driver.switch_to.alert
action1.accept()

time.sleep(1)
driver.find_element_by_xpath('//*[@id="confirmexample"]').click()
time.sleep(2)
action2 = driver.switch_to.alert
action2.accept()

time.sleep(2)

driver.find_element_by_xpath('//*[@id="promptexample"]').click()
action3 = driver.switch_to.alert
action3.send_keys('Anupriya')
time.sleep(2)
action3.accept()


time.sleep(3)
driver.close()