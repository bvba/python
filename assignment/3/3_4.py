import math
PI = 3.141592653589793

s = eval(input("한 변의 길이를 입력하세요 : "))

area = 5 * s ** 2 / (4 * math.tan(PI/5))
# 오각형의 넓이를 구하는 공식을 이용하여 넓이를 구한 후 저장
# math.tan 함수를 이용한다.

print("오각형의 넓이는", round(area, 3), "입니다.")
