print("== 게임 유닛 상속 및 오버라이딩 실습 ==")

class Unit:
    def __init__(self, name, hp, speed):
        self.name = name
        self.hp = hp
        self.speed = speed

    def move(self):
        print(f"[{self.name}] 유닛이 지상으로 속도 {self.speed}로 이동합니다.")

    def take_damage(self, damage):
        self.hp -= damage
        print(f"[{self.name}] 유닛이 {damage}의 피해를 입었습니다. (남은 HP: {self.hp})")

class Marine(Unit):
    def __init__(self, name, hp=40, speed=1):
        super().__init__(name, hp , speed)

    def stimpack(self):
        self.hp -= 10
        self.speed += 1
        print(f"[{self.name}] 스팀팩 사용! 체력 -10, 이동속도 {self.speed}로 증가!")

class Dropship(Unit):
    def __init__(self, name, hp=150, speed=3):
        super().__init__(name, hp, speed)

    def move(self):
        print(f"[{self.name}] 드랍쉽이 공중으로 속도 {self.speed}로 날아갑니다!")       

m1 = Marine("마린1")
d1 = Dropship("드랍쉽1")

print("유닛 이동 테스트")
m1.move()
d1.move()

print("유닛 독자 기능 및 데미지 테스트")
m1.stimpack()
m1.take_damage(15)
d1.take_damage(50)