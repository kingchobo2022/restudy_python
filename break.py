print("---- 재미있는 더하기 퀴즈 ----")
print("(종료하시려면 정답에 0을 입력하세요)\n")

while True:
    answer = int(input("23 + 45는 무엇일까요? : "))

    if answer == 0:
        print(" 프로그램을 사용자가 종료했습니다.")
        break
    if answer == 68:
        print("정답입니다! 축하합니다.")
        break

    print("틀렸습니다. 다시 한 번 생각해 보세요!\n")

print("--- 퀴즈 프로그램이 완전히 종료되었습니다. ---")
