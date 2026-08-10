from my_shop.payment.card import pay_by_card
from my_shop.inventory.stock import check_stock

print("=== 🛒 온라인 쇼핑몰 주문 처리 프로세스 ===")

item = "파이썬 전용 키보드"
price = 89000

# 재고 확인 및 결제 진행
if check_stock(item):
    pay_by_card(price)
    
