def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

def kg_to_lbs(kg):
    return kg * 2.20462

if __name__ == "__main__":
    print(" [unit_converter.py] 자체 단위 테스트 진행중...")
    print(f"테스트: 섭씨 0도 -> 화씨 {celsius_to_fahrenheit(0)}도")

