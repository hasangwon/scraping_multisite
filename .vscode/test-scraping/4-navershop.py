#version 1.0
import csv
from urllib.parse import quote_plus
from bs4 import BeautifulSoup
from selenium import webdriver
import glob
import time

hdr = {'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.36"}

# navershop crawling
print('DM SCRAPING..')
searchList = []

urlA = 'https://www.instagram.com/direct/t/340282366841710300949128116933970357106'
driver = webdriver.Chrome()
time.sleep(1)
driver.get(urlA)
driver.implicitly_wait(3000)

SCROLL_PAUSE_TIME = 2

    # Get scroll height
last_height = driver.execute_script("return document.body.scrollHeight")

while True:
    # Scroll down to bottom
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        # Wait to load page
    time.sleep(SCROLL_PAUSE_TIME)
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight-50);")
    time.sleep(SCROLL_PAUSE_TIME)
    # Calculate new scroll height and compare with last scroll height
    new_height = driver.execute_script("return document.body.scrollHeight")
    if new_height == last_height:
        break
    last_height = new_height

html = driver.page_source
soup = BeautifulSoup(html)
r = soup.select('div.basicList_info_area__17Xyo')
prdC = 0
searchList.append(['인스타 DM'])

for x in r:
    temp = []
    temp.append(prdC + 1)
    temp.append(x.select_one('div.Igw0E.IwRSH.eGOV_._4EzTm').text)     
    searchList.append(temp)
    prdC = prdC + 1
    if prdC == 30 : 
        break
driver.close()

f = open(f'./test-save/insta.csv', 'w', encoding='utf-8', newline='')
        
csvWriter = csv.writer(f)
for i in searchList:
    csvWriter.writerow(i)
            
f.close()
print('insta done')

  



  