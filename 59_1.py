import random

cards = ["A", "K", "Q", "J", "10"]
print("카드 1장 뽑기:", random.choice(cards))
print("로또 번호 6개 추첨:", sorted(random.sample(range(1,46), 6)))

