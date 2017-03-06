import turtle

px, py = eval(input("점 p의 좌표를 입력하세요 : "))
qx, qy = eval(input("점 q의 좌표를 입력하세요 : "))
rx, ry = eval(input("점 r의 좌표를 입력하세요 : "))

pos = (qx - px) * (ry - py) - (rx - px) * (qy - py)
# 점의 위치 상태를 저장한다

turtle.penup()
turtle.goto(px, py)
turtle.pendown()
turtle.write("p(" + str(px) + "," + str(py) + ")")
# 점의 좌표를 출력
turtle.goto(qx, qy)
# 두 점 사이를 잇는 직선을 그린다
turtle.write("q(" + str(qx) + "," + str(qy) + ")")
# 점의 좌표를 출력

turtle.penup()
turtle.goto(rx, ry)
turtle.hideturtle()
turtle.dot(5, "green")
# 점을 찍는다

if pos > 0:
    turtle.write("점r 은 직선의 왼쪽에 있습니다.")
elif pos == 0:
    turtle.write("점r 은 직선위에 있습니다.")
else:
    turtle.write("점r 은 직선의 오른쪽에 있습니다.")
# 점의 위치 상태에 따른 메세지 출력
