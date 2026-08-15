import csv
from datetime import datetime
import json
from pathlib import Path
import requests
from bs4 import BeautifulSoup

#==============================================
# 1. 설정 및 경로 초기화 (pathlib 사용)
#==============================================
DATA_DIR = Path("data")
DATA_DIR.mkdir(parents=True, exist_ok=True) # data폴더 자동 생성
TARGET_URL = "https://news.ycombinator.com/"
HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
}

#==============================================
# 2. 웹 데이터 수집 및 정제 함수
#==============================================
def fetch_tech_news(limit=15):
    """웹 서버에서 HTML을 받아와 뉴스 항목 추출"""    
    print(f"🌐 [{TARGET_URL}]에서 실시간 IT뉴스를 수집합니다...")

    try:
        response = requests.get(TARGET_URL, headers=HEADERS, timeout=10)
        response.raise_for_status()        
    except requests.exceptions.RequestException as e:
        print(f"❌ 웹 페이지 요청 중 오류 발생: {e}")        
        return []

    soup = BeautifulSoup(response.text, "html.parser")   
    title_elements = soup.select("span.titleline > a") 

    news_list = []

    for idx, item in enumerate(title_elements[:limit], 1):
        title = item.text.strip()
        link = item.get("href", "#")

        # 상대 경로 링크일 경우 절대 경로로 정제
        if link.startswith("item?id="):
            link = f"https://news.ycombinator.com/{link}"

        # 도메인 정보 추출
        site_domain = link.split("/")[2] if link.startswith("http") else "ycombinator.com"      

        news_list.append({
            "rank": idx,
            "title": title,
            "link": link,
            "domain": site_domain
        })

    print(f"✅ 총 {len(news_list)}개의 헤드라인 수집 완료!")
    return news_list

#==============================================
# 3. JSON 및 CSV 보고서 저장 함수
#==============================================
def save_reports(news_data):
    """수집된 데이터를 JSON과 CSV 파일로 영구 저장"""
    if not news_data:
        print("⚠️ 저장할 뉴스 데이터가 없습니다.")        
        return

    today_str = datetime.now().strftime("%Y%m%d") # 20260815
    timestamp_str = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    # 파일 경로 정의 (pathlib 사용)
    json_path = DATA_DIR / f"news_{today_str}.json"
    csv_path = DATA_DIR / f"news_{today_str}.csv"

    #1. JSON 파일 저장
    json_payload = {
        "collected_at": timestamp_str,
        "total_count": len(news_data),
        "articles" : news_data
    }

    with open(json_path, "w", encoding="utf-8") as f:
        json.dump(json_payload, f, ensure_ascii=False, indent=4)
    print(f"📄JSON 파일 저장 완료 : [{json_path}]")        

    #2. CSV 파일 저장 (utf-8-sig: 엑셀에서 한글 깨짐 방지)
    fieldnames = ["rank", "title", "domain", "link"]
    with open(csv_path, "w", newline="", encoding="utf-8-sig") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(news_data)
    print(f"📊CSV 파일 저장 완료: [{csv_path}]")        

#==============================================
# 4. 메인 실행 프로세스
#==============================================
def main():
    print("=== 🚀 IT 기술 뉴스 자동 수집 및 보고서 생성기 ===")

    # 1. 뉴스 데이터 수집
    news = fetch_tech_news(limit=10)

    # 2. 수집 결과 콘솔 출력
    if news:
        print("\n" + "=" * 65)
        print(f"{'순위':<4} | {'제목':<35} | {'출처':<15}")
        print("=" * 65)
        for item in news:
            short_title = item['title'][:32] + "..." if len(item['title']) > 32 else item['title']
            print(f"{item['rank']:<4} | {short_title:<35} | {item['domain']:<15}")
        print("=" * 60 + "\n")

    # 3. 파일 저장 진행
    save_reports(news)
    print("\n🎉 모든 수집 및 파일 저장 작업이 성공적으로 완료되었습니다!")

if __name__ == "__main__":
    main()