# a, b, c, d, e, f를 입력하세요 : 9.0, 4.0, 3.0, -5.0, -6.0, -21.0
# x는 2이고, y는 3입니다.

# a, b, c, d, e, f를 입력하세요 : 1.0, 2.0, 2.0, 4.0, 4.0, 5.0
# 이 방정식은 해가 없습니다.

# 4.3 실행 예

from LinearEquation import LinearEquation
# LinearEquation 파일에서 LinearEquation 클래스 import

a, b, c, d, e, f = eval(input("a, b, c, d, e, f를 입력하세요 : "))
# 입력값을 받음

linear = LinearEquation(a, b, c, d, e, f)
# 입력값으로 linear 객체 생성

linear.print()
# linear 객체의 해 출력
# 해가 없다면 안내 메세지 출력
