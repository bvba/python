import math
PI = 3.141592653589793

r = eval(input("오각형의 중심에서 꼭짓점까지의 길이를 입력하세요 : "))
s = 2 * r * math.sin(PI/5)
# 공식을 이용하여 한 변의 길이를 구함

area = 3 * math.sqrt(3) * s ** 2 / 2
# 공식과 한 변의 길이를 이용하여 오각형의 넓이를 구

print("오각형의 넓이는", round(area, 3), "입니다.")
