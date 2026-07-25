age = 25
has_license = True

# and 연산
can_drive = (age >= 19) and has_license
print("운전 가능 여부 : ", can_drive)

is_weekend = False
is_holiday = True

# or 연산
can_rest = is_weekend or is_holiday
print("쉴 수 있는 날인가? ", can_rest)

# not 연산
is_raining = False
print("우산을 챙겨야 하나요? ", not is_raining)

# 우선순위 : 1. not,  2. and,  3. or 
print(True or True and False)
print((True or True) and False)