import time

gap = eval(input("GMT와 시간대 차이를 입력하세요 : "))

totalSeconds = int(time.time())
# 현재까지 누적된 초 저장

second = totalSeconds % 60
# totalSeconds % 60 == curSecond

minute = int(totalSeconds / 60) % 60
# totalSeconds / 60 == totalMinute
# totalMinute % 60 == curMinute

hour = int(totalSeconds / 3600 + gap) % 24
# totalSeconds / 3600 == totalHour
# totalHour + gap == GMT와 시간대 차이를 맞춰줌
# (totalHour + gap) % 24 == curHour

print("현재 시간은", hour, ":", minute, ":", second, "입니다.")
