try:
    # Shift+Enter
    from lec11.Webcrawling import getRequestUrl
except:
    # Ctrl+F5
    from Webcrawling import getRequestUrl

from bs4 import BeautifulSoup

itemList = []
for page in range(1, 10):
    url = f'https://finance.naver.com/item/sise_day.naver?code=005930&page={page}'
    html = getRequestUrl(url, decoding='euc-kr')
    html  # 잘 불러왔는지 확인 (인코딩 정보나 다른 요인에 의해서 못불러옴)

    soup = BeautifulSoup(html, 'html.parser')
    trs = soup.find_all('tr', attrs={'onmouseover': 'mouseOver(this)'})
    trs
    for tr in trs:
        try:
            tds = tr.find_all('td')
            itemDic = {}
            itemDic['날짜'] = tds[0].text
            itemDic['종가'] = int(tds[1].text.replace(",", ""))

            itemDic['전일비'] = int(tds[2].text.replace(
                ",", "").replace('\n', "").replace("\t", ""))
            img = tds[2].find('img')
            if img:
                if img['alt'] == '하락':
                    itemDic['전일비'] = itemDic['전일비'] * -1
            itemDic['시가'] = int(tds[3].text.replace(",", ""))
            itemDic['고가'] = int(tds[4].text.replace(",", ""))
            itemDic['저가'] = int(tds[5].text.replace(",", ""))
            itemDic['거래량'] = int(tds[6].text.replace(",", ""))
            itemList.append(itemDic)
        except Exception as e:
            print(e)

import pandas as pd

# 데이터 저장
df = pd.DataFrame(itemList)  # 데이터프레임은 테이블 구조
df.head()  # 가장 앞에 있는 5개 데이터 조회

# csv 파일 포맷으로 저장
df.to_csv(f'./save/samsung {itemList[-1]["날짜"]}~{itemList[0]["날짜"]}.csv', encoding='utf-8', index=False)

# json 파일 포맷으로 저장
df.to_json(f'./save/samsung {itemList[-1]["날짜"]}~{itemList[0]["날짜"]}.json', orient='records', force_ascii=False, indent = 4)