import MyTriangle
# 삼각형인지 판단하는 함수와
# 삼각형의 넓이를 구하는 함수가 있는
# MyTriangle 모듈을 import 한다

side1, side2, side3 = eval(input("세 변의 길이(실수)를 입력하세요 : "))
if MyTriangle.isValid(side1, side2, side3) :    # 삼각형이면
    print("삼각형의 넓이는", format(MyTriangle.area(side1, side2, side3), ".3f"), "입니다.")
    # 넓이를 출력
else :  # 삼각형이 아니면 오류 메시지 출력
    print("잘못된 입력입니다.")
