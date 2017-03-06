# class LinearEquation
#
# - a : float
# - b : float
# - c : float
# - d : float
# - e : float
# - f : float
#
# LinearEquation(a : float, b : float, c : float, d : float, e : float, f : float)
# getAD_BC()    : float
# isSolvable()  : bool
# getX()    : float
# getY()    : float
# getA()    : float
# getB()    : float
# getC()    : float
# getD()    : float
# getE()    : float
# getF()    : float

class LinearEquation :
    def __init__(self, a = 1, b = 1, c = 1, d = 1, e = 1, f = 1) :
        self.__a = a
        self.__b = b
        self.__c = c
        self.__d = d
        self.__e = e
        self.__f = f
    # 생성자

    def getAD_BC(self) :    return (self.__a * self.__d - self.__b * self.__c)
    # ad - bc 를 반환하는 메소드
    # 수식에서 자주 사용된다

    def isSolvable(self) :
        if self.getAD_BC() != 0 :
            return True
        else : return False
    # 해가 존재하는지 알려주는 메소드

    def getX(self) :
        return (self.__e * self.__d - self.__b * self.__f) / self.getAD_BC()
    def getY(self) :
        return (self.__a * self.__f - self.__e * self.__c) / self.getAD_BC()
    # 해를 반환하는 메소드

    def print(self) :
        if(self.isSolvable()) :
            print("x는 " + str(self.getX()) + "이고, y는 " + str(self.getY()) + "입니다.")
        else :
            print("이 방정식은 해가 없습니다.")
    # 해가 존재하면 해를 출력하고, 존재하지 않으면 안내 메세지 출력


    # 모든 필드 값에 대한 getter
    def getA(self) : return self.__a
    def getB(self) : return self.__b
    def getC(self) : return self.__c
    def getD(self) : return self.__d
    def getE(self) : return self.__e
    def getF(self) : return self.__f
