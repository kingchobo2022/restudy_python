import datetime
import json
import math
import random
from pathlib import Path

print("=== 🎁 표준 라이브러리 활용: 자동 이벤트 추첨 시스템 ===")

# 1. random 모듈: 응모자 중 2명 무작위 당첨자 추첨
candidates = ["김철수", "이영희", "박민수", "최수진", "정지원"]
winners = random.sample(candidates, 2)

# 2. math 모듈 : 당첨 확률 계산 (올림 처리)
winning_rate = (len(winners) / len(candidates)) * 100
rounded_rate = math.ceil(winning_rate)

# 3. datetime 모듈 : 쿠폰 발급일 및 만료일(30일 뒤) 계산
now = datetime.datetime.now()
expire_date = now + datetime.timedelta(days=30)

formatted_now = now.strftime("%Y-%m-%d %H:%M:%S")
formated_expire = expire_date.strftime("%Y-%m-%d")

# 4. json 모듈 : 저장할 결과 데이터 구조화
event_result = {
    "event_title": "신규 서비스 오픈 기념 쿠폰 이벤트",
    "issued_at" : formatted_now,
    "expire_at" : formated_expire,
    "winning_rate_percent" : rounded_rate,
    "total_candidates" : len(candidates),
    "winners" : winners
}

# 5. pathlib & json : 결과를 JSON 파일로 영구 보관
output_path = Path("event_result.json")

with open(output_path, "w", encoding="utf-8") as f:
    json.dump(event_result, f, ensure_ascii=False, indent=4)

print("\n[ 추첨 결과 출력 ]")
print(f"- 당첨자 명단: {', '.join(winners)}")
print(f"- 개별 당첨 확률: 약 {rounded_rate}%")
print(f"- 쿠폰 발급 일시: {formatted_now}")
print(f"- 추첨 만료 일자: {formated_expire}")
print(f"✅ 추첨 결과 보고서가 [{output_path}] 파일로 저장되었습니다.")



