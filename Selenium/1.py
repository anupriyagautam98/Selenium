from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.support.ui import Select 
from selenium.webdriver.common.action_chains import ActionChains


driver = webdriver.Chrome()
driver.get('https://bonigarcia.dev/selenium-webdriver-java/web-form.html')


time.sleep(3)

elem1 =  Select(driver.find_element_by_xpath('/html/body/main/div/form/div/div[2]/label[1]/select'))
options = elem1.options
for i in options:
    print(i.text)

elem1.select_by_visible_text('Two')

if(driver.find_element_by_xpath('//*[@id="my-check-1"]').is_enabled()):
    driver.find_element_by_xpath('//*[@id="my-check-1"]').click()

time.sleep(2)

driver.execute_script('window.scrollTo(0,document.body.scrollHeight);')

driver.find_element_by_xpath('//*[@id="my-check-2"]').click()
time.sleep(1)
driver.find_element_by_xpath('//*[@id="my-radio-2"]').click()
time.sleep(2)

elem2 = driver.find_element_by_xpath('/html/body/main/div/form/div/div[3]/label[3]')
move = ActionChains(driver)
move.click_and_hold(elem2).move_by_offset(40, 0).release().perform()
time.sleep(2)
driver.maximize_window()

time.sleep(2)
driver.save_screenshot('/home/anupriya/Documents/Assignment/UI_Automation_Day4_Assessment/output.png')

time.sleep(2)
driver.close()