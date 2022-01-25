import requests

Naver_Id = 'tkXGoweTDHmazyJJBbuT'
Naver_Pw = 'H4yZI4JuU0'

keyword = '고양이'
url = 'https://openapi.naver.com/v1/search/image.json'
headers = {'X-Naver-Client-Id': Naver_Id, 'X-Naver-Client-Secret': Naver_Pw}

params = {'query': keyword, 'display': 100, 'start': 1, 'sort': 'date', 'filter': 'medium'}

rep = requests.get(url, params=params, headers=headers)
jdata = rep.json()

itemList = []
for item in jdata['items']:
    imageDic = {}
    imageDic['이름'] = item['title']
    imageDic['링크'] = item['link']

    itemList.append(imageDic)

