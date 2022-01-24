# 클래스명 맨 앞자리는 대문자
class SoccerPlayer:
    # 생성자 함수: 객체 생성시 최초로 한번 실행되는 함수
    def __init__(self, name, position, backNum):
        # self 매개변수는 자기 자신의 객체를 가르킴
        # 클래스 내의 함수 선언시 매개변수로 self를 꼭 넣어야함
        self.name = name  # 클래스 내의 필드값
        self.position = position
        self.backNum = backNum

    def changeBackNum(self, newNum):
        print(f'선수 등번호 변경 {self.backNum} -> {newNum}')
        self.backNum = newNum

    # __str__(): print()에 객체를 넣을 시 출력되는 텍스트 설정
    def __str__(self):
        return f'Name: {self.name}, Position: {self.position}, backNum: {self.backNum}'


player1 = SoccerPlayer('손흥민', 'MF', 7)
# 객체 할당
print(player1)

player1.changeBackNum(15)
print(player1)


# 사각형
class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.area()
        self.round()

    def area(self):
        self.mulNum = self.width * self.height

    def round(self):
        self.sumNum = (self.width + self.height) * 2

    def __str__(self):
        return f'넓이: {self.mulNum}, 둘레: {self.sumNum}'


rect = Rectangle(3, 4)
print(rect)


class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def round(self):
        return (self.width + self.height) * 2

    def __str__(self):
        return f'넓이: {rect.area()}, 둘레: {rect.round()}'


rect = Rectangle(3, 4)
print(rect)

# 여러개 객체를 할당
sizeList = [(2, 5), (7, 1), (3, 3)]
rectList = [rect(w, h) for w, h in sizeList]

for r in rectList:
    print(r)
    print(f'사각형 넓이: {r.area()}')
    print(f'사각형 둘레: {r.round()}')
    print("-" * 30)

# 넓이를 기준으로 정렬해서 출력
rectList.sort(key=lambda x: x.area(), reverse=True)
for r in rectList:
    print(r)
    print(f'사각형 넓이: {r.area()}')
    print(f'사각형 둘레: {r.round()}')
    print("-" * 30)
