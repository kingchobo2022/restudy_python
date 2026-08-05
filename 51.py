print("=== 예외 처리 기초 실습 : 안전한 나눗셈 프로그램 ===")

def safe_divide():
    try:
        num1 = int(input("첫 번째 정수를 입력하세요:"))
        num2 = int(input("두 번째 정수를 입력하세요:"))

        result = num1 / num2
        print(f"연산 결과 : {num1} / {num2} = {result:.2f}")
        
    except ValueError:
        print(" 오류 : 정수만 입력할 수 있습니다. 숫자로 다시 시도해 주세요.")

    except ZeroDivisionError:
        print(" 오류 : 0으로 나눌 수 없습니다.")

    except Exception as e:
        print(f" 알 수 없는 예외가 발생했습니다: {e}")        


safe_divide()

