# 1. 조건문
year = int(input())
num = 2022 - year + 1
if num >= 20:
    print('성인')
elif num >= 8:
    print('청소년')
else:
    print('어린이')

total = 0
for i in range(1, 101):
    if i % 3 == 0 and i % 7 == 0:
        total += i
print(total)

# 윤년 구하기
year = int(input())
if year % 4 == 0:
    if year % 100 != 0 or year % 400 == 0:
        print('윤년')
    else:
        print('평년')

# 2. 3항 연산자
# 변수 = 참 if 조건식 else 거짓
age, num = map(int, input().split())
test1 = '짝수' if age % 2 == 0 else '거짓'
test2 = '영' if num == 0 else ('양수' if num > 0 else '음수')
print(test1, test2)