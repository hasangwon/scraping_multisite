import csv
from urllib.parse import quote_plus
from bs4 import BeautifulSoup
from selenium import webdriver
import glob
import time
hdr = {'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36"}

# kurly crawling
print('kurly crawling')
searchList = []

urlA = 'https://www.kurly.com/shop/goods/goods_list.php?category=908006'
driver = webdriver.Chrome()
driver.implicitly_wait(3)
driver.get(urlA)
time.sleep(5)
html = driver.page_source
soup = BeautifulSoup(html)
r = soup.select('.info')
prdC = 0

searchList.append([' '])
searchList.append(['컬리'])
searchList.append(['과일'])
for x in r:
    temp = []
    temp.append(prdC + 1)
    temp.append(x.select_one('span.name').text.strip())   
    temp.append(x.select_one('span.cost span.price').text)    
    searchList.append(temp)
    prdC = prdC + 1
    if prdC == 10 : 
        break

driver.close()

urlB = 'https://www.kurly.com/shop/goods/goods_list.php?category=907'  # site to crawl
driver = webdriver.Chrome()
driver.implicitly_wait(3)
driver.get(urlB)
time.sleep(5)
html = driver.page_source
soup = BeautifulSoup(html)
r = soup.select('.info')   #take source
prdC = 0   # items count

searchList.append(['야채'])
for x in r:
    temp = []
    temp.append(x.index)
    temp.append(x.select_one('span.name').text.strip())   
    temp.append(x.select_one('span.cost span.price').text)    
    searchList.append(temp) #makes two-dimensional array
    prdC = prdC + 1
    if prdC == 10 : 
        break
driver.close()

f = open(f'./test-save/2-kurly.csv', 'w', encoding='utf-8', newline='')
        
csvWriter = csv.writer(f)
for i in searchList:
    csvWriter.writerow(i)
            
f.close()
print('kurly done')
