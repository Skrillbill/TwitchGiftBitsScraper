'''
Leaderboard Scraper - Screenshot Only
dev: SkrillBill 8-19-2021

REQUIREMENTS:
python 3.7+
selenium
webdriver-manager


'''

import requests
import shutil
import wget
import os
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from datetime import datetime




#first, lets update the chromedriver:

def update():
    url = 'https://googlechromelabs.github.io/chrome-for-testing/LATEST_RELEASE_STABLE'
    if(os.path.isfile('LATEST_RELEASE_STABLE')):
       os.remove('LATEST_RELEASE_STABLE')
    versionfile = wget.download(url)
    stableversion = open(versionfile,'r').read()

    url = 'https://edgedl.me.gvt1.com/edgedl/chrome/chrome-for-testing/' + stableversion + '/win64/chromedriver-win64.zip'
    if(os.path.isfile('chromedriver-win64.zip')):
        os.remove('chromedriver-win64.zip')
    stablerelease = wget.download(url)

    shutil.unpack_archive(stablerelease)

update()


#create our headless chrome instance and load the chat page
url = 'https://www.twitch.tv/popout/yourstreamerhere/chat'
chrome_options = webdriver.ChromeOptions()
#chrome_options.add_argument("--headless")
#CHANGE THE EXECUTABLE PATH HERE BELOW THIS LINE
chrome_service = Service('chromedriver-win64\chromedriver.exe')
driver= webdriver.Chrome(service=chrome_service)
driver.get(url)

#wait for initial page load
time.sleep(15)
#open the outfile
now = datetime.now()
timestamp = now.strftime("%Y-%m-%d_")
gifters = timestamp + "top_gifter.png"
bittys = timestamp + "top_bittys.png"
time.sleep(2)


#here we find the rotate leaderboard butotn and click it, expand it, screenshot it, rotate it again, and screenshot again.
rotate_button = driver.find_element("xpath",  '//*[@id="root"]/div/div[1]/div/div/section/div/div[1]/div/div/div/div/div/div/div[3]/button')
rotate_button.click()
time.sleep(2)

expand_sublb_button = driver.find_element("xpath", '/html/body/div[1]/div/div[1]/div/div/section/div/div[1]/div/div/div/div/div/div/div[2]/button')
expand_sublb_button.click()
time.sleep(2)
driver.get_screenshot_as_file('C:\\path\\to\\your\\folder\\here\\' + bittys)
time.sleep(2)

rotate_button = driver.find_element("xpath", '//*[@id="root"]/div/div[1]/div/div/section/div/div[1]/div/div/div/div/div/div[1]/div[2]/button')
rotate_button.click()
time.sleep(2)
#CHANGE OUTPUT DIRECTORY
driver.get_screenshot_as_file('C:\\path\\to\\your\\folder\\here\\' + gifters)

time.sleep(2)

driver.quit()
