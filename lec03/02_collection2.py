# 1. zip()
# 리스트를 같은 인덱스끼리 묶음
# 리스트의 크기가 같아야 함
nums = [100, 200, 300]
names = ['홍길동', '임꺽정', '김현수']
zipList = list(zip(nums, names))
print(zipList)

for num, name in zipList:
    print(num, name)

# 각 학생의 평균값 출력
koScores = [60, 78, 33, 98, 20]
enScores = [88, 22, 58, 90, 68]
maScores = [77, 49, 79, 34, 55]

print(list(zip(koScores, enScores, maScores)))

for ko, en, ma in zip(koScores, enScores, maScores):
    avg = (ko + en + ma) / 3
    print(avg)

for scores in zip(koScores, enScores, maScores):
    print(scores, end=" ")
    avg = sum(scores) / len(scores)
    print(avg)

# 과일 key, value 딕셔너리 분리
fruits = ['사과', '사과', '사과', '딸기', '포도', '포도', '배']
nums = []
menus = set(fruits)
for i in menus:
    nums.append(fruits.count(i))

dic = {i: val for i, val in zip(menus, nums)}
print(dic)

fruitsSet = set(fruits)
fruitsDic = {}
for i in fruitsSet:
    fruitsDic[i] = fruits.count(i)
print(fruitsDic)

# set 예제
# 다음은 9월 ~ 11월까지 헬스장에 나간 날짜 중 월별 나간 횟수를 출력
healthDates = ['09/11', '09/12', '09/13', '10/01', '10/03', '11/20']
monList = []
for date in healthDates:
    monList.append(date[:2])

for mon in sorted(set(monList)):
    print(f"{mon}월 {monList.count(mon)}")

# dict 예제
memberDic = {'id01': ['홍길동', 30, '수원'], 'id02': ['임꺽정', 40, '전주'], 'id03': ['김하나', 25, '서울'],
             'id04': ['김두한', 60, '서울']}

# 서울에 사는 사람들의 정보 출력
for key, val in memberDic.items():
    if '서울' in val[2]:
        print(key, val)

# 등록된 회원들의 평균나이 출력
total = 0
for key, val in memberDic.items():
    total += val[1] / len(key)
print(total)

total = 0
for val in memberDic.values():
    total += val[1]
print(f"{total / len(memberDic)}")
