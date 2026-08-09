import csv
from datetime import datetime
from pathlib import Path

#========================================================================
# 1. 경로 설정 (pathlib 사용) 및 사용자 정의 예외
#========================================================================
DATA_DIR = Path("data")
FILE_PATH = DATA_DIR / "leger.csv" # / 연산자로 경로 직관적 결합
FILENAMES = ["date", "type", "category", "amount"]

class InvalidAmountError(Exception):
    """ 금액이 0이하이거나 정수가 아닐 때 발생하는 예외 """
    def __init__(self, amount):
        super().__init__(f"유효하지 않은 금액입니다: '{amount}' (0보다 큰 양의 정수를 입력해 주세요.)")

#========================================================================
# 2. pathlib 기반 파일 및 디렉토리 초기화
#========================================================================
def init_storage():
    """ pathlib을 활용한 데이터 디렉토리 및 CSV 파일 초기화 """
    # parents=True: 상위 디렉토리까지 필요시 자동 생성
    # exist_ok=True: 이미 폴더가 존재해도 FileExistsError 발생 안 함
    DATA_DIR.mkdir(parents=True, exist_ok=True)

    # FILE_PATH.exists() 메서드를 파일 존재 여부 확인
    if not FILE_PATH.exists():
        with open(FILE_PATH, "w", newline="", encoding="utf-8") as f:
            writer = csv.DictWriter(f, fieldnames=FILENAMES)
            writer.writeheader()

#========================================================================
# 3. 핵심 비즈니스 로직 함수
#========================================================================
def add_entry():
    """ 수입/지출 내역 추가 """
    print("\n[ 📝 신규 내역 등록 ]")

    kind = input("구분을 선택하세요. (1:지출, 2:수입:)").strip()
    if kind == "1":
        entry_type = "지출"
    elif kind == "2":
        entry_type = "수입"
    else:
        print("❌ 잘못된 구분입니다. 등록을 취소합니다.")  
        return

    category = input("카테고리 (예: 식비, 교통, 급여, 여가): ").strip()

    # 금액 입력 및 사용자 정의 예외 검사
    try:
        raw_amount = input("금액(원):").strip()
        amount = int(raw_amount)
        if amount <= 0:
            raise InvalidAmountError(amount)
    except ValueError:
        print("❌ 오류: 금액은 숫자(정수)만 입력할 수 있습니다.")   
        return
    except InvalidAmountError as e:
        print(f"❌ {e}")
        return

    today_str = datetime.now().strftime("%Y-%m-%d")

    try:
        with open(FILE_PATH, "a", newline="", encoding="utf-8") as f:
            writer = csv.DictWriter(f, fieldnames=FILENAMES)
            writer.writerow({
                "date": today_str,
                "type": entry_type,
                "category": category,
                "amount": amount
            })
        print(f"✅ [{entry_type}] {category} - {amount:,}원이 정상적으로 기록되었습니다.")            
    except Exception as e:
        print(f"❌ 파일 저장 중 오류가 발생했습니다.: {e}")

def show_entries():
    """ 전체 내역 조회 """
    print("\n[ 📝 전체 수입/지출 내역 ]")
    print("-" * 55)
    print(f"{'날짜':<12} | {'구분':<6} | {'카테고리':<10} | {'금액':>12}")
    print("-" * 55)

    if not FILE_PATH.exists():
        print("기록된 내역이 없습니다.")
        return

    count = 0
    try:
        with open(FILE_PATH, "r", encoding="utf-8") as f:
            reader = csv.DictReader(f)
            for row in reader:
                amount = int(row["amount"])
                icon = "🔴" if row["type"] == "지출" else "🔵"
                print(f"{row['date']:<12} | {icon} {row['type']} | {row['category']:<10} | {amount:>10,}원")
                count += 1
        if count == 0:
            print("등록된 거래 내역이 존재하지 않습니다.")                
    except Exception as e:
        print(f"❌ 파일 읽기 중 오류 발생 : {e}")            

    print("-" * 55)        

def show_statics():
    """ 월별/전체 요약 통계 """
    print("\n[ 📊 가계부 결산 요약 ]")

    if not FILE_PATH.exists():
        print("데이터 파일이 없습니다. 먼저 내역을 등록해 주세요.")
        return

    total_income = 0
    total_expense = 0

    try:
        with open(FILE_PATH, "r", encoding="utf-8") as f:
            reader = csv.DictReader(f)
            for row in reader:
                amount = int(row["amount"])
                if row["type"] == "수입":
                    total_income += amount
                elif row["type"] == "지출":
                    total_expense += amount

        balance = total_income - total_expense
        print("-" * 40)
        print(f" - 총 수입 : {total_income:>12,}원")
        print(f" - 총 지출 : {total_expense:>12,}원")
        print("-" * 40)
        print(f" - 현재잔액 : {balance:>12,}원")
        print("-" * 40)
                            
    except Exception as e:
        print(f"❌ 통계 계산 중 오류 발생: {e}")    

# =========================================================
# 4. 메인 콘솔 루프
# =========================================================

def main():
    init_storage() # pathlib 을 이용한 저장소 세팅

    while True:
        print("\n" + "=" * 45)
        print(" 💰 스마트 가계부 관리 시스템(v1.0) ")
        print("=" * 45)
        print("1. 수입/지출 내역 등록")
        print("2. 전체/거래 내역 조회")
        print("3. 결산 통계 분석")
        print("0. 프로그램 종료")
        print("-" * 45)

        choice = input("👉 원하시는 작업 번호를 입력하세요.").strip()

        if choice == "1":
            add_entry()
        elif choice == "2":
            show_entries()
        elif choice == "3":
            show_statics()            
        elif choice == "0":
            print("\n👋 가계부 프로그램을 종료합니다. 수고하셨습니다!")
            break
        else:
            print("❌ 잘못된 번호입니다. 0~3 사이의 숫자를 입력해 주세요.")

if __name__ == "__main__":
    main()

