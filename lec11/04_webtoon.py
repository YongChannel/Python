try:
    # Shift+Enter
    from lec11.Webcrawling import getRequestUrl
except:
    # Ctrl+F5
    from Webcrawling import getRequestUrl

from bs4 import BeautifulSoup

url = 'https://comic.naver.com/webtoon/weekday'
html = getRequestUrl(url)
soup = BeautifulSoup(html, 'html.parser')

divTags = soup.select('div.col_inner') # 요일별 divTag

webDic = {}
weekList = ['월', '화', '수', '목', '금', '토', '일']

for week in weekList:
    webDic[week] = [] # 리스트 초기화

for week, div in zip(weekList, divTags): # 요일별 웹툰 제목
    aTags = div.select('ul > li> a.title')
    webDic[week] = [aTag.text for aTag in aTags]

from pprint import pprint
pprint(webDic)

import pandas as pd
# tempDic = {'월':[1, 2, 3], '화':[4, 5, 6, 7]}
# loca = pd.DataFrame().from_dict(tempDic, orient='index').T
# T는 전치행렬로 행과 열을 바꿔줌

df = pd.DataFrame().from_dict(webDic, orient='index').T

# csv 파일 포맷 저장
df.index.name = 'No' # 인덱스 이름 지정
df.head()
df.to_csv('./save/webtoon.csv', encoding='utf-8', index=True)

# json 파일 포맷으로 저장
df.to_json('./save/webtoon.json', orient='records', force_ascii=False, indent = 4)