print("===== 신나는 구구단 출력하기 =====")

for dan in range(2, 10):
    print(f"\n---{dan}단 시작---")

    for num in range(1, 10):
        print(dan, "x", num, "=", dan * num)

    print("\n-----------------")