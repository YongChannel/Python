# 입력이 있고 출력이 없는 함수
def say_myself(name, old, gender):
    print(f"이름: {name}, 나이: {old}, 성별: {gender}")


say_myself('yong', 27, '남자')


# 함수의 매개변수 디폴트 값 설정
def say_myself(name, old=20, gender='여자'):
    print(f"이름: {name}, 나이: {old}, 성별: {gender}")


say_myself('김태희')
say_myself('김태희', 30)

# 세개의 숫자를 매개변수로 받아서 가장 큰 값을 리턴해주는 함수
num1, num2, num3 = map(int, input().split())


def numCheck1(data1, data2, data3):
    num = [data1, data2, data3]
    num.sort()
    return num[len(num) - 1]


print(numCheck1(num1, num2, num3))

# 리스트를 입력 받아서 평균값을 리턴해주는 함수
numList = list(map(int, input().split()))


def numCheck2(data):
    result = sum(data) / len(data)
    return result


print(numCheck2(numList))

# 저항값을 리스트로 매개변수로 받아서 병렬저항의 합을 리턴해주는 함수
numList = list(map(int, input().split()))


def numCheck3(data):
    a = 0
    for i in data:
        a += 1 / i
    result = 1 / a
    return result


print(numCheck3(numList))
