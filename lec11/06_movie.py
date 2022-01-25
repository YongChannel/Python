try:
    # Shift+Enter
    from dataSave.Webcrawling import getRequestUrl
except:
    # Ctrl+F5
    from Webcrawling import getRequestUrl

from bs4 import BeautifulSoup

itemList = []
for page in range(1, 10):
    url = f'https://movie.naver.com/movie/point/af/list.naver?&page={page}'
    html = getRequestUrl(url)
    html  # 잘 불러왔는지 확인 (인코딩 정보나 다른 요인에 의해서 못불러옴)

    soup = BeautifulSoup(html, 'html.parser')
    trs = soup.select('tbody > tr')

    for tr in trs:
        try:
            title = tr.find('a', class_='movie color_b').text
            score = tr.find('em').text
            review = tr.find('br').next_sibling  # next_sibling 형제 태그 찾기
            # review
            # br 태그 바로 뒤에있는 요소를 가져옴 => 댓글
            itemDic = {}
            itemDic['제목'] = title
            itemDic['평점'] = int(score)
            itemDic['댓글'] = review.replace('\n', '').replace('\t', '').strip()
            itemDic
            itemList.append(itemDic)
        except Exception as e:
            print(e)

# Quiz 1) itemList에 중복없이 몇개의 영화제목이 있는지
# Quiz 2) '스파이더맨: 노 웨이 홈'의 평균 평점
# Quiz 3) 영화별 평균평점을 딕셔너리로 저장
# Ex) {'스파이더맨: 노 웨이 홈':7, '이터널스':5, ...}


# 중복없이 몇 개의 영화제목이 있는지
titles = [item['제목'] for item in itemList]
titleset = set(titles)
len(titleset)

# titles = []
# for item in itemList:
#     titles.append(item['제목'])


# 스파이더맨 노웨이 홈의 평균 평점
scores = [item['평점'] for item in itemList if item['제목'] == '스파이더맨: 노 웨이 홈']
scores
avg = sum(scores) / len(scores)
avg

# 영화별 평균 평점을 딕셔너리로 저장
movieScoreDic = {}
for title in titleset:
    scores = [item['평점'] for item in itemList if item['제목'] == title]
    avg = sum(scores) / len(scores)
    movieScoreDic[title] = avg

movieScoreDic

# 데이터 저장
import pandas as pd

df = pd.DataFrame(itemList)  # 데이터프레임은 테이블 구조
df.head()  # 가장 앞에 있는 5개 데이터 조회

# 제목의 갯수
df['제목'].unique()  # 제목의 중복없이 데이터 보여줌
len(df['제목'].unique())  # 48

# 제목별 평점의 평균점수 구하기
df.groupby(['제목'])['평점'].mean()

# csv 파일 포맷으로 저장
df.to_csv(f'./save/movie.csv', encoding='utf-8', index=False)

# json 파일 포맷으로 저장
df.to_json('./save/movie.json', orient='records', force_ascii=False, indent = 4)