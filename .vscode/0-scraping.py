import csv
from urllib.parse import quote_plus
from bs4 import BeautifulSoup
from selenium import webdriver
import glob
import time

hdr = {'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36"}

count = ['emart','kurly','wemap','coupang','gmarket']

for i in count:
    # emartmall crawling
    if i == 'emart':
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

        f = open(f'./save/1-emart.csv', 'w', encoding='utf-8', newline='')
        
        csvWriter = csv.writer(f)
        for i in searchList:
            csvWriter.writerow(i)
            
        f.close()
        driver.close()
        print('emart done')

    # kurly crawling
    elif i == 'kurly' : 
        print('kurly crawling')
        searchList = []

        urlA = 'https://www.kurly.com/shop/goods/goods_list.php?category=908'
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
            temp.append(x.select_one('span.name').text.strip())   
            temp.append(x.select_one('span.cost span.price').text)    
            searchList.append(temp) #makes two-dimensional array
            prdC = prdC + 1
            if prdC == 10 : 
                break

        f = open(f'./save/2-kurly.csv', 'w', encoding='utf-8', newline='')
        
        csvWriter = csv.writer(f)
        for i in searchList:
            csvWriter.writerow(i)
            
        f.close()
        driver.close()
        print('kurly done')

    # wemap crawling
    elif i == 'wemap' : 
        print('wemap crawling')
        urlA = 'https://front.wemakeprice.com/category/division/2100082'
        searchList = []
        driver = webdriver.Chrome()
        driver.implicitly_wait(3)
        driver.get(urlA)
        html = driver.page_source
        soup = BeautifulSoup(html)
        r = soup.select('.list_conts_wrap')
        prdC = 0
        
        searchList.append([' '])
        searchList.append(['위메프'])
        searchList.append(['과일'])
        for x in r:
            temp = []
            temp.append(x.select_one('.option_txt .text').text)   
            temp.append(x.select_one('.option_txt .num').text)    
            searchList.append(temp)
            prdC = prdC + 1
            if prdC == 10 : 
                break

        driver.close()

        urlB = 'https://front.wemakeprice.com/category/division/2100085'  # site to crawl
        driver = webdriver.Chrome()
        driver.implicitly_wait(3)
        driver.get(urlB)
        html = driver.page_source
        soup = BeautifulSoup(html)
        r = soup.select('.list_conts_wrap')   #take source
        prdC = 0   # items count

        searchList.append(['야채'])
        for x in r:
            temp = []
            temp.append(x.select_one('.option_txt .text').text)   
            temp.append(x.select_one('.option_txt .num').text)    
            searchList.append(temp) #makes two-dimensional array
            prdC = prdC + 1
            if prdC == 10 : 
                break

        f = open(f'./save/3-wemap.csv', 'w', encoding='utf-8', newline='')
        
        csvWriter = csv.writer(f)
        for i in searchList:
            csvWriter.writerow(i)
            
        f.close()
        driver.close()
        print('wemap done')
                    

    # coupang crawling
    elif i == 'coupang' : 
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

        f = open(f'./save/4-coupang.csv', 'w', encoding='utf-8', newline='')
        
        csvWriter = csv.writer(f)
        for i in searchList:
            csvWriter.writerow(i)
            
        f.close()
        driver.close()
        print('coupang done')
                    
    # gmarket crawling
    elif i == 'gmarket' : 
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

        f = open(f'./save/5-gmarket.csv', 'w', encoding='utf-8', newline='')
        
        csvWriter = csv.writer(f)
        for i in searchList:
            csvWriter.writerow(i)
            
        f.close()
        driver.close()
        print('gmarket done')

    else :
        print('word error!')
                    
# csv file merge
path = 'C:/PROJECTS/scraping_multisite/save/' #csv files route
merge_path = 'C:/PROJECTS/scraping_multisite/crawl_data.csv' #save file

file_list = glob.glob(path + '*')  # file check

with open(merge_path, 'w') as f: # merge file open
    for file in file_list:
        with open(file ,'rt', encoding='utf-8') as f2:
            while True:
                line = f2.readline() 

                if not line: 
                    break

                f.write(line) # write save file
                
        file_name = file.split('\\')[-1]
        print(file.split('\\')[-1] + 'write one')

print('>>making save file done')
