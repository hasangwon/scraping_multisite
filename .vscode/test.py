import csv
from urllib.parse import quote_plus
from bs4 import BeautifulSoup
from selenium import webdriver
import glob
import time

hdr = {'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36"}

print('test crawling')
searchList = []

url = 'https://www.efc365.co.kr/product/list.html?cate_no=69'  # site to crawl
driver = webdriver.Chrome()
driver.implicitly_wait(3)
driver.get(url)
html = driver.page_source
soup = BeautifulSoup(html)
r = soup.select('.description')   #take source
prdC = 0   # items count
        
searchList.append([' '])
searchList.append(['맛다름'])
searchList.append(['전체보기 10개'])
for x in r:
    temp = []
    temp.append(x.select_one('.name').text)      #items 1
    temp.append(x.select_one('div.price_area span.price').text)  #items 2
    searchList.append(temp) #makes two-dimensional array
    prdC = prdC + 1
    if prdC == 10 : 
        break

driver.close()

f = open(f'./test-save/result.csv', 'w', encoding='utf-8', newline='')
        
csvWriter = csv.writer(f)
for i in searchList:
    csvWriter.writerow(i)
            
f.close()
print('test done')