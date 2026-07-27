print("=== 쇼핑몰 상품 데이터 가공 실습 ===")

products = [
    {"name":"키보드", "price": 45000},
    {"name":"마우스", "price": 25000},
    {"name":"모니터", "price": 280000},
    {"name":"USB 허브", "price": 15000},
    {"name":"헤드셋", "price": 89000}
]

# filter() + lambda : 50,000원 이상 고가 상품만 추려내기
expensive_products = list(
    filter(lambda p: p["price"] >= 50000, products)    
)

print("\n [5만원 이상 고급 상품 목록]")
for p in expensive_products:
    print(f"{p['name']} : {p['price']:,}원")

# map() + lambda: 모든 상품 가격에 10% 할인가 적용하기
discounted_products = list(
    map(lambda p: {
        "name" : p["name"],
        "discounted_price": int(p["price"] * 0.9)
    }, products)
)

print("\n[ 10% 할인율 적용된 가격 표 ]")
for p in discounted_products:
    print(f" - {p['name']}: {p['discounted_price']:,}원")


# sorted() + lambda: 가격이 비싼 순(내림차순)으로 정렬하기
sorted_by_price = sorted(products, key=lambda p: p['price'], reverse=True)

for i, p in enumerate(sorted_by_price, 1):
    print(f"{i}위, {p['name']} {p['price']:,}원)")
