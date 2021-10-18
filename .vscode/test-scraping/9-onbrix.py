#version 1.0
import csv
from urllib.parse import quote_plus
from bs4 import BeautifulSoup
from selenium import webdriver
import glob
import time

hdr = {'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36"}

# onbrix crawling
print('onbrix crawling')
searchList = []

searchList.append([' '])
searchList.append(['온브릭스/국산과일'])
urlA = 'https://farmerstable.imweb.me/38'
driver = webdriver.Chrome()
time.sleep(2)
driver.get(urlA)
driver.implicitly_wait(3)

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
r = soup.select('.item-detail')
prdC = 0
for i in range(15) :
    temp = []
    try : 
        temp.append(prdC + 1)
        temp.append('온브릭스')
        temp.append(r[i].select_one('div.item-pay > h2').text.strip())   
        temp.append(r[i].select_one('div.item-pay > div.item-pay-detail > p.pay').text.strip())   
        searchList.append(temp) #makes two-dimensional array
    except IndexError as e :
        searchList.append(temp) #makes two-dimensional array
    prdC = prdC + 1
    if prdC == 15 : 
        break
driver.close()

urlB = 'https://farmerstable.imweb.me/39'  # site to crawl
driver = webdriver.Chrome()
driver.implicitly_wait(3)
driver.get(urlB)
html = driver.page_source
soup = BeautifulSoup(html)
r = soup.select('.item-detail')   #take source
prdC = 0   # items count

searchList.append(['온브릭스/수입과일'])
for i in range(15) :
    temp = []
    try : 
        temp.append(prdC + 1)
        temp.append('온브릭스')
        temp.append(r[i].select_one('div.item-pay > h2').text.strip())   
        temp.append(r[i].select_one('div.item-pay > div.item-pay-detail > p.pay').text.strip())   
        searchList.append(temp) #makes two-dimensional array
    except IndexError as e :
        searchList.append(temp) #makes two-dimensional array
    prdC = prdC + 1
    if prdC == 15 : 
        break
driver.close()

f = open(f'./test-save/9-onbrix.csv', 'w', encoding='utf-8', newline='')
        
csvWriter = csv.writer(f)
for i in searchList:
    csvWriter.writerow(i)
            
f.close()
print('onbrix done')

  