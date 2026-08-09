import csv

fieldnames = ["Name", "Score", "Grade"]

data = [
    {"Name": "김철수", "Score": 95, "Grade": "A"},
    {"Name": "이영희", "Score": 88, "Grade": "B"}
]

with open("55.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.DictWriter(f, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(data)

