# class QuadraticEquation
#
# - a : float
# - b : float
# - c : float
#
# QuadraticEquation(a : float, b : float, c : float)
# getDiscriminant() : float
# getRoot1()        : float
# getRoot2()        : float
# getA()    : float
# getB()    : float
# getC()    : float

import math

class QuadraticEquation :
    def __init__(self, a = 1, b = -5, c = 6) :
        self.__a = a
        self.__b = b
        self.__c = c
    # 생성자

    def getDiscriminant(self) :
        return (self.__b ** 2) - 4 * self.__a * self.__c
    # 판별식을 반환하는 메소드
    # 해를 구할 때 사용할 수 있다

    def getRoot1(self) :
        return (-self.__b - self.getDiscriminant()) / (2 * self.__a)
    def getRoot2(self) :
        return (-self.__b + self.getDiscriminant()) / (2 * self.__a)
    # 해를 반환하는 메소드

    # 모든 필드 값에 대한 getter
    def getA() : return self.__a
    def getB() : return self.__b
    def getC() : return self.__c
