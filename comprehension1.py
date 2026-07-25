print("--- 1. 문자열 길이 구하기 ---")
words = ["python", "java", "c", "php", "javascript"]

# 단어 길이가 4글자 이상인 단어만 대문자로 변환
long_words = [word.upper() for word in words if len(word) >= 4]
print("원본:", words)
print("4글자 이상 대문자 변화:", long_words)

print("\n--- 2. 조건부 가공 (if-else 문) ---")
# 60점 이상은 'PASS', 미만은 'FAIL'로 바꾼 리스트 생성
scores = [85, 42, 90, 55, 78]

# [참일때값 if 조건식 else 거짓일때값 for 변수 in 객체]
results = ["PASS" if s >= 60 else "FAIL" for s in scores ]
print("점수:", scores)
print("결과:", results)