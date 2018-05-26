import time
start = time.time()
from bs4 import BeautifulSoup
import urllib.request as req
import urllib.parse as par
from selenium import webdriver

word = input('検索用語:')
N = (int)(input('習得件数（目標）:'))

url = "https://www.instagram.com/explore/tags/" + par.quote_plus(word, encoding='utf-8')
link = req.urlopen(url)

browser = webdriver.Chrome('C:\selenium\Chromedriver')
browser.get(url)

instagram = []

for scroll_count in range(1,N):
   time.sleep(0.5)
   browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
   if scroll_count %3 == 0:
      soup = BeautifulSoup(browser.page_source, 'html.parser')
      res = soup.findAll('img')
      for elm in res:
         instagram.append(elm)
      print(len(set(instagram)))
   if len(set(instagram)) > N:
      break

print('習得件数',len(set(instagram)))
print('習得時間',time.time() - start)
print('習得件数（重複含む)',len(instagram))
print('重複度',(len(instagram)-len(set(instagram)))/len(instagram))

instagram = list(set(instagram))

elements = []

import re

for i in instagram:
   j = str(i)
   elements.append(j[10:j.find('" class=')])

print(elements[100])
browser.close() #ブラウザを閉じる
