import csv
from urllib.parse import quote_plus
from bs4 import BeautifulSoup
from selenium import webdriver
import glob
import time

hdr = {'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36"}

# navershop crawling
print('naver crawling')
searchList = []

urlA = 'https://search.shopping.naver.com/search/category?catId=50000960'
driver = webdriver.Chrome()
driver.implicitly_wait(3)
time.sleep(5)
driver.get(urlA)
html = driver.page_source
soup = BeautifulSoup(html)
r = soup.select('li.basicList_item__2XT81.ad')
prdC = 0

searchList.append([' '])
searchList.append(['네이버쇼핑'])
searchList.append(['과일'])
for x in r:
    temp = []
    temp.append(x.select_one('a.basicList_link__1MaTN').text)   
    temp.append(x.select_one('span span.price_num__2WUXn').text)     
    searchList.append(temp)
    prdC = prdC + 1
    if prdC == 10 : 
        break

driver.close()

urlB = 'https://search.shopping.naver.com/search/category?catId=50001077'  # site to crawl
driver = webdriver.Chrome()
driver.implicitly_wait(3)
driver.get(urlB)
time.sleep(5)
html = driver.page_source
soup = BeautifulSoup(html)
r = soup.select('li.basicList_item__2XT81.ad')   #take source
prdC = 0   # items count

searchList.append(['야채'])
for x in r:
    temp = []
    temp.append(x.select_one('a.basicList_link__1MaTN').text)   
    temp.append(x.select_one('span span.price_num__2WUXn').text)     
    searchList.append(temp) #makes two-dimensional array
    prdC = prdC + 1
    if prdC == 10 : 
        break
driver.close()

f = open(f'./test-save/8-navershop.csv', 'w', encoding='utf-8', newline='')
        
csvWriter = csv.writer(f)
for i in searchList:
    csvWriter.writerow(i)
            
f.close()
print('navershop done')

  