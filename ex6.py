# 1. 데이터 입력 및 연산 (변수 정의)
name = "홍길동"
current_year = 2026
birth_year = 1910

# 올해 연도에서 출생 연도를 빼서 나이를 계산
age = current_year - birth_year

height = 170.1
is_learning_python = True

# 2. 정보 출력하기
print("======== 프로필 카드 =======")
print("1. 이름:", name)

# 숫자인 age를 str()를 형 변환하여 문장과 연결
print("2. 나이: " + str(age) + "세 (출생년도: " + str(birth_year) + "년)")

# 실수형 데이터 출력
print("3. 신장 ", height, "cm")

# 불리언 데이터를 이용한 상태 출력
print("4. 파이썬을 공부 중인가요? : ", is_learning_python)
print("=====================================")

# 3. sep 옵션을 활용한 한 줄 요약 출력
print("요약", name, str(age) + "세", "키_" + str(height) + "cm", sep=" | ")
