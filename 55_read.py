import csv

with open("55.csv", "r", encoding="utf-8-sig") as f:
    reader = csv.DictReader(f)
    for row in reader:
        print(f"학생: {row['Name']} | 점수: {row['Score']}점 ({row['Grade']}학점)")

