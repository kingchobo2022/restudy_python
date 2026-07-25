birth_year_str = input("태어난 연도를 입력하세요 (예: 1990): ")
birth_year = int(birth_year_str)

current_year = int(input("올해는 몇 년도인가요? "))

age = current_year - birth_year

print("당신의 한국 나이는 ", age + 1, "세입니다.")