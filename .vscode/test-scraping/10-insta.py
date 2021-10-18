import requests
from bs4 import BeautifulSoup
import pymysql
from  selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time as time
import getpass
import urllib.request
import random
 
 
from time import sleep
 
import pandas as pd
import numpy as np
 
 
driver = webdriver.Chrome("D:\python\이전 크롬 드라이버\chromedriver85.exe")# Chromedriver PATH
driver.get("https://www.instagram.com/accounts/login/")
driver.maximize_window()
 
 
 
driver = webdriver.Chrome("D:\python\이전 크롬 드라이버\chromedriver85.exe")# Chromedriver PATH
driver.get("https://www.instagram.com/accounts/login/")
driver.maximize_window()
 
username = getpass.getpass("Input ID : ")# User ID
password = getpass.getpass("Input PWD : ")# User PWD, 특히 getpass를 통해서 비밀번호 정보를 숨길 수도 있다. 잘 배워두자 
hashTag = input("Input HashTag # : ")# Search #
 
 
 
 
element_id = driver.find_element_by_name("username")
element_id.send_keys(username)
element_password = driver.find_element_by_name("password")
element_password.send_keys(password)
 
sleep(1.5)