from cgitb import reset
import datetime

try:
    from lec11.Webcrawling import *
except:
    from Webcrawling import *

# 뉴스 1000건을 가져와서 저장(1000건 이상은 못가져옴)
searchStr = '코로나'
itemList = []
for start in range(1, 1000, 100):
    result = getNaverNews(searchStr, start, 100)  # start위치부터 100건의 뉴스
    for item in result['items']:
        newsDic = {}
        newsDic['제목'] = item['title'].replace('<b>', "").replace('</b>', "")

        # 데이터 전처리 : 불필요한 데이터 제거, 데이터를 원하는 형태로 바꿈
        newsDic['요약'] = item['description'].replace('<b>', "").replace('</b>', "").replace("&quot;", "")
        newsDic['링크'] = item['link']
        newsDic['날짜'] = item['pubDate']

        # 문자열->datetime으로 바꿈
        date = datetime.datetime.strptime(newsDic['날짜'], '%a, %d %b %Y %H:%M:%S +0900')
        # 문자열의 날짜 형식 %a(요일), %d(day), 등등
        # 'Fri, 21 Jan 2022 09:56:00 +0900'
        # datetime -> 우리가 원하는 날짜 형식의 문자열
        dateStr = date.strftime("%Y-%m-%d %H:%M:%S")
        newsDic['날짜'] = dateStr

        itemList.append(newsDic)

print('가져온 뉴스 수 :', len(itemList))
newsDic

# 데이터 저장
# pip install pandas
# 대표적인 데이터 분석 관련 라이브러리

import pandas as pd

df = pd.DataFrame(itemList)  # 데이터프레임은 테이블 구조
df.head()  # 가장 앞에 있는 5개 데이터 조회

# csv 파일 포맷으로 저장
df.to_csv(f'./save/news_{searchStr}_{len(itemList)}건.csv', encoding='utf-8', index=False)

# json 파일 포맷으로 저장
df.to_json(f'./save/news_{searchStr}_{len(itemList)}건.json', orient='records', force_ascii=False, indent=4)

# force_ascii: 한글 저장하기 위해 false
# indent: 데이터 4칸 띄어서 저장
