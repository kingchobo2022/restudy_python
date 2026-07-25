fruits = ["사과", "바나나", "딸기", "포도"]

for fruit in fruits:
    print("내가 좋아하는 과일 : ", fruit)

heros = ["아이언맨", "스파이더맨", "토르"]

for index, hero in enumerate(heros):
    print(index + 1 , '위 : ', hero)

scores = [88, 92, 75, 100, 95]    
total = 0

for score in scores:
    total += score

average = total / len(scores) 

print("총점 : ", total, "점")
print("평균 : ", average, "점")