try:
    from lec11.Webcrawling import getRequestUrl
except:
    from Webcrawling import getRequestUrl

from bs4 import BeautifulSoup
import pandas as pd

itemList = []
for page in range(1, 56):
    url = f'https://www.hollys.co.kr/store/korea/korStore2.do?pageNo={page}&sido=&gugun=&store='
    html = getRequestUrl(url)
    soup = BeautifulSoup(html, 'html.parser')
    trs = soup.select('tbody>tr')

    for tr in trs:
        try:
            tds = tr.find_all('td')
            itemDic = {}
            itemDic['지역'] = tds[0].text
            itemDic['매장명'] = tds[1].text
            itemDic['매장현황'] = tds[2].text
            itemDic['주소'] = tds[3].text
            itemDic['서비스'] = ''
            imgs = tds[4].find_all('img')
            if imgs != None:
                for img in imgs:
                    itemDic['서비스'] += img['alt'] + " "
            itemDic['서비스'] = itemDic['서비스'].strip()
            itemDic['전화번호'] = tds[5].text
            itemList.append(itemDic)
        except:
            continue

print('총 매장 개수 : ', len(itemList))

# 데이터 저장
# pip install pandas
# 대표적인 데이터 분석 관련 라이브러리

df = pd.DataFrame(itemList)
df.head()

# csv 파일 포맷으로 저장
df.to_csv('./save/cafe.csv', encoding='utf-8', index=False)
# index : 데이터프레임의 인덱스 저장 유무

# json 파일 포맷으로 저장
df.to_json('./save/cafe.json', orient='records', force_ascii=False, indent=4)
# force_ascii : 한글 저장하기 위해 False
# indent : 데이터 4칸 띄어서 저장
