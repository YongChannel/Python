try:
    # Shift+Enter
    from lec11.Webcrawling import getRequestUrl
except:
    # Ctrl+F5
    from Webcrawling import getRequestUrl

# HTML 태그를 분석하는 모듈 BS4
# 터미널창 : pip install bs4
from bs4 import BeautifulSoup

url = 'https://www.naver.com'
html = getRequestUrl(url)
soup = BeautifulSoup(html, 'html.parser')  # bs4 객체 생성

soup.prettify()  # html 예쁘게 출력

with open('네이버.html', 'w', encoding='utf-8') as f:
    f.write(soup.prettify())

# 뉴스 스탠드 언론사명 가져오기
# find_all() 해당하는 태그를 모두 찾아서 리스트로 반환
newsTags = soup.find_all(
    'div', class_='thumb_box _NM_NEWSSTAND_THUMB _NM_NEWSSTAND_THUMB_press_valid')

for tag in newsTags:
    # find() 원하는 태그를 딱 하나 찾아줌
    imgTag = tag.find('img', class_='news_logo')
    # print(imgTag)
    print(imgTag['alt'])

# select() css셀럭터 방식 태그의 경로를 통해서 원하는 정보를 찾음
imgTags = soup.select(
    'div.thumb_box._NM_NEWSSTAND_THUMB._NM_NEWSSTAND_THUMB_press_valid > a.thumb > img.news_logo')
for tag in imgTags:
    print(tag['alt'])

# 태그를 찾는 방법
# 원하는 정보가 있는 태그를 분석
# 보통 태그를 구분하는 기준으로 클래스명 혹은 아이디 값으로 사용

find_all()  # 일치하는 모든 태그를 찾아 리스트로 반환
find_all(태그명, id=아이디값)  # 태그의 아이디가 있는 경우
find_all(태그명, class_=클래스값)  # 태그의 클래스 값이 있는 경우
find_all(태그명, attrs={속성명: 속성값})  # 태그의 클래스나 아이디가 없는 경우 특정 속성값을 통해 찾기

find()  # 일치하는 태그 딱 하나 찾는 함수
find(태그명, id=아이디값)  # 태그의 아이디가 있는 경우
find(태그명, class_=클래스값)  # 태그의 클래스 값이 있는 경우
find(태그명, attrs={속성명: 속성값})  # 태그의 클래스나 아이디가 없는 경우 특정 속성값을 통해 찾기

select()  # css셀럭터 방식 태그의 경로를 통해서 원하는 정보를 찾음
# select(태그명.클래스명 > 태그명 아이디값 > 태그명)

# 태그에서 속성값을 가져올때
tag['속성명']

# 태그에서 값을 가져오는 경우
tag.text
