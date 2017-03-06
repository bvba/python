import math
import turtle
PI = math.pi

def drawPolygon(x, y, radius, numberOfSides) :
    l = 2 * radius * math.sin(PI / numberOfSides)
    # 정다각형의 한 변의 길이를 저장
    x -= l / 2          # 시작점의 x좌표 설정
    y -= math.sqrt(radius ** 2 - (l ** 2 / 4)) # 시작점의 y좌표 설정
    
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()    # 시작점으로 포인터를 옮기고 pendown
    
    for i in range(0, numberOfSides) :
        theta = 2 * PI / numberOfSides * i
        # 정다각형의 외각의 합을 저장
        
        x += (l * math.cos(theta))
        y += (l * math.sin(theta))
        turtle.goto(x, y)
        # 정다각형의 다음 꼭짓점으로 좌표를 옮김
        
    turtle.penup()
    turtle.hideturtle()

        
drawPolygon(0, 0, 250, 15)
# 중심의 좌표가 (0, 0)이고 반지름이 250인 15각형을 그림

turtle.goto(0, 0 - 250)     # 중심의 좌표가(0, 0)이고,
turtle.pendown()
turtle.circle(250)          # 반지름이 250인 원을 그림
