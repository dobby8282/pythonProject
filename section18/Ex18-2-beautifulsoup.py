'''
파일명: Ex18-2-beautifulsoup.py

BeautifulSoup
    HTML, XML 등의 마크업 언어를 파싱하는 라이브러리
    ex) <html>텍스트</html>

BeautifulSoup 설치방법
pip install beautifulsoup4

https://news.nate.com/rank?mid=n1000
'''

import requests
from bs4 import BeautifulSoup

url = 'https://news.nate.com/rank'
param = {'mid': 'n1000'}
response = requests.get(url, params=param)
html = response.text

soup = BeautifulSoup(html, 'html.parser')
tit_list = soup.find_all('h2')
for tit in tit_list:
    print(tit.text.strip())

