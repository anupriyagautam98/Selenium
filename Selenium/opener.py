from selenium import webdriver 
import time
#1.1To open the chrome browser and navigate to “https://google.com”
driver = webdriver.Chrome()
driver.get("https://google.com") 
time.sleep(3)
driver.close()

#1.2To open the firefox browser and navigate to “https://google.com”
driver = webdriver.Firefox()
driver.get("https://google.com")
time.sleep(3)
driver.close()