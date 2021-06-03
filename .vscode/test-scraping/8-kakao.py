#version 1.0
import csv
from urllib.parse import quote_plus
from bs4 import BeautifulSoup
from selenium import webdriver
import time
from openpyxl import Workbook

hdr = {'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36"}

count = ['test']

for i in count:
    # emartmall crawling
    if i == 'test':
        print('crawling start')
        searchList = []

        urlA = 'https://store.kakao.com/category/3/102104103?level=2'  # site to crawl
        driver = webdriver.Chrome()
        driver.implicitly_wait(3)
        driver.get(urlA)
        time.sleep(2)
        html = driver.page_source
        soup = BeautifulSoup(html)
        r = soup.select('.link_product')   #take source
        prdC = 0   # items count
        
        searchList.append([' '])
        searchList.append(['카카오쇼핑'])
        searchList.append(['과일'])
        for x in r:
            temp = []
            try : 
                temp.append(prdC + 1)
                temp.append(x.select_one('.product_name').text)   #items 1
                temp.append(x.select_one('.txt_number.ng-star-inserted').text)  #items 2
                temp.append('카카오쇼핑')
                searchList.append(temp) #makes two-dimensional array
            except AttributeError as e :
                temp.append('err')   #items 1
                temp.append('카카오쇼핑')
                searchList.append(temp) #makes two-dimensional array
            prdC = prdC + 1
            if prdC == 30 : 
                break
        driver.close()
        
        f = open(f'./test-save/testfile.csv', 'w', encoding='utf-8', newline='')
        csvWriter = csv.writer(f)
        for i in searchList:
            csvWriter.writerow(i)
        f.close()
        print('done')
