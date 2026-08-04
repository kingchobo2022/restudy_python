print("=== 왕초보 은행 시스템 가동 ===")

class Account:
    default_interest_rate = 0.01

    def __init__(self, account_num, owner, balance = 0):
        self.account_num = account_num
        self.owner = owner
        self.balance = balance

    # 입금 메서드
    def deposit(self, amount):
        if amount <= 0:
            print(" 입금 금액은 0원보다 커야 합니다.")
            return False
        self.balance += amount
        print(f"[{self.owner} - {self.account_num}] {amount:,}원 입금 완료 (현재 잔액: {self.balance:,}원)")
        return True

    # 출금 메서드
    def withdraw(self, amount):
        if amount <= 0:
            print(" 출금 금액은 0보다 커야 합니다.")
            return False
        if self.balance < amount:
            print("[{self.owner}] 잔액이 부족합니다. (현재 잔액: {self.balance:,}원, 요청 금액: {amount:,}원)")        
            return False
        self.balance -= amount
        print(f"[{self.owner} - {self.account_num}] {amount:,}원 출금 완료 (남은 잔액: {self.balance:,}원)")
        return True

    def display_info(self):
        print(f"- 계좌번호: {self.account_num} | 예금주: {self.owner} | 잔액: {self.balance:,}원")


# 자식 클래스 : 자유 적금 계좌 (Account 상속)
class SavingAccount(Account):
    def __init__(self, account_num, owner, balance, target_amount):
        super().__init__(account_num, owner, balance)    
        self.target_amount = target_amount # 목표 금액
        self.is_matured = False # 만기 여부

    # 출금 메서드 오버라이딩 (만기 전 출금 불가 제한)
    def withdraw(self, amount):
        if not self.is_matured:
            print(f" [{self.owner}] 적금 만기 전에는 출금할 수 없습니다. (목표: {self.target_amount:,}원 / 현재: {self.balance:,}원)")
            return False
        return super().withdraw(amount)        

    # 이자 지급 기능 (신규 추가 메서드)    
    def apply_interest(self):
        interest = int(self.balance * Account.default_interest_rate)
        self.balance += interest
        print(f"[{self.owner}] 이자 {interest:,}원이 지급되었습니다. (현재 잔액: {self.balance:,}원)")

        # 목표 금액 달성 여부 확인
        if self.balance >= self.target_amount and not self.is_matured:
            self.is_matured = True
            print(f"축하합니다. [{self.owner}] 님, 적금 목표 금액({self.target_amount:,}원)을 달성하여 만기 처리되었습니다.")

    def display_info(self):
        status = "만기됨" if self.is_matured else "적금 진행 중"
        print(f"- [적금] 계좌번호: {self.account_num} | 예금주: {self.owner} | 잔액: {self.balance:,}원 / 목표: {self.target_amount:,}원 ({status})")


# 은행 관리 클래스
class Bank:
    def __init__(self, name):
        self.name = name
        self.accounts = [] # 등록된 계좌(Account 객체들) 수집 리스트

    # 계좌 등록
    def add_account(self, account):
        self.accounts.append(account)   
        print(f" {self.name} 에 [{account.owner}]님의 계좌({account.account_num})가 등록되었습니다.")         

    # 계좌 검색
    def find_account(self, account_num):
        for acc in self.accounts:
            if acc.account_num == account_num:
                return acc
        return None

    # 계좌간 이체 기능
    def transfer(self, sender_num, receiver_num, amount):
        sender = self.find_account(sender_num)
        receiver = self.find_account(receiver_num)    

        if not sender or not receiver:
            print("이체 실패: 존재하지 않는 계좌번호입니다.")
            return

        print("\n [계좌 이체 시도] {sender.owner} => {receiver.owner} ({amount:,}원)")        
        if sender.withdraw(amount):
            receiver.deposit(amount)
            print("계좌 이체가 성공적으로 완료되었습니다.")
        else:
            print("잔액 부족 또는 출근 제한으로 이체에 실패했습니다.")

    # 전체 계좌 출력
    def show_all_accounts(self):
        print("\n=====================================")
        print(f" {self.name} 전체 계좌 현황")
        print("\n=====================================")
        for acc in self.accounts:
            acc.display_info()
            print("\n=====================================")

#=============================================
# 메인 시나리오 테스트
#=============================================
if __name__ == "__main__":
    kakao_bank = Bank("카카오뱅크")

    # 계좌 생성 (일반 계좌 및 적금 계좌)
    acc1 = Account("100-01", "라이언", 50000)
    acc2 = Account("100-02", "춘식이", 10000)
    acc3 = SavingAccount("2002-01", "어피치", 95000, 100000)

    # 은행에 등록
    kakao_bank.add_account(acc1)
    kakao_bank.add_account(acc2)
    kakao_bank.add_account(acc3)

    # 기본 입출금 테스트
    print("\n --- [1. 기본 거래 테스트 ] ---")
    acc1.deposit(20000)
    acc3.withdraw(10000) # 만기 점 출금 시도 (실패해야 함)

    # 이자 지급 및 만기 달성 테스트
    print("\n --- [2. 이자 지급 및 만기 테스트 ] ---")
    acc3.apply_interest() # 95,000 + 1% 이자(950) = 95,950원
    acc3.deposit(5000) # 추가 입금으로 100,000원 돌파 -> 만기 달성!
    acc3.apply_interest()
    acc3.withdraw(20000) # 만기 후 출금 시도 (성공해야 함)

    # 계좌 간 이체 테스트
    print("\n --- [3. 계좌 이체 테스트 ] ---")
    kakao_bank.transfer("100-01", "100-02", 30000) # 라이언 -> 춘식이 3만원 이체

    # 최종 현황 출력
    kakao_bank.show_all_accounts()
    









            
