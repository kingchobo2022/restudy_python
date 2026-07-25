age = int(input("나이를 입력하세요: "))
height = float(input("키(cm)를 입력하세요: "))

if age >= 10:
    print("[시스템] 나이 기준 (10세 이상)을 통과하셨습니다.")

    if height >= 130:
        print("축하합니다. 롤러코스터 탑승이 가능합니다")
    else:
        print("키가 130cm 미만이므로 탑승이 어렵습니다")    
else:
    print("나이가 10세 미만이므로 안전을 위해 탑승이 불가합니다")        

