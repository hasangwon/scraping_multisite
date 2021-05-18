#version 1.0
import csv
from urllib.parse import quote_plus
from bs4 import BeautifulSoup
from selenium import webdriver
import time
from openpyxl import Workbook

hdr = {'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36"}

print('crawling start...')
searchList = []

# 맛다름
print('efc crawling..')
urlA = 'https://www.efc365.co.kr/product/list.html?cate_no=24'
driver = webdriver.Chrome()
driver.implicitly_wait(3)
driver.get(urlA)
html = driver.page_source
soup = BeautifulSoup(html)
r = soup.select('.description')
prdC = 0
        
searchList.append([' '])
searchList.append(['맛다름'])
searchList.append(['국산과일'])
for x in r:
    temp = []
    temp.append(prdC + 1)
    temp.append(x.select_one('p.name ').text)   
    temp.append(x.select_one('span.price.displaynone_sale.displaynone_custom').text)    
    searchList.append(temp)
    prdC = prdC + 1
    if prdC == 30 : 
        break
driver.close()
urlA = 'https://www.efc365.co.kr/product/list.html?cate_no=25'
driver = webdriver.Chrome()
driver.implicitly_wait(3)
driver.get(urlA)
html = driver.page_source
soup = BeautifulSoup(html)
r = soup.select('.description')
prdC = 0
        
searchList.append([' '])
searchList.append(['수입과일'])
for x in r:
    temp = []
    temp.append(prdC + 1)
    temp.append(x.select_one('p.name ').text)   
    temp.append(x.select_one('span.price.displaynone_sale.displaynone_custom').text)    
    searchList.append(temp)
    prdC = prdC + 1
    if prdC == 30 : 
        break
driver.close()
urlA = 'https://www.efc365.co.kr/product/list.html?cate_no=43'
driver = webdriver.Chrome()
driver.implicitly_wait(3)
driver.get(urlA)
html = driver.page_source
soup = BeautifulSoup(html)
r = soup.select('.description')
prdC = 0
        
searchList.append([' '])
searchList.append(['야채알뜰'])
for x in r:
    temp = []
    temp.append(prdC + 1)
    temp.append(x.select_one('p.name ').text)   
    temp.append(x.select_one('span.price.displaynone_sale.displaynone_custom').text)    
    searchList.append(temp)
    prdC = prdC + 1
    if prdC == 30 : 
        break
driver.close()
urlA = 'https://www.efc365.co.kr/product/list.html?cate_no=45'
driver = webdriver.Chrome()
driver.implicitly_wait(3)
driver.get(urlA)
html = driver.page_source
soup = BeautifulSoup(html)
r = soup.select('.description')
prdC = 0
        
searchList.append([' '])
searchList.append(['신선야채'])
for x in r:
    temp = []
    temp.append(prdC + 1)
    temp.append(x.select_one('p.name ').text)   
    temp.append(x.select_one('span.price.displaynone_sale.displaynone_custom').text)    
    searchList.append(temp)
    prdC = prdC + 1
    if prdC == 30 : 
        break
driver.close()
f = open(f'./test-save/testfile.csv', 'w', encoding='utf-8', newline='')
csvWriter = csv.writer(f)
for i in searchList:
    csvWriter.writerow(i)
f.close()
print('test done!')
