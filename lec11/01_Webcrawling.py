# from urllib import response
# import urllib.request
# from webbrowser import get
# # url를 통해서 웹정보를 가져오는 모듈(rest api)

# url = 'https://ac.search.naver.com/nx/ac?q=%ED%8C%8C%EC%9D%B4%EC%8D%AC&st=100'
# req = urllib.request.Request(url)
# # url 정보 및 헤더 정보를 담는 객체

# response = urllib.request.urlopen(req)
# # url을 통해서 데이터 요청

# if response.getcode() == 200: # 정상응답인 경우
#     print(response.read().decode('utf-8'))


import urllib.request  # URL를 통해서 웹정보를 가져오는 모듈(REST API)

url = 'https://ac.search.naver.com/nx/ac?q=%ED%94%BC%EC%9E%90&st=100'
req = urllib.request.Request(url)  # URL 정보 및 헤더정보 담는 객체
response = urllib.request.urlopen(req)  # URL를 통해서 데이터 요청
if response.getcode() == 200:  # 정상응답인 경우
    print(response.read().decode('utf-8'))

try:
    # Shift+Enter
    from lec11.Webcrawling import getRequestUrl
except:
    # Ctrl+F5
    from Webcrawling import getRequestUrl
data = getRequestUrl(url)
print(data)

# jsong 형태의 text 파일 => json 객체로 변경
import json

jsonData = json.loads(data)

jsonData['query']
jsonData['items']

print("<< 네이버 연관 검색어 가져오기 >>")
searchStr = input("검색어 입력 > ")
serviceUrl = "https://ac.search.naver.com/nx/ac?"
param = f'q={urllib.parse.quote(searchStr)}&st=100'
# urllib.parse.quote() : 문자열을 UTF-8 인코딩화
url = serviceUrl + param
result = getRequestUrl(url)
jsonResult = json.loads(result)

for item in jsonResult['items'][0]:
    print(item[0])
