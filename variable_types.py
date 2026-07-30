print("=== 사원 정보 관리 시스템 ===")

class Employee:
    # 클래스 변수 (모든 사원이 공유하는 데이터)
    company_name = "테크코퍼레이션"
    total_employees = 0 

    def __init__(self, name, department, salary):
        # 인스턴스 변수 (각 사원 고유 데이터)
        self.name = name
        self.department = department
        self.salary = salary

        Employee.total_employees += 1
        self.emp_id = Employee.total_employees # 사원번호 부여

    def display_info(self):
        print(f"[{Employee.company_name}] 사번: {self.emp_id} | 이름: {self.name} | 부서명: {self.department} | 연봉: {self.salary:,}만 원")

    def raise_salary(self, amount):
        self.salary += amount
        print(f" {self.name} 사원의 연봉이 {amount:,}만 원 인상되었습니다. (현재: {self.salary:,}만 원)")

# 초기 입사자수 확인
print(f"현재 총 사원 수 : {Employee.total_employees}명\n")

# 사원 객체 생성
emp1 = Employee("김철수", "개발팀", 5500)
emp2 = Employee("이영희", "디자인팀", 4800)
emp3 = Employee("박민수", "마케팅팀", 5000)

print("사원 목록 출력")
emp1.display_info()
emp2.display_info()
emp3.display_info()

print(f"\n현재 총 사원 수 : {Employee.total_employees}명\n")

# 연봉 인상 (특정 인스턴스 변수만 변경)
print("\n [연봉 조정] ")
emp1.raise_salary(500)

# 회사명 변경 (클래스 변수 변경시 모든 객체에 일괄 반영)
print("\n [회사명 변경 진행]")
Employee.company_name = "(주)왕초보Making"

emp1.display_info()
emp2.display_info()
