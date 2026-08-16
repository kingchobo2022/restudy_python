import numpy as np
import pandas as pd

print("=== 사원 데이터 결측치 정제 및 그룹화 집계 실습 ===")

#1. 결측치가 포함된 원본 데이터프레임 생성
raw_data = {
    "사원명": ["김철수", "이영희", "박민수", "최수진", "정지원", "강동원"],
    "부서": ["개발팀", "마케팅팀", "개발팀", "디자인팀", np.nan, "개발팀"],
    "근속연수": [3, 5, np.nan, 2, 4, 7],
    "급여": [5200, 4800, 5800, np.nan, 4500, 7200],
    "성과점수": [88, 92, 75, 85, 90, 95]
}

df = pd.DataFrame(raw_data)

print("\n[ 1. 원본 데이터 및 결측치 현황 ]")
print(df)
print("\n컬럼별 결측치 개수:")
print(df.isna().sum())

# 2. 결측치 정제 (전처리 파이프라인)
# (1) '부서'가 누락된 직원은 데이터 신뢰도가 떨어지므로 해당 행 삭제
df_clean = df.dropna(subset=["부서"]).copy()

# (2) '근속연수' 결측치는 전체 사원 근속연수의 중앙값(median)으로 대체
median_years = df_clean["근속연수"].median()
df_clean["근속연수"] = df_clean["근속연수"].fillna(median_years)

mean_salary = round(df_clean["급여"].mean(), 0)
df_clean["급여"] = df_clean["급여"].fillna(mean_salary)

print("\n[ 2. 전처리 완료된 데이터 프레임 ]")
print(df_clean)

# 3. groupby()를 활용한 부서별 통계 집계
dept_summary = df_clean.groupby("부서").agg(
    사원수=("사원명", "count"),
    평균급여=("급여", "mean"),
    최고성과=("성과점수", "max")
).round(1)

print("\n[ 3. 부서별 요약 통계 보고서 ]")
print(dept_summary)