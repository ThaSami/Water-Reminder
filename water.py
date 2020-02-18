from bs4 import BeautifulSoup
import requests
from selenium import webdriver 
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC 
from selenium.webdriver.common.keys import Keys 
from selenium.webdriver.common.by import By 
import time 
import random


# works only on whatsapp web
def sendmsg(msg):        
    msg_box = driver.find_element_by_class_name('_3u328')
    msg_box.send_keys(msg)
    button = driver.find_element_by_class_name('_3M-N-')
    button.click()

#### DATA SCRAPING ####
url = 'https://mawdoo3.com/%D9%81%D9%88%D8%A7%D8%A6%D8%AF_%D8%B4%D8%B1%D8%A8_%D8%A7%D9%84%D9%85%D8%A7%D8%A1_%D9%84%D9%84%D8%AC%D8%B3%D9%85'
response = requests.get(url)
soup  = BeautifulSoup(response.text,'lxml')
result = soup.find('div', {'class': 'mw-content-rtl'}).select('ul')[1].findChildren()

benefits = []
for child in result:
    if len(child.text)>40:	
    	benefits.append(child.text)
    
#### END OF DATA SCRAPING ####

### WHATSAPP MESSAGE SENDING ###

driver = webdriver.Chrome()
driver.get("https://web.whatsapp.com/") 

# Replace the below strings with Name of your targets on whatsapp
targets = ["X","Y","Z"]
hang = input("start?")

while 1:
    for target in targets:
        user = driver.find_element_by_xpath('//span[@title = "{}"]'.format(target))
        user.click()
        msg = random.choice(benefits) 
        sendmsg(msg)
    time.sleep(3600) #wait 1 hour
