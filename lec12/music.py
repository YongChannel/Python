import requests
from bs4 import BeautifulSoup

itemList = []
for page in range(1, 5):
    header = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.36'}
    data = requests.get(f'https://www.genie.co.kr/chart/top200?ditc=D&ymd=20200403&hh=23&rtm=N&pg={page}',
                        headers=header)
    soup = BeautifulSoup(data.text, 'html.parser')

    trs = soup.select('#body-content > div.newest-list > div > table > tbody > tr')
    for song in trs:
        itemDic = {}
        itemDic['순위'] = song.select_one('td.number').text[0:3].strip()
        itemDic['제목'] = song.select_one('td.info > a.title.ellipsis').text.strip()
        itemDic['가수'] = song.select_one('td.info > a.artist.ellipsis').text.strip()

        itemList.append(itemDic)

import pandas as pd
df = pd.DataFrame(itemList)
df.head()

df.to_csv('./save/music.csv', encoding='utf-8', index=False)

df.to_json('./save/music.json', orient='records', force_ascii=False, indent = 4)