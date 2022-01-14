# 1. 자료형
# 정수형
intNum = 3
print(intNum)

# 실수형
floatNum = 3.14
print(floatNum)

# 문자형
strChar = 'hello'
print(strChar)

# 논리형
boolLog = True
boolLog2 = False
print(boolLog, boolLog2)


# 2. 연산자
num1 = 1
num2 = 2
num3 = 3
num4 = 4

num1 += 2
num2 -= 2
num3 *= 2
print(num1, num2, num3)

num1 **= 2
num2 /= 2
num3 //= 2
num4 %= 2
print(num1, num2, num3, num4)


# 3. 형변환
# char < short < int < long < float < double
num1 = 10
num2 = 20
num3 = 3.14
str1 = '5'
str2 = '3.14'

print(num1 / num2, int(num1 / num2))
print(float(num1), int(num3))
print(int(str1), float(str2))
print(int(float(str2)))

num4 = 3.14
num5 = 5
str3 = str(num3)

print(str(num4), str(num5))
print(type(str3))
