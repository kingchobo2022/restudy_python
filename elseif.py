age = int(input("나이를 입력하세요: "))

if age >= 19:
    category = "일반"
    fare = 1500
elif age >= 13:
    category = "청소년"    
    fare = 1000
elif age >= 7:
    category = "어린이"    
    fare = 500
else:
    category = "영유아"    
    fare = 0

print("분류 : ", category)    
print("요금 : " + str(fare) + "원")
