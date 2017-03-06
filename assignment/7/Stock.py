# class Stock
# 
# - symbol  : str
# - name    : str
# - previousClosingPrice    : float
# - currentPrcie            : float
#
# Stock(  symbol : str, name : str,
#       previousClosingPrice : float, currentPrice : float)
# getName()     : str
# getSymbol()   : str
# getPreviousClosingPrice() : str
# setPreviousClosingPrice(previosClosingPrice : float) : None
# getCurrentPrice() : str
# setCurrentPrice(currentPrice : str) : None
# getChangePercent() : float

class Stock :
    def __init__(self, symbol = "KU", name = "Koreatech",
                 previousClosingPrice = 500.0, currentPrice = 3141.59) :
        self.__symbol = symbol
        self.__name = name
        self.__previousClosingPrice = previousClosingPrice
        self.__currentPrice = currentPrice
    # 생성자
        
    def getChangePercent(self) :
        return (self.__currentPrice / self.__previousClosingPrice - 1) * 100.0
    # 전일 대비 가격 변동률을 구하는 메소드
    
    def print(self) :
        print("Symbol :", self.__symbol)
        print("Name :",self.__name)
        print("Previous Closing Price :", self.__previousClosingPrice)
        print("Current Price :", self.__currentPrice)
        print("Change Percnet :", format(self.getChangePercent(), "3.3f"), '\n')
    # 클래스의 필드 값과 변동률을 출력

    # 모든 필드 값에 대한 getter, setter
    def getName(self) :     return self.__name
    def getSymbol(self) :   return self.__symbol
    def getPreviousClosingPrice(self) : return self.__previousClosingPrice
    def setPreviousClosingPrice(self, previousClosingPrice) :
        self.__previosClosingPrice = previousClosingPrice
    def getCurrentPrice(self) : return self.__currentPrice
    def setCurrentPrice(self, currentPrice) :
        self.__currentPrice = currentPrice
