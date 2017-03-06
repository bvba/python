# class RegularPolygon
#
# - n : int
# - side : float
# - x : float
# - y : float
#
# RegularPolygon(n : int, side : float, x : float, y : float)
# getPerimeter()    : float
# getArea()         : float
# getN()    : int
# getSide() : float
# getX()    : float
# getY()    : float
# setN(n : int)         : None
# setSide(side : float) : None
# setX(x : float)       : None
# setY(y : float)       : None

import math
PI = math.pi

class RegularPolygon :
    def __init__(self, n = 3, side = 1, x = 0.0, y = 0.0) :
        self.__n = n
        self.__side = side
        self.__x = x
        self.__y = y
    # 생성자
    
    def print(self) : 
        print("Number :", self.__n)
        print("Side :", self.__side)
        print("Perimeter :", self.Perimeter())
        print("Area :", format(self.Area(), ".3f"), '\n')
    # 변의 개수, 변의 길이, 둘레, 넓이 출력

    # 모든 필드 값에 대한 getter, setter
    def Perimeter(self) :   return self.__n * self.__side
    def Area(self)      :   return self.__n * (self.__side ** 2) / (4 * math.tan(PI / self.__n))
    def getN(self)      :   return self.__n
    def getSide(self)   :   return self.__side
    def getX(self)      :   return self.__x
    def getY(self)      :   return self.__y
    def setN(self, n)   :   self.__n = n
    def setSide(self, side) :   self.__side = side
    def setX(self, x)   :   self.__x = x
    def setY(self, y)   :   self.__y = y
