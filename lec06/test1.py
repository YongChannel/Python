class Healthinfo:
    def __init__(self, gender, height, weight):
        self.gender = gender
        self.height = height
        self.weight = weight

    def getStdWeight(self):
        if '남성' in self.gender:
            stdWeight = (self.height - 100) * 0.9
        if '여성' in self.gender:
            stdWeight = (self.height - 100) * 0.85
        return stdWeight

    def getObesity(self):
        obesity = self.weight / self.getStdWeight() * 100
        return obesity

    def getObesityStr(self):
        obesity = self.getObesity()
        if obesity <= 90:
            return "저체중"
        if 90 < obesity <= 110:
            return "표준체중"
        if 110 < obesity <= 130:
            return "경도비만"
        if 130 < obesity <= 150:
            return "중도비만"
        else:
            return "고도비만"

    def __str__(self):
        return f"건강정보: [{self.gender}, {self.height}cm, {self.weight}kg]"


player = Healthinfo('남성', 178, 85)
print(player)
print(player.getObesityStr())
