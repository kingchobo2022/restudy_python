import requests
from bs4 import BeautifulSoup

print("===📰 웹 스크래핑 기초: 뉴스 헤드라인 데이터 수집 ===")

url = "https://news.ycombinator.com/"

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
}

try :
    # HTTP GET  요청으로 HTML 문서 가져오기
    response = requests.get(url, headers=headers, timeout=5)
    response.raise_for_status()

    # BeautifulSoup 객체 생성 ( HTML 파싱 )
    soup = BeautifulSoup(response.text, "html.parser")

    articles = soup.select("span.titleline > a")

    print(f"\n 총 {len(articles)}개의 기사 헤드라인을 수집했습니다.\n" + "-" * 60)

    for idx, article in enumerate(articles[:10], 1):
        title = article.text.strip()
        link = article.get("href", "#")
        print(f"{idx:2d}. {title}")
        print(f" 🔗링크: {link}")
        print("-" * 60)

except requests.exceptions.RequestException as e:
    print(f"❌ 웹 페이지 요청 실패: {e}")

