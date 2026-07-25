print("=== 편의점 재고 현황 관리 ===")

inventory = {
    "삼각김밥" : 12,
    "바나나우유" : 5,
    "컵라면" : 0,
    "샌드위치" : 8,
    "도시락" : 2
}

print("\n1. 전체 재고 목록 출력")
print("-" * 30)
for item, count in inventory.items():
    print(f"* {item}: {count}개")

print("\n2. 품절 상품 확인")
print("-" * 30)

for item, count in inventory.items():
    if count == 0:
        print(f" 경고: '{item}' 상품이 품절되었습니다!")

print("\n3. 총 재고 수량 계산")
print("-" * 30)
total_count = sum(inventory.values())
print(f"현재 매장의 총 상품 수량: {total_count}개")
