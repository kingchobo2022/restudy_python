print("=== ATM 전용 예외 처리 시스템 ===")

# 사용자 정의 예외 클래스 2개 정의
class AccountLockedError(Exception):
    # 비밀번호 오류 횟수 초과 등으로 계좌가 잠겼을 때 발생
    def __init__(self, owner):
        super().__init__(f"[{owner}] 님의 계좌는 잠긴 상태입니다. 영업점을 방문해 주세요.")

class InsufficientBalanceError(Exception):
    # 출금 요청 금액이 현재 잔액보다 많을 때 발생
    def __init__(self, balance, amount):
        self.shortage = amount - balance
        super().__init__(f"잔액이 {self.shortage:,}원 부족합니다. (현재 잔액: {balance:,}원 / 요청: {amount:,}원)")

# 은행 계좌 클래스
class BankAccount:
    def __init__(self, owner, balance=0, is_locked=False):
        self.owner = owner
        self.balance = balance
        self.is_locked = is_locked            

    def withdraw(self, amount):
        # 계좌 잠김 검사
        if self.is_locked:
            raise AccountLockedError(self.owner)

        # 잔액 부족 검사
        if amount > self.balance:
            raise InsufficientBalanceError(self.balance, amount)

        self.balance -= amount
        print(f"[{self.owner}] {amount:,}원 출금 완료! (잔액 : {self.balance:,}원)")


account1 = BankAccount("김철수", is_locked=False, balance=30000)
account2 = BankAccount("이영희")

try:
    print("\n[시나리오 1 : 정상 출금 시도]")
    account1.withdraw(10000)
except (AccountLockedError, InsufficientBalanceError) as e:
    print(e)    

try:
    print("\n[시나리오 2 : 잔액 부족]")
    account1.withdraw(50000)
except  InsufficientBalanceError as e:
    print(f"[잔액 부족 에러 감지] {e}")
    print(f"부족한 금액 : {e.shortage:,}원")    

try:
    print("\n[시나리오 3 : 잠김 계좌에서 출금 시도]")
    account2.withdraw(20000)
except  AccountLockedError as e:
    print(f"[보안 에러 감지] {e}")
except  InsufficientBalanceError as e:
    print(f"[잔액 부족 에러 감지] {e}")
    print(f"부족한 금액 : {e.shortage:,}원")    
        


