import requests

Naver_Id = 'tkXGoweTDHmazyJJBbuT'
Naver_Pw = 'H4yZI4JuU0'

keyword = '동화책'
url = 'https://openapi.naver.com/v1/search/shop.json'
headers = {'X-Naver-Client-Id': Naver_Id, 'X-Naver-Client-Secret': Naver_Pw}
params = {'query': keyword, 'display': 10, 'start': 1, 'sort': 'date'}

rep = requests.get(url, params=params, headers=headers)
jdata = rep.json()

itemList = []
for item in jdata['items']:
    itemDic = {}
    itemDic['제목'] = item['title'].replace('<b>', "").replace('</b>', "")
    itemDic['링크'] = item['link']
    itemDic['가격'] = item['lprice']
    itemDic['카테고리'] = item['category1']
    itemDic['판매처'] = item['mallName']

    itemList.append(itemDic)

import pandas as pd

df = pd.DataFrame(itemList)  # 데이터프레임은 테이블 구조
df.head()  # 가장 앞에 있는 5개 데이터 조회

# json 파일 포맷으로 저장
df.to_json(f'./save/shop_{keyword}.json', orient='records', force_ascii=False, indent=4)
