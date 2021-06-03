#version 1.0
import csv
from urllib.parse import quote_plus
from bs4 import BeautifulSoup
from selenium import webdriver
import glob
import time

hdr = {'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36"}


# wemap crawling
print('wemap crawling')
searchList = []
urlB = 'https://front.wemakeprice.com/category/division/2100082'
driver = webdriver.Chrome()
driver.implicitly_wait(3)
driver.get(urlB)
time.sleep(2)
html = driver.page_source
soup = BeautifulSoup(html)
r = soup.select('#list_lists .list_conts_wrap')
prdC = 0
        
searchList.append([' '])
searchList.append(['위메프'])
searchList.append(['과일'])
for x in r:
    temp = []
    temp.append(prdC + 1)
    temp.append('위메프')
    temp.append(x.select_one('.option_txt .text').text)   
    temp.append(x.select_one('.option_txt .num').text)    
    searchList.append(temp)
    prdC = prdC + 1
    if prdC == 10 : 
        break

driver.close()

f = open(f'./test-save/3-wemap.csv', 'w', encoding='utf-8', newline='')
        
csvWriter = csv.writer(f)
for i in searchList:
    csvWriter.writerow(i)
            
f.close()
print('wemap done')
                    