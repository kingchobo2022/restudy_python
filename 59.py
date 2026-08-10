import datetime

now = datetime.datetime.now()

print("현재 시각:", now.strftime("%Y년 %m월 %d일 %H시 %M분"))

future = now + datetime.timedelta(days=7)
print("7일 뒤:", future.strftime("%Y년 %m월 %d일 %H시 %M분"))