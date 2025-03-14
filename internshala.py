import os
import time
import pickle
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import requests
from bs4 import BeautifulSoup
os.environ['PATH'] += r"/home/advik/python/selenium/chromedriver_linux64 (1)"
driver = webdriver.Firefox()
driver.get("https://internshala.com/internships/android-app-development-internship/")
driver.maximize_window()
time.sleep(2)
driver.find_element(By.ID,'close_popup').click()
htm= driver.page_source
soup = BeautifulSoup(htm,"html.parser")

internlinks = []
time = []
for time in soup.find_all("i",class_="ic-16-calendar"):
    time 
for a_tag in soup.find_all("a", class_="job-title-href", href=True):
    full_link = "https://internshala.com" + a_tag["href"]  # Convert relative URL to absolute
    internlinks.append(full_link)

for link in internlinks:
    time.sleep(5)
    message = f"🔗 New Job Listing For Android Development \n Internshala: {link}"
    url = f"https://api.telegram.org/bot5086944407:AAGSvOf9K8mBipbkMDK6rfqwmcjtsGcNXcw/sendMessage"
    data = {"chat_id": -1002398388043, "text": message}
    response = requests.post(url, data=data)
    print(response.json())  
