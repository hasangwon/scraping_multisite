import csv
from urllib.parse import quote_plus
from bs4 import BeautifulSoup
from selenium import webdriver
import glob
import time

hdr = {'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36"}

# homeplus crawling
print('onbrix crawling')
searchList = []

urlA = 'https://front.homeplus.co.kr/list?categoryDepth=1&categoryId=100001'
driver = webdriver.Chrome()
driver.implicitly_wait(3)
driver.get(urlA)
html = driver.page_source
soup = BeautifulSoup(html)
r = soup.find_all('div')
prdC = 0
print(r)
searchList.append([' '])
searchList.append(['홈플러스'])
searchList.append(['과일'])
for x in r:
    temp = []
    temp.append(x.select_one('a.productTitle'))      
    searchList.append(temp)
    prdC = prdC + 1
    if prdC == 10 : 
        break

driver.close()

# urlB = 'https://farmerstable.imweb.me/39'  # site to crawl
# driver = webdriver.Chrome()
# driver.implicitly_wait(3)
# driver.get(urlB)
# html = driver.page_source
# soup = BeautifulSoup(html)
# r = soup.select('.item-detail')   #take source
# prdC = 0   # items count

# searchList.append(['수입과일'])
# for x in r:
#     temp = []
#     temp.append(x.select_one('div.item-pay > h2').text.strip())   
#     temp.append(x.select_one('a > div > div.item-pay-detail > p.pay').text.strip())     
#     searchList.append(temp) #makes two-dimensional array
#     prdC = prdC + 1
#     if prdC == 10 : 
#         break
# driver.close()

f = open(f'./test-save/9-homeplus.csv', 'w', encoding='utf-8', newline='')
        
csvWriter = csv.writer(f)
for i in searchList:
    csvWriter.writerow(i)
            
f.close()
print('homeplus done')

  