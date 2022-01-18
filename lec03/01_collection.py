# 1. 튜플
fruits = ['딸기', '당근', '수박']
tu1 = tuple(fruits)
print(tu1)

num1 = [1, 2, 3]
num2 = ['1', '2', '3']
tuNum1 = tuple(num1)
tuNum2 = tuple(num2)
print(tuNum1, tuNum2)
print(list(tuNum1), list(tuNum2))

# 2. set()
setNum = {1, 2, 3}
setNum.add(4)
setNum.remove(1)
setNum.update([5, 6])
print(setNum)

# 3. 집합연산
fruits1 = {'딸기', '당근', '수박'}
fruits2 = {'딸기', '사과', '배'}
# 합집합
union = fruits1 | fruits2
# 교집합
inter = fruits1 & fruits2
# 차집합
diff = fruits1 - fruits2

# 4. 딕셔너리
person = {'name': '홍길동', 'age': 30, 'birth': '12/30'}
name = person['name']
age = person['age']
print(name, age)

name = person.get('name')
age = person.get('age')
addr = person.get('addr')
print(name, age, addr)

# 두 가지 차이
# 키 값이 없는 경우
# name = person['name'] 오류
# name = person.get('name') 오류 없음

# 딕셔너리 수정
person['age'] = 50
del person['birth']
print(person)

# 5. pop()
# 키 값이 없는 경우 디폴트 값 전달
person.pop('name')
print(person)

# 6. update()
info = {'addr': '수원시'}
person.update(info)
print(person)

# 7. key, value 요소 출력
# keys()
key = person.keys()
# values()
value = person.values()
print(key, value)
# items()
# key, value 한 쌍으로 튜플로 출력
item = person.items()
print(item)
