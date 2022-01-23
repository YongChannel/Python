# 1. 예외 처리
for i in range(5):
    try:
        print(10 / i)
    except ZeroDivisionError:
        print('0으로 나눌 수 없음')

nums = ['10', '30', '100aa']
total = 0
for i in nums:
    try:
        total += int(i)
    except ValueError as w:
        print(w)
print(total)

# 2. 여러 예외 처리
nums = [0, 1, 2, 3]
for i in range(5):
    try:
        result = 10 / nums[i]
    except ZeroDivisionError as e1:
        print(e1)
        result = "INF"
    except IndexError as e2:
        print(e2)
        result = None
    print(result)

# 3. 다른 예외들을 같은 처리하는 경우
for i in range(5):
    try:
        result = 10 / nums[i]
    except (ZeroDivisionError, IndexError) as e:
        print(e)
    else:  # 예외가 발생하지 않은 경우 실행 구문
        print(result)

# 4. exception 모든 예외
nums = [0, 1, 2, 3]
for i in range(4):
    try:
        result = 10 / nums[i]
        print(e)
    except Exception as e:
        print(e)
    else:
        print(result)

# try except finally
# finally 문은 예외 발생 여부와 상관없이 실행
try:
    result = 10 / 0
except ZeroDivisionError as e:
    print(e)
finally:
    print('프로그램 종료')


def testFunc(num):
    try:
        result = 10 / num
    except ZeroDivisionError as e:
        print(e)
        return None
    finally:
        print('반드시 실행되는 구문')
    return result


testFunc(10)
testFunc(0)


# 5. 강제 예외 발생
# 두 정수가 담긴 문자열을 정수로 바꿔 더해주는 함수
# isdigit() 숫자인지 아닌지 판단
def num(str1, str2):
    if not str1.isdigit() or not str2.isdigit():
        raise ValueError('함수 인작 잘못')
    return int(str1) + int(str2)


try:
    print(num('a', '10'))
except Exception as e:
    print(e)

# assert
# isinstance(데이터, 타입명) 해당 데이터의 타입 여부를 체크하는 함수
print(isinstance(10, int))
print(isinstance(10, str))
print(isinstance('hello', int))
print(isinstance('hello', str))


def getListAvg(numList):
    assert isinstance(numList, list), '리스트가 아님'
    total = 0
    for val in numList:
        assert isinstance(val, int) or isinstance(val, float), '숫자가 아님'
        total += val
    return total / len(numList)


numList1 = [1, 2, 3, 4]
numList2 = 19
numList3 = [1, 'a', 2, 3]

print(getListAvg(numList1))
print(getListAvg(numList2))
print(getListAvg(numList3))
