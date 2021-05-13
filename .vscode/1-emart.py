import csv
from urllib.parse import quote_plus
from bs4 import BeautifulSoup
from selenium import webdriver
import glob
import time

hdr = {'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36"}


print('emartmall crawling')
searchList = []

urlA = 'http://emart.ssg.com/category/main.ssg?dispCtgId=6000095739'  # site to crawl
driver = webdriver.Chrome()
driver.implicitly_wait(3)
driver.get(urlA)
html = driver.page_source
soup = BeautifulSoup(html)
r = soup.select('.cunit_t232')   #take source
prdC = 0   # items count
        
searchList.append([' '])
searchList.append(['이마트몰'])
searchList.append(['과일'])
for x in r:
    temp = []
    temp.append(x.select_one('div.title a > em.tx_ko').text)      #items 1
    temp.append(x.select_one('div.opt_price em.ssg_price').text)  #items 2
    searchList.append(temp) #makes two-dimensional array
    prdC = prdC + 1
    if prdC == 10 : 
        break

driver.close()

urlB = 'http://emart.ssg.com/category/main.ssg?dispCtgId=6000095740'  # site to crawl
driver = webdriver.Chrome()
driver.implicitly_wait(3)
driver.get(urlB)
html = driver.page_source
soup = BeautifulSoup(html)
r = soup.select('.cunit_t232')   #take source
prdC = 0   # items count

searchList.append(['야채'])
for x in r:
    temp = []
    temp.append(x.select_one('div.title a > em.tx_ko').text)      #items 1
    temp.append(x.select_one('div.opt_price em.ssg_price').text)  #items 2
    searchList.append(temp) #makes two-dimensional array
    prdC = prdC + 1
    if prdC == 10 : 
        break
    
driver.close()

f = open(f'./test-save/1-emart.csv', 'w', encoding='utf-8', newline='')
        
csvWriter = csv.writer(f)
for i in searchList:
    csvWriter.writerow(i)
            
f.close()
print('emart done')
