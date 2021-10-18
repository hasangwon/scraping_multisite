import csv
from urllib.parse import quote_plus
from bs4 import BeautifulSoup
from selenium import webdriver
import glob
import time
                    
# csv file merge
path = 'C:/PROJECTS/scraping_multisite/test-save/' #csv files route
merge_path = 'C:/PROJECTS/scraping_multisite/hn.csv' #save file

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
