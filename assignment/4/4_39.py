import turtle
import math

x1, y1, r1 = eval(input("중점의 x, y좌표와 반지름을 입력해주세요 : "))
x2, y2, r2 = eval(input("중점의 x, y좌표와 반지름을 입력해주세요 : "))
distance = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
# 두 원의 중심 사이의 거리를 계산하여 저장

sum_r = r1 + r2
# 두 원의 반지름을 더한값을 저장

if r1 > r2:
    large_r = r1
    small_r = r2
    center_x = x1
    center_y = y1
else:
    large_r = r2
    small_r = r1
    center_x = x2
    center_y = y2
# 반지름이 더 큰 원의 좌표와 큰 반지름, 작은 반지름을 저장한다

turtle.penup()
turtle.goto(x1, y1 - r1)
turtle.pendown()
turtle.circle(r1)
# 원을 그린다

turtle.penup()
turtle.goto(x2, y2 - r2)
turtle.pendown()
turtle.circle(r2)
# 원을 그린다

turtle.penup()
turtle.goto(center_x - large_r, center_y - large_r - 20)
# 안내 메세지를 출력하기 좋은 곳으로 turtle을 이동시킨다
# 큰 원의 왼쪽 아래 부분

if distance + small_r < large_r :
    turtle.write("원2는 원1의 내부에 있습니다.")
elif distance + small_r == large_r :
    turtle.write("원2는 원1과 한 점에서 겹칩니다.(내부)")
elif distance < sum_r:
    turtle.write("원2는 원1과 겹칩니다.")
elif distance == sum_r:
    turtle.write("원2는 원1과 한 점에서 겹칩니다.(외부)")
else:
    turtle.write("원2는 원1과 겹치지 않습니다.")
# 조건문을 이용하여 두 원의 겹침 상태를 상황에 맞게 출력한다.
turtle.hideturtle()
