my_set = {1, 2, 3, 3, 3, 4}
print(my_set)

user_ids = ["userA", "userB", "userA", "userC", "userB", "userD"]

unique_ids = list(set(user_ids))

print("중복 제거 후 : ", unique_ids)

A = {1, 2, 3, 4, 5}
B = {4, 5, 6, 7, 8}
# 1. 차집합 ( A에는 속하고 B에는 속하지 않는 요소 )
print(A - B)
# 2. 교집합 ( 양쪽에 모두 속한 요소 )
print(A & B)
# 3. 합집합 ( 중복을 제거한 전체합 요소 )
print (A | B)

s = {10, 20}
s.add(30)
s.update([40, 50])
s.discard(100) # 요소를 제거하려고 했을 때 값이 없어도 에러가 나지 않음.
s.remove(100) # 요소를 제거하려고 했을 때 값이 없으면 KeyError 를 발생.
