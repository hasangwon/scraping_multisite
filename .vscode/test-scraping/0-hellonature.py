import csv
from urllib.parse import quote_plus
from bs4 import BeautifulSoup
from selenium import webdriver
import glob
import time
from openpyxl import Workbook

hdr = {'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36"}
# --------------------------------------채소-------------------------------------------
print('VEGETABLE scraping..')
searchList = []
# 헬로네이처 필수채소-------------------------------------------------------------------
print('HN SCRAPING..')
searchList.append(['상품명','규격','가격'])
searchList.append(['●헬로네이처/필수채소'])
urlB = 'https://www.hellonature.co.kr/fdp001.do?goTo=dpItemList&gubunFlag=D&pageSize=10&filterYn=N&ctgrCd=020100&dpItemListCntYn=Y&page=1'  # site to crawl
driver = webdriver.Chrome()
time.sleep(1)
driver.get(urlB)
driver.implicitly_wait(3000)

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
r = soup.select('div.info')
prdC = 0

for x in r :
    temp = []
    try : 
        temp.append(x.select_one('div.name').text.strip())  
        temp.append('')    
        temp.append(x.select_one('div.cost').text)    
        searchList.append(temp) #makes two-dimensional array
    except IndexError as e :
        searchList.append(temp)  
    prdC = prdC + 1
    if prdC == 100 : 
        break
driver.close()
# 헬로네이처 반찬채소-------------------------------------------------------------------
searchList.append([' '])
searchList.append(['●헬로네이처/반찬채소'])
urlB = 'https://www.hellonature.co.kr/fdp001.do?goTo=dpItemList&gubunFlag=D&pageSize=10&filterYn=N&ctgrCd=020200&dpItemListCntYn=Y&page=1'  # site to crawl
driver = webdriver.Chrome()
time.sleep(1)
driver.get(urlB)
driver.implicitly_wait(3000)

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
r = soup.select('div.info')
prdC = 0

for x in r :
    temp = []
    try : 
        temp.append(x.select_one('div.name').text.strip())  
        temp.append('')     
        temp.append(x.select_one('div.cost').text)    
        searchList.append(temp) #makes two-dimensional array
    except IndexError as e :
        searchList.append(temp)  
    prdC = prdC + 1
    if prdC == 100 : 
        break
driver.close()

# 헬로네이처 뿌리채소-------------------------------------------------------------------
searchList.append([' '])
searchList.append(['●헬로네이처/뿌리채소'])
urlB = 'https://www.hellonature.co.kr/fdp001.do?goTo=dpItemList&gubunFlag=D&pageSize=10&filterYn=N&ctgrCd=020300&dpItemListCntYn=Y&page=1'  # site to crawl
driver = webdriver.Chrome()
time.sleep(1)
driver.get(urlB)
driver.implicitly_wait(3000)

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
r = soup.select('div.info')
prdC = 0

for x in r :
    temp = []
    try : 
        temp.append(x.select_one('div.name').text.strip())   
        temp.append('')    
        temp.append(x.select_one('div.cost').text)    
        searchList.append(temp) #makes two-dimensional array
    except IndexError as e :
        searchList.append(temp)  
    prdC = prdC + 1
    if prdC == 100 : 
        break
driver.close()

# 헬로네이처 버섯류-------------------------------------------------------------------
searchList.append([' '])
searchList.append(['●헬로네이처/버섯류'])
urlB = 'https://www.hellonature.co.kr/fdp001.do?goTo=dpItemList&gubunFlag=D&pageSize=10&filterYn=N&ctgrCd=020600&dpItemListCntYn=Y&page=1'  # site to crawl
driver = webdriver.Chrome()
time.sleep(1)
driver.get(urlB)
driver.implicitly_wait(3000)

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
r = soup.select('div.info')
prdC = 0

for x in r :
    temp = []
    try : 
        temp.append(x.select_one('div.name').text.strip())   
        temp.append('')    
        temp.append(x.select_one('div.cost').text)    
        searchList.append(temp) #makes two-dimensional array
    except IndexError as e :
        searchList.append(temp)  
    prdC = prdC + 1
    if prdC == 100 : 
        break
driver.close()
# 마켓컬리 -----------------------------------------------------------------------------
print('KURLY crawling')
searchList.append([' '])
searchList.append(['●마켓컬리'])
urlB = 'https://www.kurly.com/m2/goods/list.php?category=907'  # site to crawl
driver = webdriver.Chrome()
driver.implicitly_wait(3)
driver.get(urlB)
time.sleep(4)

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
r = soup.select('.info')   #take source
prdC = 0   # items count
for x in r:
    temp = []
    temp.append(x.select_one('span.name').text.strip())   
    temp.append('')    
    temp.append(x.select_one('span.cost span.price').text)    
    searchList.append(temp) #makes two-dimensional array
    prdC = prdC + 1
    if prdC == 500 : 
        break
driver.close()
# 채소목록 병합-------------------------------------------------------------------------
print('VEGETS LIST COMBINE .. ')
f = open(f'./save2/vegets.csv', 'w', encoding='utf-8', newline='')
csvWriter = csv.writer(f)
for i in searchList:
    csvWriter.writerow(i)
f.close()
print('Done!')      
                    
# csv file merge ----------------------------------------------------------------
path = 'C:/PROJECTS/scraping_multisite/save2/' #csv files route
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

wb.save('price_1018.xlsx')
print('>>All process done!')