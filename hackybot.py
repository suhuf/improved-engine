import requests
import re
import time 
from time import sleep as sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

options = Options()
options.add_experimental_option("detach", True)

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()),
                          options=options)

driver.get("https://www.haxball.com/play")

driver.implicitly_wait(6)

driver.switch_to.frame(0)


 # Grabs all anchor tags with the a tag attribute that have a link, convert this for haxball

name = driver.find_element(By.XPATH, "//input[@data-hook='input']")


password = 1  #automate this area so that if there is a password request prompt. if not nothing. 

            #ask for name input and also ask for room input

print(name)

name.send_keys("bot")

name.send_keys(Keys.ENTER)

driver.implicitly_wait(3)

# roomlist = driver.find_element(By.XPATH, "//span[.='bot test']")

j_btn = driver.find_element(By.XPATH, "//button[@data-hook='join']")

r_btn = driver.find_element(By.XPATH, "//button[@data-hook='refresh']")


x = 0

while x < 1:
    
    roomlist = driver.find_elements(By.XPATH, "//span[.='bot test']")

    if roomlist:
        roomlist[0].click()
        j_btn.click()
        
        x = x + 2
  
    else:
        driver.implicitly_wait(3)
        sleep(1)
        r_btn.click()
        print("refreshing")

pass_field = driver.find_elements(By.XPATH, "//input[@data-hook='input']")

if pass_field:
    
    pass_field[0].send_keys(password)

    pass_field[0].send_keys(Keys.ENTER)

#driver.switch_to.frame(driver.find_element(By.CSS_SELECTOR, "iframe.textarea[src='PwfmUfRI/__cache_static__/g/game.html']"))

#print(roomlist)

#for link in links:
    #print(link.get_attribute("innerHTML"))  # This one only gets links.


# element = driver.find_elements("css", 
   #                            '//input[@maxlength="25"]')

#print(len(element))

#name_input = driver.find_element_by_xpath('//input[@type="text"]')
#print(name_input.get_attribute('value'))
