#version 1.0
import csv
from urllib.parse import quote_plus
from bs4 import BeautifulSoup
from selenium import webdriver
import glob
import time

hdr = {'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36"}
# coupang crawling
print('coupang crawling')
urlA = 'https://www.coupang.com/np/categories/194282'
searchList = []
driver = webdriver.Chrome()
driver.implicitly_wait(3)
driver.get(urlA)
html = driver.page_source
soup = BeautifulSoup(html)
r = soup.select('.baby-product-wrap')
prdC = 0
        
searchList.append([' '])
searchList.append(['쿠팡'])
searchList.append(['과일'])
for x in r:
    temp = []
    temp.append(x.select_one('.name').text.strip())   
    temp.append(x.select_one('.price-value').text.strip())    
    searchList.append(temp)
    prdC = prdC + 1
    if prdC == 10 : 
        break
                
driver.close()

urlB = 'https://www.coupang.com/np/categories/194432'  # site to crawl
driver = webdriver.Chrome()
driver.implicitly_wait(3)
driver.get(urlB)
html = driver.page_source
soup = BeautifulSoup(html)
r = soup.select('.baby-product-wrap')   #take source
prdC = 0   # items count

searchList.append(['야채'])
for x in r:
    temp = []
    temp.append(x.select_one('.name').text.strip())   
    temp.append(x.select_one('.price-value').text.strip())    
    searchList.append(temp) #makes two-dimensional array
    prdC = prdC + 1
    if prdC == 10 : 
        break
driver.close()

f = open(f'./test-save/4-coupang.csv', 'w', encoding='utf-8', newline='')
        
csvWriter = csv.writer(f)
for i in searchList:
    csvWriter.writerow(i)
            
f.close()
print('coupang done')
 