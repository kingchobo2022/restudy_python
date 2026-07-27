print("=== 학생 성적 계산기 ===")

def calculate_score(kor, eng, math):
    total = kor + eng + math
    avg = total / 3
    return total, avg

def check_pass(avg):
    if avg >= 60:
        return "합격"
    else:
        return "불합격"    

# 학생 A
student_a_total, student_a_avg = calculate_score(85, 90, 80)    
result_a = check_pass(student_a_avg)
print(f"학생 A -> 총점: {student_a_total}점, 평균: {student_a_avg:.1f} | 결과: {result_a} ")

# 학생 B
student_b_total, student_b_avg = calculate_score(50, 60, 40)    
result_b = check_pass(student_b_avg)
print(f"학생 B -> 총점: {student_b_total}점, 평균: {student_b_avg:.1f} | 결과: {result_b} ")

