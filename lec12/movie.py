import requests
from bs4 import BeautifulSoup

itemList = []
for page in range(1, 6):
    header = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.36'}
    data = requests.get(f'https://movie.naver.com/movie/point/af/list.naver?&page={page}',
                        headers=header)
    soup = BeautifulSoup(data.text, 'html.parser')

    trs = soup.select('tbody > tr')

    for tr in trs:
        title = tr.find('a', class_='movie color_b').text
        score = tr.find('em').text
        review = tr.find('br').next_sibling

        itemDic = {}
        itemDic['제목'] = title
        itemDic['평점'] = int(score)
        itemDic['댓글'] = review.replace('\n', '').replace('\t', '').strip()

        itemList.append(itemDic)

import pandas as pd

df = pd.DataFrame(itemList)
df.head()

df.to_csv('./save/movie.csv', encoding='utf-8', index=False)

df.to_json('./save/movie.json', orient='records', force_ascii=False, indent=4)
