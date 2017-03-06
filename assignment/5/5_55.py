import turtle

SIZE = 20   # 체스판의 사이즈

turtle.penup()
turtle.goto(0, 0)
turtle.pendown()
turtle.goto(0, SIZE * 8)
turtle.goto(SIZE * 8, SIZE * 8)
turtle.goto(SIZE * 8, 0)
turtle.goto(0, 0)
# 체스판의 틀을 그림

for y in range(0, 8) :
    for x in range(0, 8) :
        if (x + y) % 2 :    # x + y == 2 인 경우에만 반복문 수행
            continue
        
        turtle.penup()          # 선 그리기 종료
        turtle.goto(SIZE * x, SIZE * y)         # 사각형의 시작점으로 이동
        turtle.begin_fill()     # 채우기 함수 시작
        turtle.pendown()        # 선 그리기 시작
        turtle.goto(SIZE * x, SIZE * (y + 1))   # 사각형의 왼쪽 위
        turtle.goto(SIZE * (x + 1), SIZE * (y + 1)) # 사각형의 오른쪽 위
        turtle.goto(SIZE * (x + 1), SIZE * y)   # 사각형의 오른쪽 아래
        turtle.goto(SIZE * x, SIZE * y)         # 사각형의 시작점
        turtle.end_fill()       # 채우기 함수 종료
turtle.hideturtle()
