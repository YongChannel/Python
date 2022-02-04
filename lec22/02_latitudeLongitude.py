from lec11.Webcrawling import *
import json
import pandas as pd


def getGeoData(addr):
    serviceKey = 'FA0A93A9-78B8-3C6D-9001-E9C13E7FABB1'
    serviceUrl = 'http://api.vworld.kr/req/address?'
    param = 'service=address&request=getcoord&version=2.0&crs=epsg:4326'
    param += f'&address={urllib.parse.quote(addr)}'  # 주소 UTF-8인코딩
    param += f'&refine=true&simple=false&format=json&type=road&key={serviceKey}'
    url = serviceUrl + param
    result = getRequestUrl(url)
    if result:
        return json.loads(result)
    else:
        return None


# getGeoData('경기도 수원시 권선구 경수대로179번길 20')
# 홀리스카페 매장 주소 -> 위도,경도 바꾸기
df = pd.read_csv('C:/works/python/lec11/save/cafe.csv')
df.info()  # 541개의 데이터

# 주소 전처리
import re

addr = '강원도 원주시 호저면 마근거리길 110 (원주(춘천방향)휴게소) 옥산리 215'
re.split(r'[\,\(]', addr)
# ['강원도 원주시 호저면 마근거리길 110 ', '원주', '춘천방향)휴게소) 옥산리 215']

# apply() : 행별 데이터 변환, 람다식과 같이 많이 활용
df['전처리_주소'] = df['주소'].apply(lambda x: re.split(r'[\,\(]', x)[0])
df['전처리_주소'] = df['전처리_주소'].str.replace('.', "")
df['전처리_주소'] = df['전처리_주소'].str.strip()

# 위도, 경도 칼럼생성
df['위도'] = 0
df['경도'] = 0
df.head()

# 시리즈의 인덱스와 값이 대입되서 반복문
for i, addr in df['전처리_주소'].iteritems():
    print(i, addr)
    try:
        geoData = getGeoData(addr)
        xPos = geoData['response']['result']['point']['x']  # 경도
        yPos = geoData['response']['result']['point']['y']  # 위도
        df.loc[i, '경도'] = xPos
        df.loc[i, '위도'] = yPos
    except Exception as e:
        print(e)

df.head()
# 위도, 경도 값을 못 찾은 데이터 조회
df[df['위도'] == 0]  # [34 rows x 9 columns], 34개의 데이터는 못 찾음
df[df['위도'] == 0]['전처리_주소']
# 직접 인테넛에서 찾아서 기입 (수동) ..시간이 오래걸려서 생략

# 데이터저장
df.to_csv('./save/홀리스카페_위도경도.csv', index=False)
