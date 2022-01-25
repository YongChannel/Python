try:
    from lec11.Webcrawling import *
except:
    from Webcrawling import *

# 뉴스 1000건을 가져와서 저장(1000건 이상은 못가져옴)
searchStr = '청바지'
itemList = []
for start in range(1, 1000, 100):
    result = getNaverShop(searchStr, start, 100)  # start위치부터 100건의 뉴스
    for item in result['items']:
        itemDic = {}
        itemDic['상품명'] = item['title']
        itemDic['링크'] = item['link']
        itemDic['이미지링크'] = item['image']
        itemDic['최저가'] = item['lprice']
        itemDic['최고가'] = item['hprice']
        itemDic['브랜드명'] = item['brand']
        itemList.append(itemDic)

print('가져온 데이터 수 :', len(itemList))
itemList

# 데이터 저장
import pandas as pd

df = pd.DataFrame(itemList)  # 데이터프레임은 테이블 구조
df.head()  # 가장 앞에 있는 5개 데이터 조회

# csv 파일 포맷으로 저장
df.to_csv(f'./save/shop_{searchStr}_{len(itemList)}건.csv',
          encoding='utf-8', index=False)
# index : 데이터프레임의 인덱스 저장 유무

# json 파일 포맷으로 저장
df.to_json(f'./save/shop_{searchStr}_{len(itemList)}건.json',
           orient='records', force_ascii=False, indent=4)
# force_ascii : 한글 저장하기 위해 False
# indent : 데이터 4칸 띄어서 저장
