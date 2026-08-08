# print("=== 파이썬 텍스트 파일 입출력 실습 ===")

file_path = "my_diary.txt"

print("\n1. 일기장 파일 생성 및 초기 내용 쓰기...")
with open(file_path, "w", encoding="utf-8") as f:
    f.write("=== 2026년 파이썬 개발 일지 ===\n")
    f.write("01월 10일: 파이썬 기초 문법 정복 시작\n")

print("\n2. 일기장에 새로운 기록 추가하기...")
with open(file_path, "a", encoding="utf-8") as f:
    f.write("02월 15일: 객체지향 및 예외 처리 완료\n")
    f.write("08월 8일: 파일 입출력(File I/O) 마스터!\n")

print("\n3. 저장된 일기장 파일 전체 읽기:")
print("-" * 40)
try:
    with open(file_path, "r", encoding="utf-8") as f:
        content = f.read()
        print(content)

except FileNotFoundError:        
    print("읽어올 파일이 존재하지 않습니다.")

print("-" * 40)

print("\n4. readlines()를 사용해 한 줄씩 처리하기:")
with open(file_path, "r", encoding="utf-8") as f:
    lines = f.readlines()

    for idx, line in enumerate(lines, 1):
        print(f"line {idx}: {line.strip()}")


