from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
for i in range(100):
    driver=webdriver.Chrome('/usr/local/bin/chromedriver')
    driver.get("https://docs.google.com/forms/d/e/1FAIpQLScw9p6v-JrljvZcPjjuW5xdjj4r_w-DWfHqJ2N-3pB8fEKX2g/viewform?pli=1")
    time.sleep(1)
    
    element1=driver.find_element_by_css_selector("input.quantumWizTextinputPaperinputInput.exportInput")
    element1.send_keys("Anupriya")
    # element1.send_keys(Keys.RETURN)
    element2=driver.find_element_by_css_selector("textarea.quantumWizTextinputPapertextareaInput.exportTextarea")
    element2.send_keys("hi there")

    element3=driver.find_element_by_css_selector("span.appsMaterialWizButtonPaperbuttonLabel.quantumWizButtonPaperbuttonLabel.exportLabel")
    element3.click()
    driver.close