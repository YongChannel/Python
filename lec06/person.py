# person.py
class Person:
    def __init__(self, name, age, gender, hobby):
        self.name = name
        self.age = age
        self.gender = gender
        self.hobby = hobby

    def introduce(self):
        print(f'제 이름은 {self.name}입니다.')
        print(f'나이는 {self.age}이고, {self.gender}입니다.')
        print(f'취미는 {self.hobby}입니다.')


# Person 클래스를 상속받아서 Employee 클래스 만듬
# 상속할 클래스(Person)는 부모 클래스라고 한다.
# 상속받을 클래스(Employee)는 자식 클래스라고 한다.
# 자식 클래스는 부모 클래스의 필드(변수들)과 메서드를 상속받는다.
class Employee(Person):
    def __init__(self, name, age, gender, hobby, job, salary, id):
        # super() 부모 클래스를 호출
        # super().__init__() #부모 클래스의 생성자 함수 호출
        # 자식은 부모를 상속받았기 때문에 부모의 생성자함수도
        # 반드시 호출해줘야 한다.
        super().__init__(name, age, gender, hobby)
        self.job = job  # 직종
        self.salary = salary  # 연봉
        self.id = id  # 사원번호

    def doWork(self):
        print(f'{self.job}일을 하는 중 입니다.')

    def introduce(self):  # 부모 메서드 재정의
        super().introduce()  # 부모 introduce() 메서드 호출
        print(f'사원번호 {self.id}이고, 직종은 {self.job}입니다.')
        print(f'연봉은 {self.salary}입니다.')

    # 파이썬 특수 메서드들
    def __str__(self):  # print()에 객체를 넣을 시 출력되는 문장
        return f'[사원번호: {self.id}, 이름: {self.name}]'

    def __len__(self):  # len()에 객체를 넣을 시 값 변환되는 것 결정
        return len(self.name)  # 이름의 길이를 리턴

    def __repr__(self):  # 객체가 컬렉션에 있는 경우 print()에 컬렉션을 넣을 시 출력되는 문장
        return f'(사원번호: {self.id}, 이름: {self.name})'

    def __hash__(self):  # 해시코드 정의 두 객체가 같은지 비교시 활용됨
        return hash(self.id) + hash(self.name)

    def __eq__(self, other):  # == 에 대한 동작 정의
        return self.id == other.id and self.name == other.name

    def __ne__(self, other):  # != 에 대한 동작 정의
        # return self.id != other.id
        return not self.__eq__(other)

    def __gt__(self, other):  # > 에 대한 동작 정의
        return self.id > other.id

    def __lt__(self, other):  # < 에 대한 동작 정의
        return self.id < other.id

    def __ge__(self, other):  # >= 에 대한 동작 정의
        # return self.id >= other
        return not self.__lt__(other)

    def __le__(self, other):  # <= 에 대한 동작 정의
        # return self.id <= other
        return not self.__gt__(other)
