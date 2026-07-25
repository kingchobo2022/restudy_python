print("--- 1. 튜플 언패킹(Unpacking)")

user_info = ("홍길동", 25, "서울")
name, age, city = user_info

print(f"이름: {name}, 나이: {age}, 지역: {city}")

print("\n--- 2. 두 변수의 값 한 줄로 교환하기 (Swapping) ---")
a = 10
b = 20 

a, b = b, a
print(f"a: {a}, b: {b}")

print("\n---3. 튜플의 인덱싱과 슬라이싱 (조회는 가능!) ---")

numbers = (100, 200, 300, 400, 500)

print("첫 번째 데이터:", numbers[0])
print("뒤에서 첫 번째 데이터:", numbers[-1])
print("슬라이싱 (1~3번):", numbers[1:4])

     