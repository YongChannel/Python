import requests
from bs4 import BeautifulSoup

header = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.36'}
data = requests.get('https://finance.naver.com/item/sise_day.naver?code=005930&page=1', headers=header)
soup = BeautifulSoup(data.text, 'html.parser')

trs = soup.find_all('tr', attrs={'onmouseover': 'mouseOver(this)'})

for tr in trs:
    tds = tr.find_all('td')
    itemDic = {}
    itemDic['날짜'] = tds[0].text
    itemDic['종가'] = int(tds[1].text.replace(",", ""))

    itemDic['전일비'] = int(tds[2].text.replace(",", "").replace('\n', "").replace("\t", ""))
    img = tds[2].find('img')
    if img:
        if img['alt'] == '하락':
            itemDic['전일비'] = itemDic['전일비'] * -1

    itemDic['시가'] = int(tds[3].text.replace(",", ""))
    itemDic['고가'] = int(tds[4].text.replace(",", ""))
    itemDic['저가'] = int(tds[5].text.replace(",", ""))
    itemDic['거래량'] = int(tds[6].text.replace(",", ""))
    print(itemDic)
