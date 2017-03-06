# class Fan
# 
# SLOW = 1      : int
# MEDIUM = 2    : int
# FAST = 3      : int
#
# - speed   : int
# - on      : bool
# - radius  : float
# - color   : str
#
# Fan(speed : int, radius : float, color : str, on : bool)
# getSpeed()    : int
# getOn()       : bool
# getRadius     : float
# getColor      : str
# setSpeed(int) : None
# setOn(bool)   : None
# setRadius(float)  : None
# setColor(str) : None

class Fan :
    LOW     = 1
    MEDIUM  = 2
    FAST    = 3
    def __init__(self, speed = LOW, radius = 5.0, color = "blue", on = False) :
        self.__speed = speed
        self.__radius = radius
        self.__color = color
        self.__on = on
    # 생성자

    def print(self) :
        print("Speed :", self.__speed)
        print("Radidus :", self.__radius)
        print("Color :", self.__color)
        print("OnOff :", self.__on, '\n')
    # 클래스의 필드 값 출력

    # 모든 필드 값에 대한 getter, setter
    def getSpeed(self)  :   return self.__speed
    def getOn(self)     :   return self.__on
    def getRadius(self) :   return self.__radius
    def getColor(self)  :   return self.__color
    def setSpeed(self, speed)   :   self.__speed = speed
    def setOn(self, on)         :   self.__on = on
    def setRadius(self, radius) :   self.__radius = radius
    def setColor(self, color)   :   self.__color = color
