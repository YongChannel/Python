import requests

Naver_Id = 'tkXGoweTDHmazyJJBbuT'
Naver_Pw = 'H4yZI4JuU0'

keyword = '동화책'
url = 'https://openapi.naver.com/v1/search/shop.json'
headers = {'X-Naver-Client-Id': Naver_Id, 'X-Naver-Client-Secret': Naver_Pw}
params = {'query': keyword, 'display': 10, 'start': 1, 'sort': 'date'}

r = requests.get(url, params=params, headers=headers)
j = r.json()



import requests
from bs4 import BeautifulSoup

header = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.36'}
data = requests.get('https://movie.naver.com/movie/point/af/list.naver?&page=1', headers=header)
soup = BeautifulSoup(data.text, 'html.parser')

trs = soup.select('tbody > tr')