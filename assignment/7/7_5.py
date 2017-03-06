from RegularPolygon import RegularPolygon
# RugularPolygon 파일에서 RegularPolygon 클래스 import

r1 = RegularPolygon()       # r1 객체 생성 by default
r2 = RegularPolygon(6, 4)   # r2 객체 생성 6각형, 한 변의 길이 4
r3 = RegularPolygon(10, 4, 5.6, 7.8)
# r3 객체 생성, 10각형, 한 변의 길이 4, 다각형 중심의  좌표(5.6, 7.8)

r1.print()
r2.print()
r3.print()  # r1, r2, r3 객체의 변의 개수, 변의 길이, 둘레, 넓이 출
