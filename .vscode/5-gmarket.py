#version 1.0
import csv
from urllib.parse import quote_plus
from bs4 import BeautifulSoup
from selenium import webdriver
import glob
import time

hdr = {'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36"}


    # gmarket crawling
print('gmarket crawling')
urlA = 'http://browse.gmarket.co.kr/list?category=200000482'
searchList = []
driver = webdriver.Chrome()
driver.implicitly_wait(3)
driver.get(urlA)
html = driver.page_source
soup = BeautifulSoup(html)
r = soup.select('.box__information-major')
prdC = 0
        
searchList.append([' '])
searchList.append(['지마켓'])
searchList.append(['과일'])
for x in r:
    temp = []
    temp.append(x.select_one('span.text__item').attrs['title'])   
    temp.append(x.select_one('strong.text.text__value').text)    
    searchList.append(temp)
    prdC = prdC + 1
    if prdC == 10 : 
        break

driver.close()

urlB = 'http://browse.gmarket.co.kr/list?category=200001215'  # site to crawl
driver = webdriver.Chrome()
driver.implicitly_wait(3)
driver.get(urlB)
html = driver.page_source
soup = BeautifulSoup(html)
r = soup.select('.box__information-major')   #take source
prdC = 0   # items count

searchList.append(['야채'])
for x in r:
    temp = []
    temp.append(x.select_one('span.text__item').attrs['title'])   
    temp.append(x.select_one('strong.text.text__value').text)    
    searchList.append(temp) #makes two-dimensional array
    prdC = prdC + 1
    if prdC == 10 : 
        break
driver.close()

f = open(f'./test-save/5-gmarket.csv', 'w', encoding='utf-8', newline='')
        
csvWriter = csv.writer(f)
for i in searchList:
    csvWriter.writerow(i)
            
f.close()
print('gmarket done')

                    