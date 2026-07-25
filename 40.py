# (제목, 저자, 대여여부, 대여자ID)
books = {
    "978-1": ("파이썬 기초", "김철수", False, None),
    "978-2": ("데이터 분석", "이영희", True, "user01")
}

active_borrowers = {"user01"}

while True:
    print("\n" + "=" * 45)
    print(" 📚 스마트 도서관리 시스템(v1.0)")
    print("=" * 45)
    print("1. 도서 등록")
    print("2. 도서 전체 목록 조회")
    print("3. 도서 대여")
    print("4. 도서 반납")
    print("5. 대여 중인 회원 현황(세트 분석)")
    print("0. 프로그램 종료")
    print("-" * 45)

    choice = input("➡️ 원하시는 작업 번호를 입력하세요. ").strip()

    # 1. 도서 등록
    if choice == "1":
        isbn = input("ISBN(고유번호) 입력: ").strip()
        if isbn in books:
            print("⚠️ 이미 등록된 ISBN입니다.")
            continue
        title = input("도서 제목: ").strip()
        author = input("저자 이름: ").strip()    

        books[isbn] = (title, author, False, None)
        print(f"✅ '{title}' 도서가 성공적으로 등록되었습니다. ")
    # 2. 도서 전체 목록 조회
    elif choice == "2":
        print("\n[ 📖 전체 도서 목록 ]")
        if not books:   
            print("등록된 도서가 없습니다.")
        else:
            for isbn, (title, author, is_borrowed, borrower) in books.items():
                status = f"🔴 대여 중 ({borrower})" if is_borrowed else "🟢 대여 가능"
                print(f"- [{isbn}] {title} ({author}) 상태: {status}")
    # 3. 도서 대여
    elif choice == "3":
        isbn = input("대여할 도서의 ISBN을 입력하세요: ").strip()

        if isbn not in books:
            print("❌ 존재하지 않는 ISBN입니다.")                                                    
            continue

        title, author, is_borrowed, _ = books[isbn]

        if is_borrowed:
            print(f"⚠️ '{title}' 책은 이미 대여 중입니다. ")    
        else:
            user_id = input("대여하는 회원 ID를 입력하세요: ").strip()
            books[isbn] = (title, author, True, user_id)
            active_borrowers.add(user_id) 
            print(f"'{title}' 도서가 [{user_id}] 님에게 대여되었습니다.")

    # 4. 도서 반납
    elif choice == "4":
        isbn = input("반납할 도서의 ISBN을 입력하세요: ").strip()

        if isbn not in books:
            print("❌ 존재하지 않는 ISBN입니다.")                                                    
            continue

        title, author, is_borrowed, borrower = books[isbn]

        if not is_borrowed:
            print(f"⚠️ '{title}' 책은 대여 상태가 아닙니다.(이미 반납됨). ")                
        else:
            books[isbn] = (title, author, False, None)

            still_borrowing = any(
                info[3] == borrower for info in books.values()
            )

            if not still_borrowing:
                active_borrowers.discard(borrower)

            print(f"✅ '{title}' 도서가 정상적으로 반납되었습니다. ")    

    # 5. 대여 중인 회원 현황
    elif choice == "5":
        print("\n [  현재 대여중인 회원 목록 (중복 제거됨 )]")                            

        if not active_borrowers:
            print("현재 도서를 대여 중인 회원이 없습니다.")
        else:
            print(f"총 대여 회원수: {len(active_borrowers)}명")            
            print("회원 ID 목록:", ",".join(active_borrowers))

    # 0. 프로그램 종료
    elif choice == "0":
        print("\n도서 관리 프로그램을 종료합니다. 수고하셨습니다!")
        break
    else:
        print("❌ 잘못된 번호 입니다. 0~5 사이의 숫자를 입력하세요.")    



