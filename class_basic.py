print("=== RPG Game 캐릭터 생성 실습 ===")

# 클래스 정의
class Character:
    def __init__(self, name, job, hp):
        self.name = name
        self.job = job
        self.hp = hp

    # 상태 출력 메서드
    def show_info(self):
        print(f" 이름: {self.name} | 직업: {self.job} | HP: {self.hp}")

    # 피격 메서드
    def take_damage(self, damage):
        self.hp -= damage
        print(f" [{self.name}]님이 {damage}의 피해를 입었습니다! (남은 HP: {self.hp})")

# 클래스로부터 객체 생성
hero1 = Character("전사라이언", "전사", 100)
hero2 = Character("마법사춘식이", "마법사", 60)

print("\n[ 생성된 캐릭터 정보 ]")
hero1.show_info()
hero2.show_info()

print("\n[ 전투 진행 ]")
hero1.take_damage(20)
hero2.take_damage(35)


