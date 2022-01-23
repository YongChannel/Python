# 1. 함수의 리턴값 여러개 주기
def testFunc():
    return 1, 2, 3


testFunc()
a, b, c = testFunc()
print(a, b, c)

# 2. 리스트 컴프리헨션
# 기존 리스트를 활용하여 새로운 리스트를 만드는 방법
nums = []
for i in range(10, 0, -2):
    nums.append(i)
print(nums)

nums1 = [i for i in range(10, 0, -2)]
print(nums1)

# 조건문을 통한 값 필터링
evenList = [i for i in range(10) if i % 2 == 0]
print(evenList)

# 3. 3항 연산자 활용
nums = [0 if i % 2 == 0 else 1 for i in range(10)]
numsList = []
for i in range(10):
    nums = 0 if i % 2 == 0 else 1
    numsList.append(nums)
print(numsList)

# 알파벳 리스트
alphaList = [chr(ord('a') + i) for i in range(26)]
# ord(문자): 아스키코드 정수값으로 반환
# chr(숫자): 아스키코드 문자값으로 반환
print(alphaList)

# 기존 리스트를 통해 새로운 리스트 생성
nums = [1, 2, 3, 4, 5]
numSquares = [num * num for num in nums]
print(numSquares)

# 이름에 *처리한 리스트 만들기
names = ['홍길동', '김구', '임꺽정']
secretNames = [name[0] + '*' * (len(name) - 1) for name in names]
print(secretNames)

# 과일명 및 과일 개수를 튜플 형태로 리스트 만들기
fruits = ['사과', '사과', '딸기', '포도', '딸기', '사과']
fruitsList = [(f, fruits.count(f) for i in set(fruits))]
print(fruitsList)

# 4. 중첩 반복문
rowCols = [(row, col) for row in range(5) for col in range(6)]
print(rowCols)

rowCols = []
for row in range(5):
    for col in range(6):
        rowCols.append((row, col))

# 2차원 리스트 만들기
tSpaceList = [[0] * 7 for i in range(6)]
tSpaceList = [[0, 0, 0, 0, 0, 0, 0] for i in range(6)]
print(tSpaceList)


# 1. 함수의 리턴값 여러개 주기
def testFunc():
    return 1, 2, 3


testFunc()
a, b, c = testFunc()
print(a, b, c)

# 2. 리스트 컴프리헨션
# 기존 리스트를 활용하여 새로운 리스트를 만드는 방법
nums = []
for i in range(10, 0, -2):
    nums.append(i)
print(nums)

nums1 = [i for i in range(10, 0, -2)]
print(nums1)

# 조건문을 통한 값 필터링
evenList = [i for i in range(10) if i % 2 == 0]
print(evenList)

# 3. 3항 연산자 활용
nums = [0 if i % 2 == 0 else 1 for i in range(10)]
numsList = []
for i in range(10):
    nums = 0 if i % 2 == 0 else 1
    numsList.append(nums)
print(numsList)

# 알파벳 리스트
alphaList = [chr(ord('a') + i) for i in range(26)]
# ord(문자): 아스키코드 정수값으로 반환
# chr(숫자): 아스키코드 문자값으로 반환
print(alphaList)

# 기존 리스트를 통해 새로운 리스트 생성
nums = [1, 2, 3, 4, 5]
numSquares = [num * num for num in nums]
print(numSquares)

# 이름에 *처리한 리스트 만들기
names = ['홍길동', '김구', '임꺽정']
secretNames = [name[0] + '*' * (len(name) - 1) for name in names]
print(secretNames)

# 과일명 및 과일 개수를 튜플 형태로 리스트 만들기
fruits = ['사과', '사과', '딸기', '포도', '딸기', '사과']
fruitsList = [(f, fruits.count(f) for i in set(fruits))]
print(fruitsList)

# 4. 중첩 반복문
rowCols = [(row, col) for row in range(5) for col in range(6)]
print(rowCols)

rowCols = []
for row in range(5):
    for col in range(6):
        rowCols.append((row, col))

# 2차원 리스트 만들기
tSpaceList = [[0] * 7 for i in range(6)]
tSpaceList = [[0, 0, 0, 0, 0, 0, 0] for i in range(6)]
print(tSpaceList)

# zip함수 활용 여러개 리스트 동시 처리
koList = [30, 55, 98, 24]
enList = [90, 10, 50, 77]
maList = [80, 20, 50, 90]
# 각 학생의 평균값 리스트
avgList = [sum(scores) / len(scores) for scores in zip(koList, enList, maList)]
print(avgList)

# 리스트 언팽킹 활용
# 2차원 리스트인 경우 *의 언패킹 방법을 활용해 같은 인덱스 끼리 연산 가능
midtermList = [koList, enList, maList]
print(midtermList)
print(*midtermList)
avgList = [sum(scores) / len(scores) for scores in zip(*midtermList)]
print(avgList)

# 5. 람다식
lambda 매개변수: 리턴값


# 1. 함수의 리턴값 여러개 주기
def testFunc():
    return 1, 2, 3


testFunc()
a, b, c = testFunc()
print(a, b, c)

# 2. 리스트 컴프리헨션
# 기존 리스트를 활용하여 새로운 리스트를 만드는 방법
nums = []
for i in range(10, 0, -2):
    nums.append(i)
print(nums)

nums1 = [i for i in range(10, 0, -2)]
print(nums1)

# 조건문을 통한 값 필터링
evenList = [i for i in range(10) if i % 2 == 0]
print(evenList)

# 3. 3항 연산자 활용
nums = [0 if i % 2 == 0 else 1 for i in range(10)]
numsList = []
for i in range(10):
    nums = 0 if i % 2 == 0 else 1
    numsList.append(nums)
print(numsList)

# 알파벳 리스트
alphaList = [chr(ord('a') + i) for i in range(26)]
# ord(문자): 아스키코드 정수값으로 반환
# chr(숫자): 아스키코드 문자값으로 반환
print(alphaList)

# 기존 리스트를 통해 새로운 리스트 생성
nums = [1, 2, 3, 4, 5]
numSquares = [num * num for num in nums]
print(numSquares)

# 이름에 *처리한 리스트 만들기
names = ['홍길동', '김구', '임꺽정']
secretNames = [name[0] + '*' * (len(name) - 1) for name in names]
print(secretNames)

# 과일명 및 과일 개수를 튜플 형태로 리스트 만들기
fruits = ['사과', '사과', '딸기', '포도', '딸기', '사과']
fruitsList = [(f, fruits.count(f) for i in set(fruits))]
print(fruitsList)

# 4. 중첩 반복문
rowCols = [(row, col) for row in range(5) for col in range(6)]
print(rowCols)

rowCols = []
for row in range(5):
    for col in range(6):
        rowCols.append((row, col))

# 2차원 리스트 만들기
tSpaceList = [[0] * 7 for i in range(6)]
tSpaceList = [[0, 0, 0, 0, 0, 0, 0] for i in range(6)]
print(tSpaceList)


# 1. 함수의 리턴값 여러개 주기
def testFunc():
    return 1, 2, 3


testFunc()
a, b, c = testFunc()
print(a, b, c)

# 2. 리스트 컴프리헨션
# 기존 리스트를 활용하여 새로운 리스트를 만드는 방법
nums = []
for i in range(10, 0, -2):
    nums.append(i)
print(nums)

nums1 = [i for i in range(10, 0, -2)]
print(nums1)

# 조건문을 통한 값 필터링
evenList = [i for i in range(10) if i % 2 == 0]
print(evenList)

# 3. 3항 연산자 활용
nums = [0 if i % 2 == 0 else 1 for i in range(10)]
numsList = []
for i in range(10):
    nums = 0 if i % 2 == 0 else 1
    numsList.append(nums)
print(numsList)

# 알파벳 리스트
alphaList = [chr(ord('a') + i) for i in range(26)]
# ord(문자): 아스키코드 정수값으로 반환
# chr(숫자): 아스키코드 문자값으로 반환
print(alphaList)

# 기존 리스트를 통해 새로운 리스트 생성
nums = [1, 2, 3, 4, 5]
numSquares = [num * num for num in nums]
print(numSquares)

# 이름에 *처리한 리스트 만들기
names = ['홍길동', '김구', '임꺽정']
secretNames = [name[0] + '*' * (len(name) - 1) for name in names]
print(secretNames)

# 과일명 및 과일 개수를 튜플 형태로 리스트 만들기
fruits = ['사과', '사과', '딸기', '포도', '딸기', '사과']
fruitsList = [(f, fruits.count(f) for i in set(fruits))]
print(fruitsList)

# 4. 중첩 반복문
rowCols = [(row, col) for row in range(5) for col in range(6)]
print(rowCols)

rowCols = []
for row in range(5):
    for col in range(6):
        rowCols.append((row, col))

# 2차원 리스트 만들기
tSpaceList = [[0] * 7 for i in range(6)]
tSpaceList = [[0, 0, 0, 0, 0, 0, 0] for i in range(6)]
print(tSpaceList)

# zip함수 활용 여러개 리스트 동시 처리
koList = [30, 55, 98, 24]
enList = [90, 10, 50, 77]
maList = [80, 20, 50, 90]
# 각 학생의 평균값 리스트
avgList = [sum(scores) / len(scores) for scores in zip(koList, enList, maList)]
print(avgList)

# 리스트 언팽킹 활용
# 2차원 리스트인 경우 *의 언패킹 방법을 활용해 같은 인덱스 끼리 연산 가능
midtermList = [koList, enList, maList]
print(midtermList)
print(*midtermList)
avgList = [sum(scores) / len(scores) for scores in zip(*midtermList)]
print(avgList)

# 5. 람다식
# lambda 매개변수:리턴값
func = lambda x, y: x + y
result = func(3, 4)
print(result)

fruitsList = [('딸기', 2), ('포도', 1), ('사과', 3)]
fruitsList.sort()
print(fruitsList)
fruitsList.sort(key=lambda x: x[1])
fruitsList.sort(key=lambda x: x[1], reverse=True)
print(fruitsList)

# 사각형의 (가로,세로)
rectList = [(10, 3), (5, 4), (9, 2)]
# 가로 값 기준 정렬
sorted(rectList, key=lambda x: x[0])
# 세로 값 기준 정렬
sorted(rectList, key=lambda x: x[1])
# 넓이값 기준 정렬
sorted(rectList, key=lambda x: x[0] * x[1])
print(rectList)


# 6. 람다식 활용
def printCondList(dataList, cond):
    for v in dataList:
        if cond(v):
            print(v)


nums = [1, 2, 3, 4, 5, 6]
printCondList(nums, lambda x: x % 2 == 0)

# (차명, 연식, 가솔린 여부)
carList = [('소나타', 10, True), ('그렌저', 5, False), ('모닝', 3, True), ('티볼리', 4, True), ('qm6', 6, False)]
# 연식이 5년 이하인 자동차만 출력
printCondList(carList, lambda x: x[1] <= 5)
# 연식이 5년 이하면서 가솔린이 아닌 차만 출력
printCondList(carList, lambda x: x[1] <= 5 and x[2] == False)
