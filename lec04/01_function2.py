# 1. 값에 의한 호출
def testFunc(b):
    b = 3  # 지역변수


a = 7  # 전역변수
testFunc(a)
print(a)


# 2. 참조에 의한 호출
def testFunc2(numList):
    numList.append(10)
    numList[0] = -1
    numList = [1, 2, 3, 4]


nums = [1, 2]
testFunc2(nums)
print(nums)


# 3. 함수 내에서 함수 밖에 변수를 사용
def testFunc3():
    global a
    a = 10


a = 1
testFunc3()
print(a)


# 4. 함수의 가변인수로 매개변수의 개수가 정해져 있지 않고 사용하는 인수
# *: 가변인수 처리되어 여러개를 넣을 수 있음
# 가변인수로 들어오는 매개변수는 튜플로 묶어짐
# 가변인수는 함수 매개변수의 마지막의 위치
def testFunc4(sign, *arg):
    if sign == '+':
        return sum(arg)
    elif sign == '*':
        result = 1
        for val in arg:
            result *= val
        return result
    else:
        return None


result = testFunc4('+', 1, 2, 3, 4, 5)
print(result)
result = testFunc4('*', 1, 2, 3, 4, 5)
print(result)
result = testFunc4('-', 1, 2, 3, 4, 5)
print(result)


# 가변인수로 들어오는 매개변수는 딕셔너리로 묶어짐
def testFunc5(**kwargs):
    print(kwargs)


testFunc5(first=3, second=2, third=5)


# 재귀함수
# 자신을 재참조하는 함수

def fac(n):
    if n == 1:
        return 1
    else:
        return n * fac(n - 1)


num = int(input())
print(fac(num))


def fibo1(m):
    result = []

    for i in range(m):
        if i in [0, 1]:
            result.append(1)
        else:
            result.append(result[i - 1] + result[i - 2])

    return result[m - 1]


num2 = int(input())
print(fibo1(num2))

n = 10
Listfibo = [1, 1]
for i in range(2, n):
    Listfibo.append(Listfibo[i - 1] + Listfibo[i - 2])
print(Listfibo)

n = 10
Listfibo2 = [0] * n
Listfibo2[0], Listfibo2[1] = 1, 1
for i in range(2, n):
    Listfibo2[i] = Listfibo2[i - 1] + Listfibo2[i - 2]
print(Listfibo2)


# 최대공약수
# 유클리드 호제법
def gcd(a, b):
    if a % b == 0:
        return b
    else:
        return gcd(b, a % b)


def gcd2(a, b, c):
    return (a * b) / c


n = gcd(3, 12)
m = gcd2(3, 12, n)
print(n, m)

a, b = 192, 162
while a % b != 0:
    a, b = b, a % b

print(b)

# a, b 값 바꾸는 방법
a, b = 10, 20
temp = b
b = a
a = temp

# 파이썬에서 a, b 값 바꾸는 방법
a, b = 10, 20
a, b = b, a


# 년, 월, 일을 함수의 매개변수로 받고 요일을 리턴해주는 함수
# 제라의 공식
def getWeek(year, mon, day):
    if mon <= 2:
        year -= 1
        mon += 12

    a = year // 100
    b = year % 100

    week = ((21 * a // 4) + (5 * b // 4) + 26 * (mon + 1) // 10 + day - 1) % 7
    return week


# 임의의 달력 만들기
def leapyear(year):
    if year % 4 == 0:
        if year % 100 != 0 or year % 400 == 0:
            print('[윤년]')


def getMon(year, mon):
    lastdays = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    sel = lastdays[mon - 1]

    if mon <= 2:
        year -= 1
        mon += 12

    a = year // 100
    b = year % 100
    week = ((21 * a // 4) + (5 * b // 4) + 26 * (mon + 1) // 10) % 7 + 1

    print(f'{year + 1}년 {mon - 12}월')
    print('일  월  화  수  목  금  토')

    for k in range(week - 1):
        print("  ", end='  ')

    for i in range(1, sel + 1):
        print(f'{i:0>2}', end='  ')
        if week == 7:
            print()
            week = 0
        week += 1
    print()


print('year, mon 입력)', end=' ')
y, n = map(int, input().split())
getMon(y, n)
leapyear(y)
