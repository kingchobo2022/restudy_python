from pathlib import Path
import matplotlib.pyplot as plt
import pandas as pd

print("=== 📈 matplotlib 기초: 매출 및 카테고리 실적 시각화 ===")

# 1. 한글 폰트 및 마이너스 부호 설정 (Windows: Malgun Gothic, Mac: AppleGothic)
plt.rc("font", family="Malgun Gothic")
plt.rc("axes", unicode_minus=False)

# 2. 샘플 데이터프레임 생성
monthly_data = {
    "월": ["1월", "2월", "3월", "4월", "5월", "6월"],
    "매출액": [3200, 3800, 3500, 4200, 4900, 5600],
    "마케팅비": [400, 450, 420, 520, 600, 750]
}
category_data = {
    "카테고리": ["전자기기", "패션", "식품", "도서", "생활용품"],
    "판매량": [140, 220, 310, 95, 180]
}

df_month = pd.DataFrame(monthly_data)
df_cat = pd.DataFrame(category_data)

# 3. 1행 2열(가로로 2개) 구조의 차트 캔버스 생성
fig, (ax1, ax2) = plt.subplots(nrows=1, ncols=2, figsize=(14, 5))
fig.suptitle("2026년 상반기 비즈니스 성과 분석 대시보드", fontsize=16, fontweight="bold")

# [좌측 차트] 선 그래프 (월별 매출 및 마케팅비 추이)
ax1.plot(df_month["월"], df_month["매출액"], marker="o", color="#1f77b4", linewidth=2, label="매출액(만원)")
ax1.plot(df_month["월"], df_month["마케팅비"], marker="s", color="#ff7f0e", linestyle="--", label="마케팅비(만원)")
ax1.set_title("월별 매출 및 마케팅비 추이")
ax1.set_xlabel("월")
ax1.set_ylabel("금액 (만원)")
ax1.grid(True, linestyle=":", alpha=0.6)
ax1.legend()

# [우측 차트] 막대 그래프 (카테고리별 판매량 비교)
colors = ["#2ca02c", "#d62728", "#9467bd", "#8c564b", "#e377c2"]
bars = ax2.bar(df_cat["카테고리"], df_cat["판매량"], color=colors, width=0.6)
ax2.set_title("상품 카테고리별 상반기 누적 판매량")
ax2.set_xlabel("카테고리")
ax2.set_ylabel("판매량 (건)")

# 막대 상단에 수치 라벨 표기
for bar in bars:
    height = bar.get_height()
    ax2.text(bar.get_x() + bar.get_width()/2.0, height + 5, f"{int(height)}건", ha="center", va="bottom", fontsize=9)

# 여백 자동 조정
plt.tight_layout()

# 4. 차트 결과물을 고화질 PNG 이미지 파일로 저장 (pathlib 활용)
output_dir = Path("charts")
output_dir.mkdir(parents=True, exist_ok=True)
output_file = output_dir / "business_dashboard.png"

plt.savefig(output_file, dpi=300)
print(f"✅ 대시보드 차트 이미지가 성공적으로 저장되었습니다: [{output_file}]")

# 화면에 팝업 창으로 표시 (VS Code 또는 로컬 GUI 환경)
plt.show()