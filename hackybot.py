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



url = 'https://api.weather.gov/'

"headers = {myweatherapp.com contact@myweatherapp.com}"


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


def weather():

    a = requests.post(url, data={})
    
    if a.status_code == 200:
        print(a)


    # Read API endpoint and print it to terminal. After being given a state or zip


    
    pass


def chatbox_r():

    r_chatbox = driver.find_element(By.XPATH,"//div[@data-hook='log-contents']") # either here

    if "Exit room" in  r_chatbox.text:   # or here

        exit()
        

def exit():

    sleep(2)
    
    inputbox[0].send_keys("Exiting room, Goodbye")
    inputbox[0].send_keys(Keys.ENTER)
    sleep(2)

    driver.quit()
    
    pass


print(name)

name.send_keys("bot")

name.send_keys(Keys.ENTER)

driver.implicitly_wait(3)

# roomlist = driver.find_element(By.XPATH, "//span[.='bot test']")

j_btn = driver.find_element(By.XPATH, "//button[@data-hook='join']")

r_btn = driver.find_element(By.XPATH, "//button[@data-hook='refresh']")

x = 0
y = 0

while x < 1:
    
    roomlist = driver.find_elements(By.XPATH, "//span[.='test room']")
   

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

while y < 1:
    
    inputbox = driver.find_elements(By.XPATH, "//input[@data-hook='input']")

    if inputbox:
        print("Inputbox present")
        y = y + 2

    else:
        driver.implicitly_wait(3)
        sleep(1)
        print("refreshing")


# print(driver.find_element_by_id("signupModalButton").text)

inputbox[0].click()

while True:

    sleep (3)
    inputbox[0].send_keys("Hello! I am a bot in development... tell me something!")
    inputbox[0].send_keys(Keys.ENTER)
    #chatbox = driver.find_elements(By.CSS_SELECTOR,'p' )
    chatbox = driver.find_element(By.XPATH,"//div[@data-hook='log-contents']") 
    #chatbox = driver.find_elements(By.TAG_NAME, "p")
    
    chatbox_r()

    if "bot be quiet" in chatbox.text:
        sleep(2)
        inputbox[0].send_keys("Ok shutting up!")
        inputbox[0].send_keys(Keys.ENTER)
        break

while True:
    sleep(2)
    chatbox_r()

print(inputbox[0])

print(chatbox.text)


