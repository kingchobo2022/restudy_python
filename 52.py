print("=== 회원가입 자격 검증 및 리소스 관리 시스템 ===")

def register_user(username, age):
    print(f"\n---------------------------------------")
    print(f"[{username}] 님의 회원가입 요청 처리 중 ...(나이: {age}세)")

    try:
        if age < 0:
            raise ValueError("나이는 음수가 될 수 없습니다.")
        if age < 14:
            raise PermissionError("만 14세 미만은 보호자 동의 없이 가입할 수 없습니다.")        

    except ValueError as e: 
        print(f"[입력 오류] {e}")
    except PermissionError as e:
        print(f"[권한 오류] {e}")        
    else:
        print(f"환영합니다. [{username}]님의 가입이 정상적으로 완료되었습니다.")
        print("가입 축하 메일을 발송했습니다.")
    finally:
        print("[시스템] 가입 세션을 안전하게 종료하고 데이터베이스 연결을 정돈합니다.")        

register_user("김철수", 25)        
register_user("이영희", -5)
register_user("박민수", 12)