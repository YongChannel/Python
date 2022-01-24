try:
    # shift + enter 로 실행시 기본경로를 최상위 폴더 경로로 잡음
    # 최상위 경로는 pythonstudy
    from lec06.person import Person, Employee
except:
    # ctrl + f5 기본실행, 기본경로는 현재 폴더로 잡음
    from person import Person, Employee

p1 = Person('홍길동', 30, '남자', '무술')
p2 = Person('김하나', 27, '여자', '독서')

p1.introduce()
p2.introduce()

print(p1)

e1 = Employee('임꺽정', 45, '남자', '등산', '영업', 5000, 2)
e2 = Employee('김현아', 30, '여자', '피아노', '디자인', 5500, 3)
e3 = Employee('장철수', 33, '남자', '게임', '개발', 6000, 10)

e1.introduce()
e2.introduce()
e3.introduce()

# 클래스 다형성: 부모 클래스의 introduce()가 있기 때문에
# Person 및 Person을 상속받은 클래스에서 모두 introduce() 호출가능
pList = [p1, p2, e1, e2, e3]
for p in pList:
    p.introduce()
    if isinstance(p, Employee):
        p.doWork()
    print('_' * 20)

print(e1)  # __str__
print(pList)  # __repr__
len(e1)  # __len__
e1 == e2
e1 != e2
e1 > e2
e1 < e2
e1 >= e2
e1 <= e2

e1.__hash__()
e2.__hash__()

e1 = Employee('임꺽정', 45, '남자', '등산', '영업', 5000, 2)
e2 = Employee('김현아', 30, '여자', '피아노', '디자인', 5500, 3)
e3 = Employee('장철수', 33, '남자', '게임', '개발', 6000, 10)
e4 = Employee('김현수', 33, '남자', '게임', '개발', 5500, 10)

eSet = {e1, e2, e3, e4}
print(eSet)
# 클래스 객체를 set과 같은 자료구조에 넣을 시 중복여부 되는 기준을 만들어야함
# __hash__(), __eq__()를 정의해야함
# __hash__()가 있는 이유는 숫자 비교가 빨라서, 먼저 hash코드로 비교 후 hash 코드가 같으면 __eq__() 다시한번 값 비교
