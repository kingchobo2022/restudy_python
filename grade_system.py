# 입력받기
score = int(input("0부터 100 사이의 성적 점수를 입력하세요: "))

# 1차 필터링 : 정상적인 점수 범위 검사
if score < 0 or score > 100:
    print("에러: 올바른 점수 범위가 아닙니다. 0 ~ 100 사이로 입력해 주세요.")
        
else:
    print("[시스템] 정상적인 점수가 확인되었습니다. 학점 판정을 시작합니다.")

    # 2차 필터링: 기본 학점(Grade) 결정
    if score >= 90:
        grade = "A"            
    elif score >= 80:
        grade = "B"        
    elif score >= 70:
        grade = "C"        
    elif score >= 60:
        grade = "D"        
    else:
        grade = "F"

    # 중첩 조건문을 활용한 '+' 보너스 학점 부여
    # 단, F 학점이 아니고 점수의 일의 자리가 5점 이상이어야 합니다.
    if grade != "F":
        if score % 10 >= 5:
            grade = grade + "+"

    # 결과 출력
    print("-----------------------------")
    print("입력 점수:", score, "점")
    print("최종 학점:", grade)
    print("-----------------------------")
