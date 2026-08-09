import unit_converter as uc
from unit_converter import kg_to_lbs

print("=== 단위 변환 서비스 실행 ===")
temp_c = 25
temp_f = uc.celsius_to_fahrenheit(temp_c)
print(f"- 섭씨 {temp_c}C -> 화씨 {temp_f:.1f}F")

weight_kg = 70
weight_lbs = kg_to_lbs(weight_kg)
print(f"- 체중 {weight_kg}kg -> {weight_lbs:.1f} lbs")
