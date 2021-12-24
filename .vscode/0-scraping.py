import csv
from urllib.parse import quote_plus
from bs4 import BeautifulSoup
from selenium import webdriver
import glob
import time
from openpyxl import Workbook

hdr = {'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36"}
# --------------------------------------과일-------------------------------------------
print('FRUITS scraping..')
searchList = []
searchList.append(['index','sname','pname','price'])
# 이마트몰 -----------------------------------------------------------------------------
print('EMART crawling')
urlA = 'http://emart.ssg.com/category/main.ssg?dispCtgId=6000095739'  # site to crawl
driver = webdriver.Chrome()
driver.implicitly_wait(3)
driver.get(urlA)
html = driver.page_source
soup = BeautifulSoup(html)
r = soup.select('.cunit_t232')   #take source
prdC = 0   # items count
        
searchList.append(['이마트몰/과일'])
for x in r:
    temp = []
    temp.append(prdC + 1)
    temp.append('이마트몰')
    temp.append(x.select_one('div.title a > em.tx_ko').text)      #items 1
    temp.append(x.select_one('div.opt_price em.ssg_price').text)  #items 2
    searchList.append(temp) #makes two-dimensional array
    prdC = prdC + 1
    if prdC == 30 : 
        break
driver.close()

# 마켓컬리 -----------------------------------------------------------------------------
print('K crawling')



urlA = 'https://www.kurly.com/shop/goods/goods_list.php?category=908006'
driver = webdriver.Chrome()
time.sleep(2)
driver.get(urlA)
driver.implicitly_wait(3)

SCROLL_PAUSE_TIME = 2

    # Get scroll height
last_height = driver.execute_script("return document.body.scrollHeight")

while True:
    # Scroll down to bottom
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        # Wait to load page
    time.sleep(SCROLL_PAUSE_TIME)
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight-50);")
    time.sleep(SCROLL_PAUSE_TIME)
    # Calculate new scroll height and compare with last scroll height
    new_height = driver.execute_script("return document.body.scrollHeight")
    if new_height == last_height:
        break
    last_height = new_height

html = driver.page_source
soup = BeautifulSoup(html)
r = soup.select('.info')
prdC = 0
searchList.append([' '])
searchList.append(['컬리/과일'])
for i in range(30) :
    temp = []
    try : 
        temp.append(prdC + 1)
        temp.append('마켓컬리')
        temp.append(r[i].select_one('span.name').text.strip())   
        temp.append(r[i].select_one('span.cost span.price').text)    
        searchList.append(temp) #makes two-dimensional array
    except IndexError as e :
        searchList.append(temp) #makes two-dimensional array
    prdC = prdC + 1
    if prdC == 30 : 
        break
driver.close()

# 쿠팡 -----------------------------------------------------------------------------
print('COUPANG crawling')
urlA = 'https://www.coupang.com/np/categories/194282'
driver = webdriver.Chrome()
driver.implicitly_wait(3)
driver.get(urlA)
html = driver.page_source
soup = BeautifulSoup(html)
r = soup.select('.baby-product-wrap')
prdC = 0
        
searchList.append([' '])
searchList.append(['쿠팡/과일'])
for x in r:
    temp = []
    temp.append(prdC + 1)
    temp.append('쿠팡')
    temp.append(x.select_one('.name').text.strip())   
    temp.append(x.select_one('.price-value').text.strip())    
    searchList.append(temp)
    prdC = prdC + 1
    if prdC == 30 : 
        break
driver.close()

# 네이버 -----------------------------------------------------------------------------
print('NAVER crawling')
urlA = 'https://search.shopping.naver.com/search/category?catId=50000960'
driver = webdriver.Chrome()
time.sleep(2)
driver.get(urlA)
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
r = soup.select('div.basicList_info_area__17Xyo')
prdC = 0
searchList.append([' '])
searchList.append(['네이버쇼핑/과일'])
for x in r:
    temp = []
    temp.append(prdC + 1)
    temp.append('네이버쇼핑')
    temp.append(x.select_one('a.basicList_link__1MaTN').text)   
    temp.append(x.select_one('span span.price_num__2WUXn').text)     
    searchList.append(temp)
    prdC = prdC + 1
    if prdC == 30 : 
        break
driver.close()

# 위메프 -----------------------------------------------------------------------------
print('WEMAP crawling')
urlA = 'https://front.wemakeprice.com/category/division/2100082'
driver = webdriver.Chrome()
driver.implicitly_wait(3)
driver.get(urlA)
html = driver.page_source
soup = BeautifulSoup(html)
r = soup.select('.box_listwrap.tab_cont .list_conts_wrap')
prdC = 0
        
searchList.append([' '])
searchList.append(['위메프/과일'])
for x in r:
    temp = []
    temp.append(prdC + 1)
    temp.append('위메프')
    temp.append(x.select_one('.option_txt .text').text)   
    temp.append(x.select_one('.option_txt .num').text)    
    searchList.append(temp)
    prdC = prdC + 1
    if prdC == 30 : 
        break
driver.close()                  

# 홈플러스 -----------------------------------------------------------------------------
print('HOMEPLUS crawling')
urlA = 'https://front.homeplus.co.kr/list?categoryDepth=1&categoryId=100001'
driver = webdriver.Chrome()
time.sleep(2)
driver.get(urlA)
driver.implicitly_wait(3)

SCROLL_PAUSE_TIME = 2

    # Get scroll height
last_height = driver.execute_script("return document.body.scrollHeight")

while True:
    # Scroll down to bottom
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        # Wait to load page
    time.sleep(SCROLL_PAUSE_TIME)
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight-50);")
    time.sleep(SCROLL_PAUSE_TIME)
    # Calculate new scroll height and compare with last scroll height
    new_height = driver.execute_script("return document.body.scrollHeight")
    if new_height == last_height:
        break
    last_height = new_height

html = driver.page_source
soup = BeautifulSoup(html)
r = soup.select('div.detailInfo')
prdC = 0
searchList.append([' '])
searchList.append(['홈플러스/과일'])
for x in r:
    temp = []
    temp.append(prdC + 1)
    temp.append('홈플러스')
    temp.append(x.select_one('a.productTitle.css-y9z3ts-defaultStyle-Linked').text)   
    temp.append(x.select_one('strong.priceValue').text)     
    searchList.append(temp)
    prdC = prdC + 1
    if prdC == 30 : 
        break
driver.close()

# 지마켓 -----------------------------------------------------------------------------
print('GMARKET crawling')
urlA = 'http://browse.gmarket.co.kr/list?category=200000482'
driver = webdriver.Chrome()
driver.implicitly_wait(3)
driver.get(urlA)
html = driver.page_source
soup = BeautifulSoup(html)
r = soup.select('.box__information-major')
prdC = 0
        
searchList.append([' '])
searchList.append(['지마켓/과일'])
for x in r:
    temp = []
    temp.append(prdC + 1)
    temp.append('지마켓')
    temp.append(x.select_one('span.text__item').attrs['title'])   
    temp.append(x.select_one('strong.text.text__value').text)    
    searchList.append(temp)
    prdC = prdC + 1
    if prdC == 30 : 
        break
driver.close()

# 카카오 -----------------------------------------------------------------------------
print('KAKAO crawling')
urlA = 'https://store.kakao.com/category/3/102104103?level=2'  # site to crawl
driver = webdriver.Chrome()
driver.implicitly_wait(3)
driver.get(urlA)
time.sleep(2)
html = driver.page_source
soup = BeautifulSoup(html)
r = soup.select('.link_product') 
prdC = 0   # items count
        
searchList.append([' '])
searchList.append(['카카오쇼핑/과일'])
for x in r:
    temp = []
    try : 
        temp.append(prdC + 1)
        temp.append('카카오쇼핑')
        temp.append(x.select_one('.product_name').text)   #items 1
        temp.append(x.select_one('.txt_number.ng-star-inserted').text)  #items 2
        searchList.append(temp) #makes two-dimensional array
    except AttributeError as e :
        temp.append('err')   #items 1
        searchList.append(temp) #makes two-dimensional array
    prdC = prdC + 1
    if prdC == 30 : 
        break
driver.close()

# ONBRIX -----------------------------------------------------------------------------
print('ONBRIX crawling')
searchList.append([' '])
searchList.append(['온브릭스/국산과일'])
urlA = 'https://farmerstable.imweb.me/38'
driver = webdriver.Chrome()
time.sleep(2)
driver.get(urlA)
driver.implicitly_wait(3)

SCROLL_PAUSE_TIME = 2

    # Get scroll height
last_height = driver.execute_script("return document.body.scrollHeight")

while True:
    # Scroll down to bottom
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        # Wait to load page
    time.sleep(SCROLL_PAUSE_TIME)
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight-50);")
    time.sleep(SCROLL_PAUSE_TIME)
    # Calculate new scroll height and compare with last scroll height
    new_height = driver.execute_script("return document.body.scrollHeight")
    if new_height == last_height:
        break
    last_height = new_height

html = driver.page_source
soup = BeautifulSoup(html)
r = soup.select('.item-detail')
prdC = 0
for i in range(15) :
    temp = []
    try : 
        temp.append(prdC + 1)
        temp.append('온브릭스')
        temp.append(r[i].select_one('div.item-pay > h2').text.strip())   
        temp.append(r[i].select_one('div.item-pay > div.item-pay-detail > p.pay').text.strip())   
        searchList.append(temp) #makes two-dimensional array
    except IndexError as e :
        searchList.append(temp) #makes two-dimensional array
    prdC = prdC + 1
    if prdC == 15 : 
        break
driver.close()

urlB = 'https://farmerstable.imweb.me/39'  # site to crawl
driver = webdriver.Chrome()
driver.implicitly_wait(3)
driver.get(urlB)
html = driver.page_source
soup = BeautifulSoup(html)
r = soup.select('.item-detail')   #take source
prdC = 0   # items count

searchList.append(['온브릭스/수입과일'])
for i in range(15) :
    temp = []
    try : 
        temp.append(prdC + 1)
        temp.append('온브릭스')
        temp.append(r[i].select_one('div.item-pay > h2').text.strip())   
        temp.append(r[i].select_one('div.item-pay > div.item-pay-detail > p.pay').text.strip())   
        searchList.append(temp) #makes two-dimensional array
    except IndexError as e :
        searchList.append(temp) #makes two-dimensional array
    prdC = prdC + 1
    if prdC == 15 : 
        break
driver.close()

# 과일목록 병합-------------------------------------------------------------------------
print('FRUITS LIST COMBINE .. ')
f = open(f'./save/fruits.csv', 'w', encoding='utf-8', newline='')
        
csvWriter = csv.writer(f)
for i in searchList:
    csvWriter.writerow(i)
f.close()
print('Done!')
# --------------------------------------채소-------------------------------------------
print('VEGETABLE scraping..')
searchList = []
searchList.append([' - 채소 -'])
# 이마트 -----------------------------------------------------------------------------
print('EMART crawling')
searchList.append(['이마트몰/채소'])
urlB = 'http://emart.ssg.com/category/main.ssg?dispCtgId=6000095740&sort=sale'  # site to crawl
driver = webdriver.Chrome()
driver.implicitly_wait(3)
driver.get(urlB)
html = driver.page_source
soup = BeautifulSoup(html)
r = soup.select('.cunit_t232')   #take source
prdC = 0   # items count

for x in r:
    temp = []
    temp.append(prdC + 1)
    temp.append('이마트몰')
    temp.append(x.select_one('div.title a > em.tx_ko').text)      #items 1
    temp.append(x.select_one('div.opt_price em.ssg_price').text)  #items 2
    searchList.append(temp) #makes two-dimensional array
    prdC = prdC + 1
    if prdC == 30 : 
        break
driver.close()

# 마켓컬리 -----------------------------------------------------------------------------
print('KURLY crawling')
searchList.append([' '])
searchList.append(['마켓컬리/채소'])
urlB = 'https://www.kurly.com/shop/goods/goods_list.php?category=907'  # site to crawl
driver = webdriver.Chrome()
driver.implicitly_wait(3)
driver.get(urlB)
time.sleep(4)
html = driver.page_source
soup = BeautifulSoup(html)
r = soup.select('.info')   #take source
prdC = 0   # items count
for x in r:
    temp = []
    temp.append(prdC + 1)
    temp.append('마켓컬리')
    temp.append(x.select_one('span.name').text.strip())   
    temp.append(x.select_one('span.cost span.price').text)    
    searchList.append(temp) #makes two-dimensional array
    prdC = prdC + 1
    if prdC == 30 : 
        break
driver.close()
# 쿠팡 -----------------------------------------------------------------------------
print('KURLY crawling') 
searchList.append([' '])
searchList.append(['쿠팡/채소'])
urlB = 'https://www.coupang.com/np/categories/194432'  # site to crawl
driver = webdriver.Chrome()
driver.implicitly_wait(3)
driver.get(urlB)
html = driver.page_source
soup = BeautifulSoup(html)
r = soup.select('.baby-product-wrap')   #take source
prdC = 0   # items count

for x in r:
    temp = []
    temp.append(prdC + 1)
    temp.append('쿠팡')
    temp.append(x.select_one('.name').text.strip())   
    temp.append(x.select_one('.price-value').text.strip())    
    searchList.append(temp) #makes two-dimensional array
    prdC = prdC + 1
    if prdC == 30 : 
        break
driver.close()
        
# 네이버 -----------------------------------------------------------------------------
print('NAVER crawling')
urlB = 'https://search.shopping.naver.com/search/category?catId=50001077'
driver = webdriver.Chrome()
time.sleep(2)
driver.get(urlB)
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
r = soup.select('div.basicList_info_area__17Xyo')
prdC = 0
searchList.append([' '])
searchList.append(['네이버쇼핑/채소'])
for x in r:
    temp = []
    temp.append(prdC + 1)
    temp.append('네이버쇼핑')
    temp.append(x.select_one('a.basicList_link__1MaTN').text)   
    temp.append(x.select_one('span span.price_num__2WUXn').text)     
    searchList.append(temp) 
    prdC = prdC + 1
    if prdC == 30 : 
        break
driver.close()

# 위메프 -----------------------------------------------------------------------------
print('WEMAP crawling')
searchList.append([' '])
searchList.append(['위메프/채소'])
urlB = 'https://front.wemakeprice.com/category/division/2100085'  # site to crawl
driver = webdriver.Chrome()
driver.implicitly_wait(3)
driver.get(urlB)
html = driver.page_source
soup = BeautifulSoup(html)
r = soup.select('.box_listwrap.tab_cont .list_conts_wrap')
prdC = 0   # items count

for x in r:
    temp = []
    temp.append(prdC + 1)
    temp.append('위메프')
    temp
    temp.append(x.select_one('.option_txt .text').text)   
    temp.append(x.select_one('.option_txt .num').text)    
    searchList.append(temp) #makes two-dimensional array
    prdC = prdC + 1
    if prdC == 30 : 
        break
driver.close()

# 홈플러스 -----------------------------------------------------------------------------
print('HOMEPLUS crawling')
urlA = 'https://front.homeplus.co.kr/list?categoryId=100003&categoryDepth=1'
driver = webdriver.Chrome()
time.sleep(2)
driver.get(urlA)
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
r = soup.select('div.detailInfo')
prdC = 0
searchList.append([' '])
searchList.append(['홈플러스/채소'])
for x in r:
    temp = []
    temp.append(prdC + 1)
    temp.append('홈플러스')
    temp.append(x.select_one('a.productTitle.css-y9z3ts-defaultStyle-Linked').text)   
    temp.append(x.select_one('strong.priceValue').text)     
    searchList.append(temp)
    prdC = prdC + 1
    if prdC == 30 : 
        break
driver.close()

# 지마켓 -----------------------------------------------------------------------------
print('GMARKET crawling')
searchList.append([' '])
searchList.append(['지마켓/채소']) 
urlB = 'http://browse.gmarket.co.kr/list?category=200001215'  # site to crawl
driver = webdriver.Chrome()
driver.implicitly_wait(3)
driver.get(urlB)
html = driver.page_source
soup = BeautifulSoup(html)
r = soup.select('.box__information-major')   #take source
prdC = 0   # items count
for x in r:
    temp = []
    temp.append(prdC + 1)
    temp.append('지마켓')
    temp.append(x.select_one('span.text__item').attrs['title'])   
    temp.append(x.select_one('strong.text.text__value').text)    
    searchList.append(temp) #makes two-dimensional array
    prdC = prdC + 1
    if prdC == 30 :  
        break
driver.close()

# 카카오 -----------------------------------------------------------------------------
print('KAKAO crawling')
searchList.append([' '])
searchList.append(['카카오쇼핑/농산물'])
urlB = 'https://store.kakao.com/category/3/102104101?level=2'  # site to crawl
driver = webdriver.Chrome()
driver.implicitly_wait(3)
driver.get(urlB)
html = driver.page_source
soup = BeautifulSoup(html)
r = soup.select('.link_product') 
prdC = 0   # items count

for x in r:
    temp = []
    try : 
        temp.append(prdC + 1)
        temp.append('카카오쇼핑')
        temp.append(x.select_one('.product_name').text)   #items 1
        temp.append(x.select_one('.txt_number.ng-star-inserted').text)  #items 2
        searchList.append(temp) #makes two-dimensional array
    except AttributeError as e :
        temp.append('err')   #items 1
        searchList.append(temp) #makes two-dimensional array
    prdC = prdC + 1
    if prdC == 30 : 
        break
driver.close()

# 맛다름 자사몰 과일/채소------------------------------------------------------------------
# - 국산과일
print('EFC crawling..')
searchList.append([' - 자사몰 - '])
searchList.append(['맛다름'])
searchList.append(['국산과일'])
urlA = 'https://www.efc365.co.kr/product/list.html?cate_no=24'
driver = webdriver.Chrome()
driver.get(urlA)
driver.implicitly_wait(3)

SCROLL_PAUSE_TIME = 2

    # Get scroll height
last_height = driver.execute_script("return document.body.scrollHeight")

while True:
    # Scroll down to bottom
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        # Wait to load page
    time.sleep(SCROLL_PAUSE_TIME)
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight-50);")
    time.sleep(SCROLL_PAUSE_TIME)
    # Calculate new scroll height and compare with last scroll height
    new_height = driver.execute_script("return document.body.scrollHeight")
    if new_height == last_height:
        break
    last_height = new_height

html = driver.page_source
soup = BeautifulSoup(html)
r = soup.select('.description')
prdC = 0
for i in range(30) :
    temp = []
    try : 
        temp.append(prdC + 1)
        temp.append('맛다름')
        #temp.append(r[i].select_one('p.name ').text)   
        #temp.append(r[i].select_one('span.price.displaynone_sale.displaynone_custom').text)  
        searchList.append(temp) #makes two-dimensional array
    except AttributeError as e :
        searchList.append(temp) #makes two-dimensional array
    prdC = prdC + 1
    if prdC == 30 : 
        break
driver.close()

#수입과일
print('EFC crawling..')
searchList.append(['수입과일'])
urlA = 'https://www.efc365.co.kr/product/list.html?cate_no=25'
driver = webdriver.Chrome()
driver.get(urlA)
driver.implicitly_wait(3)

SCROLL_PAUSE_TIME = 2

    # Get scroll height
last_height = driver.execute_script("return document.body.scrollHeight")

while True:
    # Scroll down to bottom
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        # Wait to load page
    time.sleep(SCROLL_PAUSE_TIME)
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight-50);")
    time.sleep(SCROLL_PAUSE_TIME)
    # Calculate new scroll height and compare with last scroll height
    new_height = driver.execute_script("return document.body.scrollHeight")
    if new_height == last_height:
        break
    last_height = new_height

html = driver.page_source
soup = BeautifulSoup(html)
r = soup.select('.description')
prdC = 0
for i in range(30) :
    temp = []
    try : 
        temp.append(prdC + 1)
        temp.append('맛다름')
        #temp.append(r[i].select_one('p.name ').text)   
        #temp.append(r[i].select_one('span.price.displaynone_sale.displaynone_custom').text)  
        searchList.append(temp) #makes two-dimensional array
    except AttributeError as e :
        searchList.append(temp) #makes two-dimensional array
    prdC = prdC + 1
    if prdC == 30 : 
        break
driver.close()

#야채알뜰
print('EFC crawling..')
searchList.append(['야채알뜰'])
urlA = 'https://www.efc365.co.kr/product/list.html?cate_no=43'
driver = webdriver.Chrome()
driver.get(urlA)
driver.implicitly_wait(3)

SCROLL_PAUSE_TIME = 2

    # Get scroll height
last_height = driver.execute_script("return document.body.scrollHeight")

while True:
    # Scroll down to bottom
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        # Wait to load page
    time.sleep(SCROLL_PAUSE_TIME)
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight-50);")
    time.sleep(SCROLL_PAUSE_TIME)
    # Calculate new scroll height and compare with last scroll height
    new_height = driver.execute_script("return document.body.scrollHeight")
    if new_height == last_height:
        break
    last_height = new_height

html = driver.page_source
soup = BeautifulSoup(html)
r = soup.select('.description')
prdC = 0
for i in range(30) :
    temp = []
    try : 
        temp.append(prdC + 1)
        temp.append('맛다름')
        #temp.append(r[i].select_one('p.name ').text)   
        #temp.append(r[i].select_one('span.price.displaynone_sale.displaynone_custom').text)  
        searchList.append(temp) #makes two-dimensional array
    except AttributeError as e :
        searchList.append(temp) #makes two-dimensional array
    prdC = prdC + 1
    if prdC == 30 : 
        break
driver.close()

#신선야채
print('EFC crawling..')
searchList.append(['신선야채'])
urlA = 'https://www.efc365.co.kr/product/list.html?cate_no=45'
driver = webdriver.Chrome()
driver.get(urlA)
driver.implicitly_wait(3)

SCROLL_PAUSE_TIME = 2

    # Get scroll height
last_height = driver.execute_script("return document.body.scrollHeight")

while True:
    # Scroll down to bottom
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        # Wait to load page
    time.sleep(SCROLL_PAUSE_TIME)
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight-50);")
    time.sleep(SCROLL_PAUSE_TIME)
    # Calculate new scroll height and compare with last scroll height
    new_height = driver.execute_script("return document.body.scrollHeight")
    if new_height == last_height:
        break
    last_height = new_height

html = driver.page_source
soup = BeautifulSoup(html)
r = soup.select('.description')
prdC = 0
for i in range(30) :
    temp = []
    try : 
        temp.append(prdC + 1)
        temp.append('맛다름')
        #temp.append(r[i].select_one('p.name ').text)   
        #temp.append(r[i].select_one('span.price.displaynone_sale.displaynone_custom').text)   
        searchList.append(temp) #makes two-dimensional array
    except AttributeError as e :
        searchList.append(temp) #makes two-dimensional array
    prdC = prdC + 1 
    if prdC == 30 : 
        break
driver.close()

# 채소목록 병합-------------------------------------------------------------------------
print('VEGETS LIST COMBINE .. ')
f = open(f'./save/vegets.csv', 'w', encoding='utf-8', newline='')
csvWriter = csv.writer(f)
for i in searchList:
    csvWriter.writerow(i)
f.close()
print('Done!')      
                    
# csv file merge ----------------------------------------------------------------
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
print('making save file done!')
time.sleep(2)
# CSV to XLSX ----------------------------------------------------------------------
print('csv to xlsx...')
wb = Workbook()
ws = wb.active
with open('./crawl_data.csv', 'r', encoding='cp949') as f:
    for row in csv.reader(f):
        ws.append(row)
wb.save('Prd_list_12.xlsx')
print('>>All process done!')







