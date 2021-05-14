import csv
from urllib.parse import quote_plus
from bs4 import BeautifulSoup
from selenium import webdriver
import glob
import time

hdr = {'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36"}

# 11st crawling
print('11st crawling')
searchList = []

urlA = 'https://www.11st.co.kr/browsing/DisplayCategory.tmall?method=getDisplayCategory1Depth&dispCtgrNo=1129478'
driver = webdriver.Chrome()
driver.implicitly_wait(3)
driver.get(urlA)
html = driver.page_source
soup = BeautifulSoup(html)
r = soup.select('.box_pd')
prdC = 0

searchList.append([' '])
searchList.append(['11번가'])
searchList.append(['과일'])
for x in r:
    temp = []
    temp.append(x.select_one('div.pname').text)   
    temp.append(x.select_one('strong.sale_price').num)     
    searchList.append(temp)
    prdC = prdC + 1
    if prdC == 10 : 
        break

driver.close()

urlB = 'https://www.11st.co.kr/browsing/DisplayCategory.tmall?method=getDisplayCategory1Depth&dispCtgrNo=1129477'  # site to crawl
driver = webdriver.Chrome()
driver.implicitly_wait(3)
driver.get(urlB)
html = driver.page_source
soup = BeautifulSoup(html)
r = soup.select('.box_pd')
prdC = 0   # items count

searchList.append(['야채'])
for x in r:
    temp = []
    temp.append(x.select_one('div.pname > p').text)   
    temp.append(x.select_one('strong.sale_price').num)     
    searchList.append(temp) #makes two-dimensional array
    prdC = prdC + 1
    if prdC == 10 : 
        break
driver.close()

f = open(f'./test-save/7-11st.csv', 'w', encoding='utf-8', newline='')
        
csvWriter = csv.writer(f)
for i in searchList:
    csvWriter.writerow(i)
            
f.close()
print('11st done')

  