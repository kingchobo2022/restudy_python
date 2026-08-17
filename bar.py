import matplotlib.pyplot as plt
import pandas as pd

# Windows: Malgun Gothic
# Mac : AppleGothic
plt.rc("font", family="Malgun Gothic")

# 마이너스 깨짐 방지
plt.rc("axes", unicode_minus=False)

# 1. 데이터 프레임 생성 (음수 데이터 포함)
data = {
    "월": ["12월", "1월", "2월", "3월", "4월"],
    "최저기온": [-7.5, -10.2, -4.3, 2.1, 8.5]
}
df = pd.DataFrame(data)

# 2. 막대그래프 그리기
plt.bar(df["월"], df["최저기온"], color="cornflowerblue")

# 3. 차트 설정
plt.title("월별 최저 기온 변화")
plt.xlabel("월")
plt.ylabel("기온 (섭씨)")
plt.axhline(0, color="gray", linestyle="--", linewidth=0.8)
# 4. 그래프 출력
plt.show()
