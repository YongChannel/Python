from email import header
import urllib.request
import datetime

Naver_Id = 'tkXGoweTDHmazyJJBbuT'
Naver_Pw = 'H4yZI4JuU0'


def getRequestUrl(url, decoding='utf-8', header={}):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.36'}
    headers.update(header)
    req = urllib.request.Request(url, headers=headers)
    try:
        response = urllib.request.urlopen(req)
        if response.getcode() == 200:  # 정상응답
            print(f'[{datetime.datetime.now()}] Url Request Success')
            return response.read().decode(decoding)
    except Exception as e:
        print(e)
        print(f'[{datetime.datetime.now()}] Error for Url')


# 네이버 API 뉴스 정보 :
# searchStr : 검색어
# start : 시작위치
# display : 최대 출력 건수
import json


def getNaverNews(searchStr, start, display):
    serviceUrl = 'https://openapi.naver.com/v1/search/news.json'
    param = "?query=" + urllib.parse.quote(searchStr)
    param += f'&display={display}&start={start}'
    url = serviceUrl + param
    header = {'X-Naver-Client-Id': Naver_Id,
              'X-Naver-Client-Secret': Naver_Pw}
    result = getRequestUrl(url, header=header)
    if result:
        return json.loads(result)
    else:
        return None


def getNaverShop(searchStr, start, display):
    serviceUrl = 'https://openapi.naver.com/v1/search/shop.json'
    param = "?query=" + urllib.parse.quote(searchStr)
    param += f'&display={display}&start={start}'
    url = serviceUrl + param
    header = {'X-Naver-Client-Id': Naver_Id,
              'X-Naver-Client-Secret': Naver_Pw}
    result = getRequestUrl(url, header=header)
    if result:
        return json.loads(result)
    else:
        return None


def getNaverImg(searchStr, start, display, filter='all'):
    serviceUrl = 'https://openapi.naver.com/v1/search/image.json'
    param = "?query=" + urllib.parse.quote(searchStr)
    param += f'&display={display}&start={start}&filter={filter}'
    url = serviceUrl + param
    header = {'X-Naver-Client-Id': Naver_Id,
              'X-Naver-Client-Secret': Naver_Pw}
    result = getRequestUrl(url, header=header)
    if result:
        return json.loads(result)
    else:
        return None
