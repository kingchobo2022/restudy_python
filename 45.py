# names = ["김철수", "이영희", "박민수"]
# scores = [85, 92, 78]

# for name, score in zip(names, scores):
#     print(f"{name}: {score}점")

# fruits = ["사과", "바나나", "체리"]
# for idx, fruit in enumerate(fruits, start=1):
#     print(f"{idx}번 과일: {fruit}")

# scores = [80, 95, 70, 85]
# all_pass = all(score >= 60 for score in scores) # True
# has_a_grade = any(score >= 90 for score in scores) # True

nums = [-10, 5, 20, 3]
print(sum(nums))
print(max(nums))
print(min(nums))
print(abs(nums[0]))
print(round(3.14159, 2))

expr = "10 + 20 * 3"
result = eval(expr)
print(result)


