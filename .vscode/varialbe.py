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

print('crawling..')
url = 'https://www.11st.co.kr/browsing/DisplayCategory.tmall?method=getDisplayCategory1Depth&dispCtgrNo=1129478'
driver = webdriver.Chrome()
driver.get(url)
driver.implicitly_wait(3)

SCROLL_PAUSE_TIME = 2

last_height = driver.execute_script("return document.body.scrollHeight")
while True:
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(SCROLL_PAUSE_TIME)
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight-50);")
    time.sleep(SCROLL_PAUSE_TIME)
    new_height = driver.execute_script("return document.body.scrollHeight")
    if new_height == last_height:
        break
    last_height = new_height
    
html = driver.page_source
soup = BeautifulSoup(html)
r = soup.select('div.pname')
prdC = 0

searchList.append(['test'])

for x in r:
    temp = []
    temp.append(prdC + 1)
    temp.append('11st')
    temp.append(x.select_one('.pname p').text)   
    temp.append(x.select_one('strong.sale_price').text)    
    searchList.append(temp)
    prdC = prdC + 1
    if prdC == 10:
        break

driver.close()

f = open(f'./test-save/testfile.csv', 'w', encoding='utf-8', newline='')
csvWriter = csv.writer(f)
for i in searchList:
    csvWriter.writerow(i)
f.close()
print('test done!')




# import csv
# from urllib.parse import quote_plus
# from bs4 import BeautifulSoup
# from selenium import webdriver
# import glob
# import time
# from openpyxl import Workbook

# hdr = {'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36"}

# count = ['emart','kurly','wemap','coupang','gmarket','kakao','onbrix']

# for i in count:
#     # emartmall crawling
#     if i == 'emart':
#         print('emartmall crawling')
#         searchList = []

#         urlA = 'http://emart.ssg.com/category/main.ssg?dispCtgId=6000095739'  # site to crawl
#         driver = webdriver.Chrome()
#         driver.implicitly_wait(3)
#         driver.get(urlA)
#         html = driver.page_source
#         soup = BeautifulSoup(html)
#         r = soup.select('.cunit_t232')   #take source
#         prdC = 0   # items count
        
#         searchList.append([' '])
#         searchList.append(['이마트몰'])
#         searchList.append(['과일'])
#         for x in r:
#             temp = []
#             temp.append(prdC + 1)
#             temp.append(x.select_one('div.title a > em.tx_ko').text)      #items 1
#             temp.append(x.select_one('div.opt_price em.ssg_price').text)  #items 2
#             searchList.append(temp) #makes two-dimensional array
#             prdC = prdC + 1
#             if prdC == 30 : 
#                 break

#         driver.close()

#         urlB = 'http://emart.ssg.com/category/main.ssg?dispCtgId=6000095740'  # site to crawl
#         driver = webdriver.Chrome()
#         driver.implicitly_wait(3)
#         driver.get(urlB)
#         html = driver.page_source
#         soup = BeautifulSoup(html)
#         r = soup.select('.cunit_t232')   #take source
#         prdC = 0   # items count

#         searchList.append(['야채'])
#         for x in r:
#             temp = []
#             temp.append(prdC + 1)
#             temp.append(x.select_one('div.title a > em.tx_ko').text)      #items 1
#             temp.append(x.select_one('div.opt_price em.ssg_price').text)  #items 2
#             searchList.append(temp) #makes two-dimensional array
#             prdC = prdC + 1
#             if prdC == 30 : 
#                 break
#         driver.close()

#         f = open(f'./save/1-emart.csv', 'w', encoding='utf-8', newline='')
        
#         csvWriter = csv.writer(f)
#         for i in searchList:
#             csvWriter.writerow(i)
            
#         f.close()
#         print('emart done')

#     # kurly crawling
#     elif i == 'kurly' : 
#         print('kurly crawling')
#         searchList = []

#         urlA = 'https://www.kurly.com/shop/goods/goods_list.php?category=908006'
#         driver = webdriver.Chrome()
#         driver.implicitly_wait(3)
#         driver.get(urlA)
#         time.sleep(5)
#         html = driver.page_source
#         soup = BeautifulSoup(html)
#         r = soup.select('.info')
#         prdC = 0

#         searchList.append([' '])
#         searchList.append(['컬리'])
#         searchList.append(['과일'])
#         for x in r:
#             temp = []
#             temp.append(prdC + 1)
#             temp.append(x.select_one('span.name').text.strip())   
#             temp.append(x.select_one('span.cost span.price').text)    
#             searchList.append(temp)
#             prdC = prdC + 1
#             if prdC == 30 : 
#                 break

#         driver.close()

#         urlB = 'https://www.kurly.com/shop/goods/goods_list.php?category=907'  # site to crawl
#         driver = webdriver.Chrome()
#         driver.implicitly_wait(3)
#         driver.get(urlB)
#         time.sleep(5)
#         html = driver.page_source
#         soup = BeautifulSoup(html)
#         r = soup.select('.info')   #take source
#         prdC = 0   # items count

#         searchList.append(['야채'])
#         for x in r:
#             temp = []
#             temp.append(prdC + 1)
#             temp.append(x.select_one('span.name').text.strip())   
#             temp.append(x.select_one('span.cost span.price').text)    
#             searchList.append(temp) #makes two-dimensional array
#             prdC = prdC + 1
#             if prdC == 30 : 
#                 break
#         driver.close()

#         f = open(f'./save/2-kurly.csv', 'w', encoding='utf-8', newline='')
        
#         csvWriter = csv.writer(f)
#         for i in searchList:
#             csvWriter.writerow(i)
            
#         f.close()
#         print('kurly done')

#     # wemap crawling
#     elif i == 'wemap' : 
#         print('wemap crawling')
#         urlA = 'https://front.wemakeprice.com/category/division/2100082'
#         searchList = []
#         driver = webdriver.Chrome()
#         driver.implicitly_wait(3)
#         driver.get(urlA)
#         html = driver.page_source
#         soup = BeautifulSoup(html)
#         r = soup.select('.list_conts_wrap')
#         prdC = 0
        
#         searchList.append([' '])
#         searchList.append(['위메프'])
#         searchList.append(['과일'])
#         for x in r:
#             temp = []
#             temp.append(prdC + 1)
#             temp.append(x.select_one('.option_txt .text').text)   
#             temp.append(x.select_one('.option_txt .num').text)    
#             searchList.append(temp)
#             prdC = prdC + 1
#             if prdC == 30 : 
#                 break

#         driver.close()

#         urlB = 'https://front.wemakeprice.com/category/division/2100085'  # site to crawl
#         driver = webdriver.Chrome()
#         driver.implicitly_wait(3)
#         driver.get(urlB)
#         html = driver.page_source
#         soup = BeautifulSoup(html)
#         r = soup.select('.list_conts_wrap')   #take source
#         prdC = 0   # items count

#         searchList.append(['야채'])
#         for x in r:
#             temp = []
#             temp.append(prdC + 1)
#             temp.append(x.select_one('.option_txt .text').text)   
#             temp.append(x.select_one('.option_txt .num').text)    
#             searchList.append(temp) #makes two-dimensional array
#             prdC = prdC + 1
#             if prdC == 30 : 
#                 break
#         driver.close()

#         f = open(f'./save/3-wemap.csv', 'w', encoding='utf-8', newline='')
        
#         csvWriter = csv.writer(f)
#         for i in searchList:
#             csvWriter.writerow(i)
            
#         f.close()
#         print('wemap done')
                    

#     # coupang crawling
#     elif i == 'coupang' : 
#         print('coupang crawling')
#         urlA = 'https://www.coupang.com/np/categories/194282'
#         searchList = []
#         driver = webdriver.Chrome()
#         driver.implicitly_wait(3)
#         driver.get(urlA)
#         html = driver.page_source
#         soup = BeautifulSoup(html)
#         r = soup.select('.baby-product-wrap')
#         prdC = 0
        
#         searchList.append([' '])
#         searchList.append(['쿠팡'])
#         searchList.append(['과일'])
#         for x in r:
#             temp = []
#             temp.append(prdC + 1)
#             temp.append(x.select_one('.name').text.strip())   
#             temp.append(x.select_one('.price-value').text.strip())    
#             searchList.append(temp)
#             prdC = prdC + 1
#             if prdC == 30 : 
#                 break
                
#         driver.close()

#         urlB = 'https://www.coupang.com/np/categories/194432'  # site to crawl
#         driver = webdriver.Chrome()
#         driver.implicitly_wait(3)
#         driver.get(urlB)
#         html = driver.page_source
#         soup = BeautifulSoup(html)
#         r = soup.select('.baby-product-wrap')   #take source
#         prdC = 0   # items count

#         searchList.append(['야채'])
#         for x in r:
#             temp = []
#             temp.append(prdC + 1)
#             temp.append(x.select_one('.name').text.strip())   
#             temp.append(x.select_one('.price-value').text.strip())    
#             searchList.append(temp) #makes two-dimensional array
#             prdC = prdC + 1
#             if prdC == 30 : 
#                 break
#         driver.close()

#         f = open(f'./save/4-coupang.csv', 'w', encoding='utf-8', newline='')
        
#         csvWriter = csv.writer(f)
#         for i in searchList:
#             csvWriter.writerow(i)
            
#         f.close()
#         print('coupang done')
                    
#     # gmarket crawling
#     elif i == 'gmarket' : 
#         print('gmarket crawling')
#         urlA = 'http://browse.gmarket.co.kr/list?category=200000482'
#         searchList = []
#         driver = webdriver.Chrome()
#         driver.implicitly_wait(3)
#         driver.get(urlA)
#         html = driver.page_source
#         soup = BeautifulSoup(html)
#         r = soup.select('.box__information-major')
#         prdC = 0
        
#         searchList.append([' '])
#         searchList.append(['지마켓'])
#         searchList.append(['과일'])
#         for x in r:
#             temp = []
#             temp.append(prdC + 1)
#             temp.append(x.select_one('span.text__item').attrs['title'])   
#             temp.append(x.select_one('strong.text.text__value').text)    
#             searchList.append(temp)
#             prdC = prdC + 1
#             if prdC == 30 : 
#                 break

#         driver.close()

#         urlB = 'http://browse.gmarket.co.kr/list?category=200001215'  # site to crawl
#         driver = webdriver.Chrome()
#         driver.implicitly_wait(3)
#         driver.get(urlB)
#         html = driver.page_source
#         soup = BeautifulSoup(html)
#         r = soup.select('.box__information-major')   #take source
#         prdC = 0   # items count

#         searchList.append(['야채'])
#         for x in r:
#             temp = []
#             temp.append(prdC + 1)
#             temp.append(x.select_one('span.text__item').attrs['title'])   
#             temp.append(x.select_one('strong.text.text__value').text)    
#             searchList.append(temp) #makes two-dimensional array
#             prdC = prdC + 1
#             if prdC == 30 : 
#                 break
#         driver.close()

#         f = open(f'./save/5-gmarket.csv', 'w', encoding='utf-8', newline='')
        
#         csvWriter = csv.writer(f)
#         for i in searchList:
#             csvWriter.writerow(i)
            
#         f.close()
#         print('gmarket done')

#     #kakao
#     elif i == 'kakao':
#         print('kakao crawling')
#         searchList = []

#         urlA = 'https://store.kakao.com/category/3/102104103?level=2'  # site to crawl
#         driver = webdriver.Chrome()
#         driver.implicitly_wait(3)
#         driver.get(urlA)
#         time.sleep(2)
#         html = driver.page_source
#         soup = BeautifulSoup(html)
#         r = soup.select('.link_item')   #take source
#         prdC = 0   # items count
        
#         searchList.append([' '])
#         searchList.append(['카카오쇼핑'])
#         searchList.append(['과일'])
#         for x in r:
#             temp = []
#             try : 
#                 temp.append(prdC + 1)
#                 temp.append(x.select_one('span.txt_item.ng-star-inserted').text)   #items 1
#                 temp.append(x.select_one('span.txt_price.ng-star-inserted').text)  #items 2
#                 searchList.append(temp) #makes two-dimensional array
#             except AttributeError as e :
#                 temp.append(x.select_one('em.emph_viral.ng-star-inserted').text)   #items 1
#                 searchList.append(temp) #makes two-dimensional array
#             prdC = prdC + 1
#             if prdC == 30 : 
#                 break
#         driver.close()

#         urlB = 'https://store.kakao.com/category/3/102104101?level=2'  # site to crawl
#         driver = webdriver.Chrome()
#         driver.implicitly_wait(3)
#         driver.get(urlB)
#         html = driver.page_source
#         soup = BeautifulSoup(html)
#         r = soup.select('.link_item')   #take source
#         prdC = 0   # items count

#         searchList.append(['농산물'])
#         for x in r:
#             temp = []
#             try : 
#                 temp.append(prdC + 1)
#                 temp.append(x.select_one('span.txt_item.ng-star-inserted').text)   #items 1
#                 temp.append(x.select_one('span.txt_price.ng-star-inserted').text)  #items 2
#                 searchList.append(temp) #makes two-dimensional array
#             except AttributeError as e :
#                 temp.append(x.select_one('em.emph_viral.ng-star-inserted').text)   #items 1
#                 searchList.append(temp) #makes two-dimensional array
#             prdC = prdC + 1
#             if prdC == 30 : 
#                 break
#         driver.close()
        
#         f = open(f'./save/8-kakao.csv', 'w', encoding='utf-8', newline='')
#         csvWriter = csv.writer(f)
#         for i in searchList:
#             csvWriter.writerow(i)
#         f.close()
#         print('kako done')
    
#         # onbrix crawling
#     elif i == 'onbrix' :
#         print('onbrix crawling')
#         searchList = []

#         urlA = 'https://farmerstable.imweb.me/38'
#         driver = webdriver.Chrome()
#         driver.implicitly_wait(3)
#         driver.get(urlA)
#         html = driver.page_source
#         soup = BeautifulSoup(html)
#         r = soup.select('.item-detail')
#         prdC = 0

#         searchList.append([' '])
#         searchList.append(['온브릭스'])
#         searchList.append(['국산과일'])
#         for x in r:
#             temp = []
#             temp.append(prdC + 1)
#             temp.append(x.select_one('div.item-pay > h2').text.strip())   
#             temp.append(x.select_one('a > div > div.item-pay-detail > p.pay').text.strip())     
#             searchList.append(temp)
#             prdC = prdC + 1
#             if prdC == 15 : 
#                 break

#         driver.close()

#         urlB = 'https://farmerstable.imweb.me/39'  # site to crawl
#         driver = webdriver.Chrome()
#         driver.implicitly_wait(3)
#         driver.get(urlB)
#         html = driver.page_source
#         soup = BeautifulSoup(html)
#         r = soup.select('.item-detail')   #take source
#         prdC = 0   # items count

#         searchList.append(['수입과일'])
#         for x in r:
#             temp = []
#             temp.append(prdC + 1)
#             temp.append(x.select_one('div.item-pay > h2').text.strip())   
#             temp.append(x.select_one('a > div > div.item-pay-detail > p.pay').text.strip())     
#             searchList.append(temp) #makes two-dimensional array
#             prdC = prdC + 1
#             if prdC == 15 : 
#                 break
#         driver.close()

#         f = open(f'./save/9-onbrix.csv', 'w', encoding='utf-8', newline='')
        
#         csvWriter = csv.writer(f)
#         for i in searchList:
#             csvWriter.writerow(i)
            
#         f.close()
#         print('onbrix done')
        
#     else :
#         print('word error!')
                    
# # csv file merge
# path = 'C:/PROJECTS/scraping_multisite/save/' #csv files route
# merge_path = 'C:/PROJECTS/scraping_multisite/crawl_data.csv' #save file

# file_list = glob.glob(path + '*')  # file check

# with open(merge_path, 'w') as f: # merge file open
#     for file in file_list:
#         with open(file ,'rt', encoding='utf-8') as f2:
#             while True:
#                 line = f2.readline() 

#                 if not line: 
#                     break

#                 f.write(line) # write save file
                
#         file_name = file.split('\\')[-1]
#         print(file.split('\\')[-1] + 'write one')

# print('>>making save file done')

# time.sleep(2)

# wb = Workbook()
# ws = wb.active
# with open('./crawl_data.csv', 'r', encoding='cp949') as f:
#     for row in csv.reader(f):
#         ws.append(row)

# wb.save('Prd_list_05_17.xlsx')