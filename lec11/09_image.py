try:
    from lec11.Webcrawling import *
except:
    from Webcrawling import *
import datetime
import re

# 뉴스 1000건을 가져와서 저장(1000건 이상은 못가져옴)
searchStr = '청바지'
itemList = []
for start in range(1, 500, 100):
    result = getNaverImg(searchStr, start, 100, 'small')

    for item in result['items']:
        itemDic = {}
        # 정규표현식 활용 -> 제목 한글만 남기도록
        itemDic['제목'] = item['title']
        itemDic['제목'] = re.sub(r'[^가-힣 ]+', "", itemDic['제목']).strip()
        itemDic['링크'] = item['link']
        m = re.search(r'\.([a-zA-Z]+?)$', itemDic['링크'])
        itemDic['확장자'] = m.group(1) if m != None else 'jpg'
        itemList.append(itemDic)

print('가져온 데이터 수 :', len(itemList))
itemList

# 데이터 저장
import os

# 폴더 만들기
path = f'./save/image/{searchStr}'
if not os.path.exists(path):
    os.makedirs(path)

for item in itemList:
    fileName = item['제목'] + "." + item['확장자']

    filePath = os.path.join(path, fileName)
    # filePath = path + "/" + fileName

    # url통해 파일다운
    urllib.request.urlretrieve(item['링크'], filePath)
    print(f'{fileName} 다운로드 완료')
