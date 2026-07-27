print("=== 회원 포인트 관리 프로그램 ===")

total_system_points = 1000

def add_points(user_name, current_point, bonus):
    """
    [안전한 방식] 매개변수와 return을 활용한 지역 변수 처리
    """
    new_point = current_point + bonus
    print(f"{user_name} 님에게 {bonus}pt 지급 완료! (현재 : {new_point}pt)")    
    return new_point

def use_system_event():
    """
    [global 활용] 전역 포인트 풀에서 차감
    """
    global total_system_points
    event_cost = 200
    total_system_points -= event_cost
    print(f"이벤트 개최! 시스템 전체 포인트 {event_cost}pt 차감됨.")


# --- 메인 실행부 ---
user_a_point = 100

# 1. 지역 변수 + return 방식 포인트 추가
user_a_point = add_points("김철수", user_a_point, 50)

# 2. global 키워드로 전역 시스템 포인트 수정
print(f"이벤트 전 시스템 총 포인트: {total_system_points}pt")
use_system_event()
print(f"이벤트 후 시스템 총 포인트 : {total_system_points}pt")
