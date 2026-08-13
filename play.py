from playwright.sync_api import sync_playwright

print("=== Playwright를 이용한 동적 웹 데이터 자동 수집 ===")

def main():
    target_url = "https://quotes.toscrape.com/js/";

    with sync_playwright() as p:
        # headless=True: 브라우저 창을 띄우지 않고 백그라운드에서 실행
        # (개발/디버깅 시에는 headless=False로 설정하면 화면 동작을 직접 볼 수 있어요.)
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()

        print(f"[{target_url}] 접속 중...")
        page.goto(target_url)

        # JS 렌더링이 완료되어 특정 요소(.quote)가 화면에 뜰 때까지 자동 대기
        page.wait_for_selector(".quote")

        # page.locator().all() : 조건에 해당하는 모든 요소를 리스트 형태로 반환
        quote_elements = page.locator(".quote").all()

        print(f"총 {len(quote_elements)}개의 동적 명언 데이터를 발견했습니다.\n" + "=" * 65)

        # 수집 데이터 순회 및 추출
        for idx, quote in enumerate(quote_elements, 1):
            # inner_text() : 요소 내부의 텍스트만 깔끔하게 추출
            text = quote.locator(".text").inner_text()
            author = quote.locator(".author").inner_text()

            tags = quote.locator(".tag").all_inner_texts()
            
            tag_str = ", ".join([f"#{t}" for t in tags])

            print(f"{idx:2d}. \"{text}\"")
            print(f"   작성자 : {author}")
            print(f"   태그 : {tag_str}")
            print("-" * 65)

        page.screenshot(path="result_screenshot.png")    
        print(" 현재 화면이 [result_screenshot.png]로 저장되었습니다.")

        browser.close()


if __name__ == "__main__":
    main()



