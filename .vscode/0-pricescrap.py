import csv
from urllib.parse import quote_plus
from bs4 import BeautifulSoup
from selenium import webdriver
import glob
import time
from openpyxl import Workbook

#공통 선언
hdr = {'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36"}
print('헬로네이처 스크래핑 시작')
searchList = []
searchList.append(['●헬로네이처'])
searchList.append(['상품명','가격','행사가'])

#양파
driver = webdriver.Chrome()
driver.get('https://www.hellonature.co.kr/fdp001.do?goTo=dpItemView&itemCd=108195')
html = driver.page_source
soup = BeautifulSoup(html)
temp = []
try :    
    temp.append(soup.select_one('.prd_name').text.strip())
    temp.append(soup.select_one('#afterCost').text.strip())
    temp.append(soup.select_one('#beforeCost').text.strip())
    searchList.append(temp)
except AttributeError as e :
    temp.append(soup.select_one('#afterCost').text.strip())
    searchList.append(temp) 
driver.implicitly_wait(1000)

#대파
driver.get('https://www.hellonature.co.kr/fdp001.do?goTo=dpItemView&itemCd=108198')
html = driver.page_source
soup = BeautifulSoup(html)
temp =[]
try :    
    temp.append(soup.select_one('.prd_name').text.strip())
    temp.append(soup.select_one('#afterCost').text.strip())
    temp.append(soup.select_one('#beforeCost').text.strip())
    searchList.append(temp)
except AttributeError as e :
    temp.append(soup.select_one('#afterCost').text.strip())
    searchList.append(temp)  
driver.implicitly_wait(1000)

#양상추
driver.get('https://www.hellonature.co.kr/fdp001.do?goTo=dpItemView&itemCd=108201')
html = driver.page_source
soup = BeautifulSoup(html)
temp =[]
try :    
    temp.append(soup.select_one('.prd_name').text.strip())
    temp.append(soup.select_one('#afterCost').text.strip())
    temp.append(soup.select_one('#beforeCost').text.strip())
    searchList.append(temp)
except AttributeError as e :
    temp.append(soup.select_one('#afterCost').text.strip())
    searchList.append(temp) 
driver.implicitly_wait(1000)

#당근
driver.get('https://www.hellonature.co.kr/fdp001.do?goTo=dpItemView&itemCd=108196')
html = driver.page_source
soup = BeautifulSoup(html)
temp =[]
try :    
    temp.append(soup.select_one('.prd_name').text.strip())
    temp.append(soup.select_one('#afterCost').text.strip())
    temp.append(soup.select_one('#beforeCost').text.strip())
    searchList.append(temp)
except AttributeError as e :
    temp.append(soup.select_one('#afterCost').text.strip())
    searchList.append(temp) 
driver.implicitly_wait(1000)
#감자
driver.get('https://www.hellonature.co.kr/fdp001.do?goTo=dpItemView&itemCd=108194')
html = driver.page_source
soup = BeautifulSoup(html)
temp =[]
try :    
    temp.append(soup.select_one('.prd_name').text.strip())
    temp.append(soup.select_one('#afterCost').text.strip())
    temp.append(soup.select_one('#beforeCost').text.strip())
    searchList.append(temp)
except AttributeError as e :
    temp.append(soup.select_one('#afterCost').text.strip())
    searchList.append(temp) 
driver.implicitly_wait(1000)
#생강
driver.get('https://www.hellonature.co.kr/fdp001.do?goTo=dpItemView&itemCd=108203')
html = driver.page_source
soup = BeautifulSoup(html)
temp =[]
try :    
    temp.append(soup.select_one('.prd_name').text.strip())
    temp.append(soup.select_one('#afterCost').text.strip())
    temp.append(soup.select_one('#beforeCost').text.strip())
    searchList.append(temp)
except AttributeError as e :
    temp.append(soup.select_one('#afterCost').text.strip())
    searchList.append(temp) 
driver.implicitly_wait(1000)
#파프
driver.get('https://www.hellonature.co.kr/fdp001.do?goTo=dpItemView&itemCd=108200')
html = driver.page_source
soup = BeautifulSoup(html)
temp =[]
try :    
    temp.append(soup.select_one('.prd_name').text.strip())
    temp.append(soup.select_one('#afterCost').text.strip())
    temp.append(soup.select_one('#beforeCost').text.strip())
    searchList.append(temp)
except AttributeError as e :
    temp.append(soup.select_one('#afterCost').text.strip())
    searchList.append(temp) 
driver.implicitly_wait(1000)
#백오이
driver.get('https://www.hellonature.co.kr/fdp001.do?goTo=dpItemView&itemCd=108197')
html = driver.page_source
soup = BeautifulSoup(html)
temp =[]
try :    
    temp.append(soup.select_one('.prd_name').text.strip())
    temp.append(soup.select_one('#afterCost').text.strip())
    temp.append(soup.select_one('#beforeCost').text.strip())
    searchList.append(temp)
except AttributeError as e :
    temp.append(soup.select_one('#afterCost').text.strip())
    searchList.append(temp) 
driver.implicitly_wait(1000)
#깐마늘
driver.get('https://www.hellonature.co.kr/fdp001.do?goTo=dpItemView&itemCd=108202')
html = driver.page_source
soup = BeautifulSoup(html)
temp =[]
try :    
    temp.append(soup.select_one('.prd_name').text.strip())
    temp.append(soup.select_one('#afterCost').text.strip())
    temp.append(soup.select_one('#beforeCost').text.strip())
    searchList.append(temp)
except AttributeError as e :
    temp.append(soup.select_one('#afterCost').text.strip())
    searchList.append(temp) 
driver.implicitly_wait(1000)
#붉은 비트
driver.get('https://www.hellonature.co.kr/fdp001.do?goTo=dpItemView&itemCd=108204')
html = driver.page_source
soup = BeautifulSoup(html)
temp =[]
try :    
    temp.append(soup.select_one('.prd_name').text.strip())
    temp.append(soup.select_one('#afterCost').text.strip())
    temp.append(soup.select_one('#beforeCost').text.strip())
    searchList.append(temp)
except AttributeError as e :
    temp.append(soup.select_one('#afterCost').text.strip())
    searchList.append(temp) 
driver.implicitly_wait(1000)
#파프리카 4입
driver.get('https://www.hellonature.co.kr/fdp001.do?goTo=dpItemView&itemCd=108196')
html = driver.page_source
soup = BeautifulSoup(html)
temp =[]
try :    
    temp.append('파프리카4입')
    searchList.append(temp)
except AttributeError as e :
    temp.append(soup.select_one('#afterCost').text.strip())
    searchList.append(temp) 
driver.implicitly_wait(1000)
#국내산 가지 250g
driver.get('https://www.hellonature.co.kr/fdp001.do?goTo=dpItemView&itemCd=029065')
html = driver.page_source
soup = BeautifulSoup(html)
temp =[]
try :    
    temp.append(soup.select_one('.prd_name').text.strip())
    temp.append(soup.select_one('#afterCost').text.strip())
    temp.append(soup.select_one('#beforeCost').text.strip())
    searchList.append(temp)
except AttributeError as e :
    temp.append(soup.select_one('#afterCost').text.strip())
    searchList.append(temp) 
driver.implicitly_wait(1000)
#브콜
driver.get('https://www.hellonature.co.kr/fdp001.do?goTo=dpItemView&itemCd=024211')
html = driver.page_source
soup = BeautifulSoup(html)
temp =[]
try :    
    temp.append(soup.select_one('.prd_name').text.strip())
    temp.append(soup.select_one('#afterCost').text.strip())
    temp.append(soup.select_one('#beforeCost').text.strip())
    searchList.append(temp)
except AttributeError as e :
    temp.append(soup.select_one('#afterCost').text.strip())
    searchList.append(temp) 
driver.implicitly_wait(1000)
#금치
driver.get('https://www.hellonature.co.kr/fdp001.do?goTo=dpItemView&itemCd=025972')
html = driver.page_source
soup = BeautifulSoup(html)
temp =[]
try :    
    temp.append(soup.select_one('.prd_name').text.strip())
    temp.append(soup.select_one('#afterCost').text.strip())
    temp.append(soup.select_one('#beforeCost').text.strip())
    searchList.append(temp)
except AttributeError as e :
    temp.append(soup.select_one('#afterCost').text.strip())
    searchList.append(temp) 
driver.implicitly_wait(1000)
#양배추
driver.get('https://www.hellonature.co.kr/fdp001.do?goTo=dpItemView&itemCd=104078')
html = driver.page_source
soup = BeautifulSoup(html)
temp =[]
try :    
    temp.append(soup.select_one('.prd_name').text.strip())
    temp.append(soup.select_one('#afterCost').text.strip())
    temp.append(soup.select_one('#beforeCost').text.strip())
    searchList.append(temp)
except AttributeError as e :
    temp.append(soup.select_one('#afterCost').text.strip())
    searchList.append(temp) 
driver.implicitly_wait(1000)
#무 1통
driver.get('https://www.hellonature.co.kr/fdp001.do?goTo=dpItemView&itemCd=020380')
html = driver.page_source
soup = BeautifulSoup(html)
temp =[]
try :    
    temp.append(soup.select_one('.prd_name').text.strip())
    temp.append(soup.select_one('#afterCost').text.strip())
    temp.append(soup.select_one('#beforeCost').text.strip())
    searchList.append(temp)
except AttributeError as e :
    temp.append(soup.select_one('#afterCost').text.strip())
    searchList.append(temp) 
driver.implicitly_wait(1000)
#스틱 샐러리 150g
driver.get('https://www.hellonature.co.kr/fdp001.do?goTo=dpItemView&itemCd=104067')
html = driver.page_source
soup = BeautifulSoup(html)
temp =[]
try :    
    temp.append(soup.select_one('.prd_name').text.strip())
    temp.append(soup.select_one('#afterCost').text.strip())
    temp.append(soup.select_one('#beforeCost').text.strip())
    searchList.append(temp)
except AttributeError as e :
    temp.append(soup.select_one('#afterCost').text.strip())
    searchList.append(temp) 
driver.implicitly_wait(1000)
#인큐 애호박 1개
driver.get('https://www.hellonature.co.kr/fdp001.do?goTo=dpItemView&itemCd=026266')
html = driver.page_source
soup = BeautifulSoup(html)
temp =[]
try :    
    temp.append(soup.select_one('.prd_name').text.strip())
    temp.append(soup.select_one('#afterCost').text.strip())
    temp.append(soup.select_one('#beforeCost').text.strip())
    searchList.append(temp)
except AttributeError as e :
    temp.append(soup.select_one('#afterCost').text.strip())
    searchList.append(temp) 
driver.implicitly_wait(1000)

#포슬포슬 밤고구마 800g
driver.get('https://www.hellonature.co.kr/fdp001.do?goTo=dpItemView&itemCd=024440')
html = driver.page_source
soup = BeautifulSoup(html)
temp =[]
try :    
    temp.append(soup.select_one('.prd_name').text.strip())
    temp.append(soup.select_one('#afterCost').text.strip())
    temp.append(soup.select_one('#beforeCost').text.strip())
    searchList.append(temp)
except AttributeError as e :
    temp.append(soup.select_one('#afterCost').text.strip())
    searchList.append(temp) 
driver.implicitly_wait(1000)
#당진햇호박고구마
driver.get('https://www.hellonature.co.kr/fdp001.do?goTo=dpItemView&itemCd=101219')
html = driver.page_source
soup = BeautifulSoup(html)
temp =[]
try :    
    temp.append(soup.select_one('.prd_name').text.strip())
    temp.append(soup.select_one('#afterCost').text.strip())
    temp.append(soup.select_one('#beforeCost').text.strip())
    searchList.append(temp)
except AttributeError as e :
    temp.append(soup.select_one('#afterCost').text.strip())
    searchList.append(temp) 
driver.implicitly_wait(1000)
#남해초
driver.get('https://www.hellonature.co.kr/fdp001.do?goTo=dpItemView&itemCd=101645')
html = driver.page_source
soup = BeautifulSoup(html)
temp =[]
try :    
    temp.append(soup.select_one('.prd_name').text.strip())
    temp.append(soup.select_one('#afterCost').text.strip())
    temp.append(soup.select_one('#beforeCost').text.strip())
    searchList.append(temp)
except AttributeError as e :
    temp.append(soup.select_one('#afterCost').text.strip())
    searchList.append(temp) 
driver.implicitly_wait(1000)
#깐쪽파
driver.get('https://www.hellonature.co.kr/fdp001.do?goTo=dpItemView&itemCd=104111')
html = driver.page_source
soup = BeautifulSoup(html)
temp =[]
try :    
    temp.append(soup.select_one('.prd_name').text.strip())
    temp.append(soup.select_one('#afterCost').text.strip())
    temp.append(soup.select_one('#beforeCost').text.strip())
    searchList.append(temp)
except AttributeError as e :
    temp.append(soup.select_one('#afterCost').text.strip())
    searchList.append(temp) 
driver.implicitly_wait(1000)
#흙쪽파
driver.get('https://www.hellonature.co.kr/fdp001.do?goTo=dpItemView&itemCd=101352')
html = driver.page_source
soup = BeautifulSoup(html)
temp =[]
try :    
    temp.append(soup.select_one('.prd_name').text.strip())
    temp.append(soup.select_one('#afterCost').text.strip())
    temp.append(soup.select_one('#beforeCost').text.strip())
    searchList.append(temp)
except AttributeError as e :
    temp.append(soup.select_one('#afterCost').text.strip())
    searchList.append(temp) 
driver.implicitly_wait(1000)
#알배기쌈배추
driver.get('https://www.hellonature.co.kr/fdp001.do?goTo=dpItemView&itemCd=028593')
html = driver.page_source
soup = BeautifulSoup(html)
temp =[]
try :    
    temp.append(soup.select_one('.prd_name').text.strip())
    temp.append(soup.select_one('#afterCost').text.strip())
    temp.append(soup.select_one('#beforeCost').text.strip())
    searchList.append(temp)
except AttributeError as e :
    temp.append(soup.select_one('#afterCost').text.strip())
    searchList.append(temp) 
driver.implicitly_wait(1000)
#홍고추
driver.get('https://www.hellonature.co.kr/fdp001.do?goTo=dpItemView&itemCd=028826')
html = driver.page_source
soup = BeautifulSoup(html)
temp =[]
try :    
    temp.append(soup.select_one('.prd_name').text.strip())
    temp.append(soup.select_one('#afterCost').text.strip())
    temp.append(soup.select_one('#beforeCost').text.strip())
    searchList.append(temp)
except AttributeError as e :
    temp.append(soup.select_one('#afterCost').text.strip())
    searchList.append(temp) 
driver.implicitly_wait(1000)
#꽈리고추
driver.get('https://www.hellonature.co.kr/fdp001.do?goTo=dpItemView&itemCd=106403')
html = driver.page_source
soup = BeautifulSoup(html)
temp =[]
try :    
    temp.append(soup.select_one('.prd_name').text.strip())
    temp.append(soup.select_one('#afterCost').text.strip())
    temp.append(soup.select_one('#beforeCost').text.strip())
    searchList.append(temp)
except AttributeError as e :
    temp.append(soup.select_one('#afterCost').text.strip())
    searchList.append(temp) 
driver.implicitly_wait(1000)
#청양고추
driver.get('https://www.hellonature.co.kr/fdp001.do?goTo=dpItemView&itemCd=026266')
html = driver.page_source
soup = BeautifulSoup(html)
temp =[]
try :    
    temp.append('청양고추')
    searchList.append(temp)
except AttributeError as e :
    temp.append(soup.select_one('#afterCost').text.strip())
    searchList.append(temp) 
driver.implicitly_wait(1000)
#오이맛고추 150g
driver.get('https://www.hellonature.co.kr/fdp001.do?goTo=dpItemView&itemCd=105437')
html = driver.page_source
soup = BeautifulSoup(html)
temp =[]
try :    
    temp.append(soup.select_one('.prd_name').text.strip())
    temp.append(soup.select_one('#afterCost').text.strip())
    temp.append(soup.select_one('#beforeCost').text.strip())
    searchList.append(temp)
except AttributeError as e :
    temp.append(soup.select_one('#afterCost').text.strip())
    searchList.append(temp) 
driver.implicitly_wait(1000)
#백오이 5개
driver.get('https://www.hellonature.co.kr/fdp001.do?goTo=dpItemView&itemCd=026266')
html = driver.page_source
soup = BeautifulSoup(html)
temp =[]
try :    
    temp.append('백오이')
    searchList.append(temp)
except AttributeError as e :
    temp.append(soup.select_one('#afterCost').text.strip())
    searchList.append(temp) 
driver.implicitly_wait(1000)
driver.close()
#헬로네이처 끝

#오아시스 공통 선언
searchList.append([''])
searchList.append(['●오아시스'])
searchList.append(['상품명','가격','행사가'])
#양파
driver = webdriver.Chrome()
driver.get('https://www.oasis.co.kr/product/detail/5626-1002761?categoryId=')
html = driver.page_source
soup = BeautifulSoup(html)
temp = []
try :    
    temp.append(soup.select_one('div.textSubject > h3').text.strip())
    temp.append(soup.select_one('div.price > dd:nth-child(2)').text.strip())
    temp.append(soup.select_one('div.price > dd:nth-child(4) > span > b').text.strip())
    searchList.append(temp)
except AttributeError as e :
    searchList.append(temp) 
driver.implicitly_wait(1000)

#대파
driver.get('https://www.oasis.co.kr/product/detail/34458-1034436?categoryId=')
html = driver.page_source
soup = BeautifulSoup(html)
temp =[]
try :    
    temp.append(soup.select_one('div.textSubject > h3').text.strip())
    temp.append(soup.select_one('div.price > dd:nth-child(2)').text.strip())
    temp.append(soup.select_one('div.price > dd:nth-child(4) > span > b').text.strip())
    searchList.append(temp)
except AttributeError as e :
    searchList.append(temp) 
driver.implicitly_wait(1000)
#양상추
driver.get('https://www.oasis.co.kr/product/detail/7336-1004663?categoryId=')
html = driver.page_source
soup = BeautifulSoup(html)
temp =[]
try :    
    temp.append(soup.select_one('div.textSubject > h3').text.strip())
    temp.append(soup.select_one('div.price > dd:nth-child(2)').text.strip())
    temp.append(soup.select_one('div.price > dd:nth-child(4) > span > b').text.strip())
    searchList.append(temp)
except AttributeError as e :
    searchList.append(temp) 
driver.implicitly_wait(1000)
#햇당근
driver.get('https://www.oasis.co.kr/product/detail/8028-1005399?categoryId=')
html = driver.page_source
soup = BeautifulSoup(html)
temp =[]
try :    
    temp.append(soup.select_one('div.textSubject > h3').text.strip())
    temp.append(soup.select_one('div.price > dd:nth-child(2)').text.strip())
    temp.append(soup.select_one('div.price > dd:nth-child(4) > span > b').text.strip())
    searchList.append(temp)
except AttributeError as e :
    searchList.append(temp) 
driver.implicitly_wait(1000)
#국내산 햇감자
driver.get('https://www.oasis.co.kr/product/detail/5932-1003128?categoryId=')
html = driver.page_source
soup = BeautifulSoup(html)
temp =[]
try :    
    temp.append(soup.select_one('div.textSubject > h3').text.strip())
    temp.append(soup.select_one('div.price > dd:nth-child(2)').text.strip())
    temp.append(soup.select_one('div.price > dd:nth-child(4) > span > b').text.strip())
    searchList.append(temp)
except AttributeError as e :
    searchList.append(temp) 
driver.implicitly_wait(1000)
#빈칸
driver.get('https://www.oasis.co.kr/product/detail/34458-1034436?categoryId=')
html = driver.page_source
soup = BeautifulSoup(html)
temp =[]
try :    
    temp.append('')
    searchList.append(temp)
except AttributeError as e :
    searchList.append(temp) 
driver.implicitly_wait(1000)
#국내산 파프리카
driver.get('https://www.oasis.co.kr/product/detail/24611-1023031?categoryId=')
html = driver.page_source
soup = BeautifulSoup(html)
temp =[]
try :    
    temp.append(soup.select_one('div.textSubject > h3').text.strip())
    temp.append(soup.select_one('div.price > dd:nth-child(2)').text.strip())
    temp.append(soup.select_one('div.price > dd:nth-child(4) > span > b').text.strip())
    searchList.append(temp)
except AttributeError as e :
    searchList.append(temp) 
driver.implicitly_wait(1000)
#국내산 백오이
driver.get('https://www.oasis.co.kr/product/detail/3231-1000110?categoryId=')
html = driver.page_source
soup = BeautifulSoup(html)
temp =[]
try :    
    temp.append(soup.select_one('div.textSubject > h3').text.strip())
    temp.append(soup.select_one('div.price > dd:nth-child(2)').text.strip())
    temp.append(soup.select_one('div.price > dd:nth-child(4) > span > b').text.strip())
    searchList.append(temp)
except AttributeError as e :
    searchList.append(temp) 
driver.implicitly_wait(1000)
#깐마늘 300g
driver.get('https://www.oasis.co.kr/product/detail/2343-2123?categoryId=')
html = driver.page_source
soup = BeautifulSoup(html)
temp =[]
try :    
    temp.append(soup.select_one('div.textSubject > h3').text.strip())
    temp.append(soup.select_one('div.price > dd:nth-child(2)').text.strip())
    temp.append(soup.select_one('div.price > dd:nth-child(4) > span > b').text.strip())
    searchList.append(temp)
except AttributeError as e :
    searchList.append(temp) 
driver.implicitly_wait(1000)
#국내산 비트 300g
driver.get('https://www.oasis.co.kr/product/detail/7337-1004664?categoryId=')
html = driver.page_source
soup = BeautifulSoup(html)
temp =[]
try :    
    temp.append(soup.select_one('div.textSubject > h3').text.strip())
    temp.append(soup.select_one('div.price > dd:nth-child(2)').text.strip())
    temp.append(soup.select_one('div.price > dd:nth-child(4) > span > b').text.strip())
    searchList.append(temp)
except AttributeError as e :
    searchList.append(temp) 
driver.implicitly_wait(1000)
#4입 파프리카
driver.get('https://www.oasis.co.kr/product/detail/9663-1007102?categoryId=')
html = driver.page_source
soup = BeautifulSoup(html)
temp =[]
try :    
    temp.append(soup.select_one('div.textSubject > h3').text.strip())
    temp.append(soup.select_one('div.price > dd:nth-child(2)').text.strip())
    temp.append(soup.select_one('div.price > dd:nth-child(4) > span > b').text.strip())
    searchList.append(temp)
except AttributeError as e :
    searchList.append(temp) 
driver.implicitly_wait(1000)
#국내산 가지
driver.get('https://www.oasis.co.kr/product/detail/1352-1000855?categoryId=')
html = driver.page_source
soup = BeautifulSoup(html)
temp =[]
try :    
    temp.append(soup.select_one('div.textSubject > h3').text.strip())
    temp.append(soup.select_one('div.price > dd:nth-child(2)').text.strip())
    temp.append(soup.select_one('div.price > dd:nth-child(4) > span > b').text.strip())
    searchList.append(temp)
except AttributeError as e :
    searchList.append(temp) 
driver.implicitly_wait(1000)
#국내산 브로콜리
driver.get('https://www.oasis.co.kr/product/detail/6997-1004333?categoryId=')
html = driver.page_source
soup = BeautifulSoup(html)
temp =[]
try :    
    temp.append(soup.select_one('div.textSubject > h3').text.strip())
    temp.append(soup.select_one('div.price > dd:nth-child(2)').text.strip())
    temp.append(soup.select_one('div.price > dd:nth-child(4) > span > b').text.strip())
    searchList.append(temp)
except AttributeError as e :
    searchList.append(temp) 
driver.implicitly_wait(1000)
#시금치 200g
driver.get('https://www.oasis.co.kr/product/detail/26348-1025032?categoryId=')
html = driver.page_source
soup = BeautifulSoup(html)
temp =[]
try :    
    temp.append(soup.select_one('div.textSubject > h3').text.strip())
    temp.append(soup.select_one('div.price > dd:nth-child(2)').text.strip())
    temp.append(soup.select_one('div.price > dd:nth-child(4) > span > b').text.strip())
    searchList.append(temp)
except AttributeError as e :
    searchList.append(temp) 
driver.implicitly_wait(1000)
#국산 양배추
driver.get('https://www.oasis.co.kr/product/detail/34451-1034429?categoryId=')
html = driver.page_source
soup = BeautifulSoup(html)
temp =[]
try :    
    temp.append(soup.select_one('div.textSubject > h3').text.strip())
    temp.append(soup.select_one('div.price > dd:nth-child(2)').text.strip())
    temp.append(soup.select_one('div.price > dd:nth-child(4) > span > b').text.strip())
    searchList.append(temp)
except AttributeError as e :
    searchList.append(temp) 
driver.implicitly_wait(1000)
#무농약 무
driver.get('https://www.oasis.co.kr/product/detail/7445-1004779?categoryId=')
html = driver.page_source
soup = BeautifulSoup(html)
temp =[]
try :    
    temp.append(soup.select_one('div.textSubject > h3').text.strip())
    temp.append(soup.select_one('div.price > dd:nth-child(2)').text.strip())
    temp.append(soup.select_one('div.price > dd:nth-child(4) > span > b').text.strip())
    searchList.append(temp)
except AttributeError as e :
    searchList.append(temp) 
driver.implicitly_wait(1000)
#국내산 샐러리
driver.get('https://www.oasis.co.kr/product/detail/7338-1004665?categoryId=')
html = driver.page_source
soup = BeautifulSoup(html)
temp =[]
try :    
    temp.append(soup.select_one('div.textSubject > h3').text.strip())
    temp.append(soup.select_one('div.price > dd:nth-child(2)').text.strip())
    temp.append(soup.select_one('div.price > dd:nth-child(4) > span > b').text.strip())
    searchList.append(temp)
except AttributeError as e :
    searchList.append(temp) 
driver.implicitly_wait(1000)
#국내산 애호박
driver.get('https://www.oasis.co.kr/product/detail/2362-1000608?categoryId=')
html = driver.page_source
soup = BeautifulSoup(html)
temp =[]
try :    
    temp.append(soup.select_one('div.textSubject > h3').text.strip())
    temp.append(soup.select_one('div.price > dd:nth-child(2)').text.strip())
    temp.append(soup.select_one('div.price > dd:nth-child(4) > span > b').text.strip())
    searchList.append(temp)
except AttributeError as e :
    searchList.append(temp) 
driver.implicitly_wait(1000)
#세척 햇 밤고구마
driver.get('https://www.oasis.co.kr/product/detail/7495-1004833?categoryId=')
html = driver.page_source
soup = BeautifulSoup(html)
temp =[]
try :    
    temp.append(soup.select_one('div.textSubject > h3').text.strip())
    temp.append(soup.select_one('div.price > dd:nth-child(2)').text.strip())
    temp.append(soup.select_one('div.price > dd:nth-child(4) > span > b').text.strip())
    searchList.append(temp)
except AttributeError as e :
    searchList.append(temp) 
driver.implicitly_wait(1000)
#호박고구마
driver.get('https://www.oasis.co.kr/product/detail/34458-1034436?categoryId=')
html = driver.page_source
soup = BeautifulSoup(html)
temp =[]
try :    
    temp.append('호구마')
    temp.append('13100원')
    searchList.append(temp)
except AttributeError as e :
    searchList.append(temp) 
driver.implicitly_wait(1000)
#무농약이상 시금치
driver.get('https://www.oasis.co.kr/product/detail/7466-1004801?categoryId=')
html = driver.page_source
soup = BeautifulSoup(html)
temp =[]
try :    
    temp.append(soup.select_one('div.textSubject > h3').text.strip())
    temp.append(soup.select_one('div.price > dd:nth-child(2)').text.strip())
    temp.append(soup.select_one('div.price > dd:nth-child(4) > span > b').text.strip())
    searchList.append(temp)
except AttributeError as e :
    searchList.append(temp) 
driver.implicitly_wait(1000)
#무농약당근
driver.get('https://www.oasis.co.kr/product/detail/4388-1001475?categoryId=')
html = driver.page_source
soup = BeautifulSoup(html)
temp =[]
try :    
    temp.append(soup.select_one('div.textSubject > h3').text.strip())
    temp.append(soup.select_one('div.price > dd:nth-child(2)').text.strip())
    temp.append(soup.select_one('div.price > dd:nth-child(4) > span > b').text.strip())
    searchList.append(temp)
except AttributeError as e :
    searchList.append(temp) 
driver.implicitly_wait(1000)
#국내산쪽파
driver.get('https://www.oasis.co.kr/product/detail/17511-1015257?categoryId=')
html = driver.page_source
soup = BeautifulSoup(html)
temp =[]
try :    
    temp.append(soup.select_one('div.textSubject > h3').text.strip())
    temp.append(soup.select_one('div.price > dd:nth-child(2)').text.strip())
    temp.append(soup.select_one('div.price > dd:nth-child(4) > span > b').text.strip())
    searchList.append(temp)
except AttributeError as e :
    searchList.append(temp) 
driver.implicitly_wait(1000)
#국내산알배기배추
driver.get('https://www.oasis.co.kr/product/detail/7341-1004668?categoryId=')
html = driver.page_source
soup = BeautifulSoup(html)
temp =[]
try :    
    temp.append(soup.select_one('div.textSubject > h3').text.strip())
    temp.append(soup.select_one('div.price > dd:nth-child(2)').text.strip())
    temp.append(soup.select_one('div.price > dd:nth-child(4) > span > b').text.strip())
    searchList.append(temp)
except AttributeError as e :
    searchList.append(temp) 
driver.implicitly_wait(1000)
#국내산 홍고추
driver.get('https://www.oasis.co.kr/product/detail/19976-1017986?categoryId=')
html = driver.page_source
soup = BeautifulSoup(html)
temp =[]
try :    
    temp.append(soup.select_one('div.textSubject > h3').text.strip())
    temp.append(soup.select_one('div.price > dd:nth-child(2)').text.strip())
    temp.append(soup.select_one('div.price > dd:nth-child(4) > span > b').text.strip())
    searchList.append(temp)
except AttributeError as e :
    searchList.append(temp) 
driver.implicitly_wait(1000)
#꽈리
driver.get('https://www.oasis.co.kr/product/detail/7345-1004672?categoryId=')
html = driver.page_source
soup = BeautifulSoup(html)
temp =[]
try :    
    temp.append(soup.select_one('div.textSubject > h3').text.strip())
    temp.append(soup.select_one('div.price > dd:nth-child(2)').text.strip())
    temp.append(soup.select_one('div.price > dd:nth-child(4) > span > b').text.strip())
    searchList.append(temp)
except AttributeError as e :
    searchList.append(temp) 
driver.implicitly_wait(1000)
#청양
driver.get('https://www.oasis.co.kr/product/detail/7472-1004808?categoryId=')
html = driver.page_source
soup = BeautifulSoup(html)
temp =[]
try :    
    temp.append(soup.select_one('div.textSubject > h3').text.strip())
    temp.append(soup.select_one('div.price > dd:nth-child(2)').text.strip())
    temp.append(soup.select_one('div.price > dd:nth-child(4) > span > b').text.strip())
    searchList.append(temp)
except AttributeError as e :
    searchList.append(temp) 
driver.implicitly_wait(1000)
#아삭이
driver.get('https://www.oasis.co.kr/product/detail/7344-1004671?categoryId=')
html = driver.page_source
soup = BeautifulSoup(html)
temp =[]
try :    
    temp.append(soup.select_one('div.textSubject > h3').text.strip())
    temp.append(soup.select_one('div.price > dd:nth-child(2)').text.strip())
    temp.append(soup.select_one('div.price > dd:nth-child(4) > span > b').text.strip())
    searchList.append(temp)
except AttributeError as e :
    searchList.append(temp) 
driver.implicitly_wait(1000)
#백오이3개
driver.get('https://www.oasis.co.kr/product/detail/12216-1009754?categoryId=')
html = driver.page_source
soup = BeautifulSoup(html)
temp =[]
try :    
    temp.append(soup.select_one('div.textSubject > h3').text.strip())
    temp.append(soup.select_one('div.price > dd:nth-child(2)').text.strip())
    temp.append(soup.select_one('div.price > dd:nth-child(4) > span > b').text.strip())
    searchList.append(temp)
except AttributeError as e :
    searchList.append(temp) 
driver.implicitly_wait(1000)

driver.close()

#배열 -> csv 병합
print('배열 병합 .. ')
f = open(f'./hellonature.csv', 'w', encoding='utf-8', newline='')
csvWriter = csv.writer(f)
for i in searchList:
    csvWriter.writerow(i)
f.close()
print('완료')      
time.sleep(1)

#엑셀 변환
print('엑셀 변환..')
wb = Workbook()
ws = wb.active
with open('./hellonature.csv', 'r', encoding='utf-8') as f:
    for row in csv.reader(f):
        ws.append(row)

wb.save('헬로네이처오아시스판매가.xlsx')
print('>>모든 작업 완료!')

