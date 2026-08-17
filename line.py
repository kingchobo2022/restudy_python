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
    "평균기온": [-7.5, -10.2, -4.3, 2.1, 8.5]
}
df = pd.DataFrame(data)

plt.plot(df["월"], 
         df["평균기온"], 
         marker="o", 
         color="royalblue", 
         linestyle="-", 
         linewidth=2
         )

plt.title("겨울철 월별 평균 기온 추이")
plt.xlabel("월")
plt.ylabel("기온(C)")
plt.axhline(0, color="gray", linestyle="--", linewidth=0.8)
plt.grid(True, linestyle=":", alpha=0.6)

plt.show()
