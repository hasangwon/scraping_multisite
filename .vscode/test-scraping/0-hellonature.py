#version 1.0
import csv
from urllib.parse import quote_plus
from bs4 import BeautifulSoup
from selenium import webdriver
import glob
import time

hdr = {'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.36"}

# hn crawling
print('HN SCRAPING..')
searchList = []

urlA = 'https://www.hellonature.co.kr/fdp001.do?goTo=dpItemList&gubunFlag=D&pageSize=60&filterYn=N&ctgrCd=020600&dpItemListCntYn=Y&page=1'
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
r = soup.select('div.info')
prdC = 0
searchList.append(['헬로네이처'])

for i in range(60) :
    temp = []
    try : 
        temp.append(prdC + 1)
        temp.append('헬로네이처')
        temp.append(r[i].select_one('div.name').text.strip())   
        temp.append(r[i].select_one('div.cost').text)    
        searchList.append(temp) #makes two-dimensional array
    except IndexError as e :
        searchList.append(temp)  
    prdC = prdC + 1
    if prdC == 60 : 
        break
driver.close()

f = open(f'./test-save/hellonature.csv', 'w', encoding='utf-8', newline='')
        
csvWriter = csv.writer(f)
for i in searchList:
    csvWriter.writerow(i)
            
f.close()
print('hn done')

  




  