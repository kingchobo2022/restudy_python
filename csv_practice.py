import csv
import os

print ("=== CSV 기반 회원 데이터 관리 시스템 ===")

data_dir = "members_data"
file_path = os.path.join(data_dir, "member_list.csv")

if not os.path.exists(data_dir):
    os.makedirs(data_dir)
    print(f"📂 [{data_dir}] 디렉토리를 신규 생성했습니다.")

fieldnames = ["id", "name", "point", "role"]

members = [
    {"id": "user101", "name": "김철수", "point": 1500, "role": "VIP"},
    {"id": "user102", "name": "이영희", "point": 800, "role": "Gold"},
    {"id": "user103", "name": "박민수", "point": 2300, "role": "VIP"},
    {"id": "user104", "name": "최수진", "point": 450, "role": "Silver"}
]

print("\n1. 회원 명부 데이터를 CSV 파일로 저장 중...")
with open(file_path, "w", newline="", encoding="utf-8") as f:
    writer = csv.DictWriter(f, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(members)

print(f"✅ [{file_path}] 파일 저장이 완료되었습니다.")

print("\n2. 저장된 CSV 파일 읽기 및 VIP 회원 분석:")
print("-" * 50)

total_points = 0
vip_count = 0

if os.path.exists(file_path):
    with open(file_path, "r", encoding="utf-8") as f:
        reader = csv.DictReader(f)

        for row in reader:
            point = int(row["point"]) # 형변환 int로
            total_points += point

            if row["role"] == "VIP":
                vip_count += 1
                print(f"👑 VIP 회원 발견: [{row['id']}] {row['name']}님 (포인트: {point:,}pt)")                

    print("-" * 50)
    print(f" - 전체 회원 누적 포인트 총합 : {total_points:,}pt")
    print(f" - VIP 회원 수: {vip_count}명")
else:
    print("❌ 지정된 경로에 파일이 존재하지 않습니다.")    


