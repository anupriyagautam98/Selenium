from selenium import webdriver 
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
import time

driver = webdriver.Chrome() 
driver.maximize_window()
driver.get("https://bonigarcia.dev/selenium-webdriver-java/web-form.html")
print(driver.current_url)

element1=driver.find_element(By.XPATH,'/html/body/main/div/div[1]/div[1]/h1')
print(element1.text)

element2=driver.find_element(By.XPATH,'/html/body/main/div/form/div/div[1]/label[1]')
element2.send_keys("test Data")

element3=driver.find_element(By.XPATH,'/html/body/main/div/form/div/div[1]/label[3]')
element3.send_keys("123,Sector 62, Noida")

element4=driver.find_element(By.ID,'my-radio-1')
print(element4.is_selected(),end=' ')
print("And",end=' ')
print(element4.get_attribute("checked"))

element5=driver.find_element(By.XPATH,'/html/body/main/div/form/div/div[3]/label[2]')
print(element5.is_displayed())


action = ActionChains(driver) 
driver.execute_script('window.scrollTo(0,document.body.scrollHeight);')
source=driver.find_element_by_xpath("/html/body/main/div/form/div/div[1]/label[5]/input")
time.sleep(1)
action.context_click(source).perform()


script='window.open("https://google.com","_blank")'
driver.execute_async_script(script)
driver.close()

