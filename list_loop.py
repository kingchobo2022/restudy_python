print("=== 성적 처리 및 합격자 선별 프로그램 ===")

students = ["김철수", "이영희", "박민수", "정도영"]
scores   = [      75,      95,       60,      88]
pass_students = []

for i, score in enumerate(scores):
    name = students[i]

    if score >= 80:
        print(f"{name}님: {score} 점 (합격)")     
        pass_students.append(name)
    else:
        print(f"{name}님: {score} 점 (불합격)")     

print("\n--- 최종 합격자 명단 ---")
print(pass_students)
