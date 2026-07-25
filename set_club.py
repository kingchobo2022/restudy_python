print("=== 동아리 중복 가입자 및 공통 인원 분석 ===")

# 농구부 명단
basketball = {"김철수", "이영희", "박민수", "정지원"}

# 축구부 명단
soccer = {"이영희", "최동현", "정지원", "강민석"}

print ("1. 전체 동아리 참여 학생 목록 (합집합)")
all_students = basketball | soccer
print(all_students)

print("\n2. 농구부와 축구부를 모두 하는 학생(교집합)")
both = basketball & soccer
print(both)

print("\n3. 농구부만 하고 축구부는 안 하는 학생 (차집합)")
basketball_only = basketball - soccer
print(basketball_only)

