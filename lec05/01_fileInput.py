# 1. 텍스트 파일 읽기
# 파일 열기
f = open('C:\works\python\lec05\회원정보.txt', 'r', encoding='utf-8')
# utf-8 : 가변 길이 인코딩 방식 1~4byte 값을 동적으로 얻음
# r = 내용을 읽기만 할 때 사용
# w = 내용을 새로 작성할 때 사용
# a = 내용을 추가할 때 사용

# 파일 읽기
text = f.read()
print(text)
# 파일 닫기
f.close()

# 2. with 키워드
# 파일 닫기를 안해도 됨
with open('C:\works\python\lec05\회원정보.txt', 'r', encoding='utf-8') as f:
    lines = f.readlines()  # readlines() 한줄씩 읽어 리스트로 반환

for i, val in enumerate(lines):
    print(i, val.strip('\n').split(','))

# 회원 한 사람의 정보가 딕셔너리로 저장되고 모든 회원 정보를 리스트에 저장
members = []
with open('C:\works\python\lec05\회원정보.txt', 'r', encoding='utf-8') as f:
    lines = f.readlines()
    keyList = lines[0].strip('\n').split(',')

    for line in lines[1:]:
        valList = line.strip('\n').split(',')
        member = {}
        for key, val in zip(keyList, valList):
            member[key] = val
        members.append(member)

    print(keyList)
    print(members)
    print(members[0], members[0]['Name'])

# 수원시에 거주하는 사람 정보 출력
for i in members:
    if '수원' in i['Address']:
        print(i)

# 이름이 강동원인 사람 정보 출력
for i in members:
    if '강동원' in i['Name']:
        print(i)

# id가 id02인 사람의 주소를 부산광역시 해운대구 해운대동으로 수정
for i in members:
    if 'id02' in i['ID']:
        i['Address'] = '부산광역시 해운대구 해운대동'
print(members)


# 3. lambda 식 활용
def printCondVal(data, cond):
    for v in data:
        if cond(v):
            print(v)


def alterConVal(data, cond, key, val):
    for v in data:
        if cond(v):
            v[key] = val


printCondVal(members, lambda x: '수원' in x['Address'])
printCondVal(members, lambda x: '강동원' == x['Name'])
alterConVal(members, lambda x: 'id02' == x['ID'], 'Address', '수원시 권선구 세류동')
alterConVal(members, lambda x: '전지현' == x['Name'], 'Phone', '123456789')
print(members)

# 4. 텍스트 파일 쓰기
with open('C:\works\python\lec05\텍스트 파일 쓰기.txt', 'w', encoding='utf-8') as f:
    # write() 한줄을 쓰고 개행함
    f.write(f"{0}번째 줄 입니다.\n")
    for i in range(1, 10):
        f.write(f"{i}번째 줄 입니다.\n")

with open('C:\works\python\lec05\텍스트 파일 쓰기.txt', 'a', encoding='utf-8') as f:
    for i in range(10, 20):
        f.write(f"{i}번째 줄 입니다.\n")
# w 모드: 기존 내용을 지우고 파일 처음부터 내용을 씀
# a 모드: 파일 내용 끝에서 부터 새로운 내용을 추가

with open('C:\works\python\lec05\수정된 회원정보.txt', 'w', encoding='utf-8') as f:
    keyList = members[0].keys()
    text = ','.join(keyList) + '\n'
    f.write(text)
    print(keyList)
    print(text)

    for member in members:
        valList = member.values()
        text = ','.join(valList) + '\n'
        f.write(text)

# 5. pickle 모듈
# 객체(리스트, 딕셔너리, 클래스 등) 저장 및 불러오기
import pickle

# 객체 저장
with open('C:\works\python\lec05\members.pickle', 'wb') as f:
    pickle.dump(members, f)

# 객체 불러오기
with open('C:\works\python\lec05\members.pickle', 'rb') as f:
    loadData = pickle.load(f)
print(loadData)

# 6. 폴더 만들기
import os

path = 'C:\works\python\lec05'
os.makedirs(path + "/대전")

if not os.path.exists(path + "/대전"):
    os.makedirs(path + "/대전")
