# 1. 반복문
numList = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for i in range(len(numList)):
    if numList[i] % 2 == 0:
        numList[i] = 0
print(numList)

for i, val in enumerate(numList):
    if i % 2 != 0:
        numList[i] = 0
print(numList)

nameList = ['이영호', '김택용', '송병구', '이제동']
num = 0
for i in nameList:
    if i[0] == '이':
        num += 1
print(num)

# 2. * 찍기
for i in range(len(nameList)):
    nameList[i] = nameList[i][0] + '*' * (len(nameList[i]) - 1)
print(nameList)

for i, val in enumerate(nameList):
    nameList[i] = val[0] + '*' * (len(val) - 1)
print(nameList)

# 3. 평균점수
koScores = [60, 78, 33, 98, 20]
enScores = [88, 22, 58, 90, 68]
maScores = [77, 49, 79, 34, 55]
midScores = [koScores, enScores, maScores]

# 과목별 평균점수 리스트
subNum = len(midScores)
subAvgs = []

for scores in midScores:
    avg = sum(scores) / len(scores)
    subAvgs.append(avg)
print(subAvgs)

# 학생별 평균점수 리스트
stuNum = len(midScores[0])
stuAvgs = [0] * stuNum

for scores in midScores:
    for i, val in enumerate(scores):
        stuAvgs[i] += val / subNum
print(stuAvgs)

# 4. 문자열 반복
for char in 'hello':
    print(char, end="")

for char in 'world'[::-1]:
    print(char, end="")

num1 = 12345
strNum = str(num1)
sumNum = 0
for i in strNum:
    sumNum += int(i)
print(sumNum)

# 5. while()
numBox = 0
while num1 != 0:
    numBox += (num1 % 10)
    num1 //= 10
print(numBox)

# 6. 동전 계산기
change = 1260
moneys = [500, 100, 50, 10]
for val in moneys:
    cnt = change // val
    change %= val
    print(f"{val}원: {cnt}개", end=" ")

# 7. 달력 만들기
days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

for i, val in enumerate(days):
    print(f"{i + 1}월", end="-")
    for j in range(1, val + 1):
        print(f"{j}일", end="")
        if j != val:
            print(f",", end="")
    print()

lastdays = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

for i, lastday in enumerate(lastdays):
    mon = i + 1
    print(f"{mon:0>2}월", end="-")
    for day in range(1, lastday + 1):
        print(f"{day:0>2}일", end="")
        if day != lastday:
            print(f",", end="")
    print()

# 8. 반복문 제어
for i in range(10):
    if i == 5:
        break
    print(i)

for i in range(10):
    if i % 3 == 0:
        continue
    print(i)

# for else
for i in range(10):
    print(i)
else:
    print('프로그램 종료')

for i in range(10):
    if i > 3:
        break
    print(i)
else:
    print('프로그램 종료')
