import math
R = 6370.01     # 지구 반지름(km)

x1, y1 = eval(input("첫 번째 점(위도와 경도)을 60분법 각으로 입력하세요 : "))
x2, y2 = eval(input("두 번째 점(위도와 경도)을 60분법 각으로 입력하세요 : "))

rad_x1 = math.radians(x1);
rad_x2 = math.radians(x2);
rad_y1 = math.radians(y1);
rad_y2 = math.radians(y2);
# 각 위도와 경도를 radian으로 바꾸어 저장

distance = R * math.acos(math.sin(rad_x1) * math.sin(rad_x2) + math.cos(rad_x1) * math.cos(rad_x2) * math.cos(rad_y1 - rad_y2))
# 구의 표면에서 두 점 사이의 거리(대권 거리)
# 공식을 이용하여 대권 거리를 구한 후 저장

print("두 점 사이의 거리는", round(distance, 3), "km입니다.")
