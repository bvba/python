import math

def isValid(side1, side2, side3) :
    ar = [side1, side2, side3]
    ar.sort()
    if ar[0] + ar[1] > ar[2] :
        # 가장 긴 변의 길이가 나머지 두 변의 길이를 합친 것 보다 긴 경우
        # 삼각형이 만들어 질 수 있으므로 True 반환
        return True
    else :  # 아닌경우 삼각형을 만들 수 없으므로 False 반환
        return False

def area(side1, side2, side3) :
    s = (side1 + side2 + side3) / 2.0   # 헤론의 공식 사용을 위한 s 값 설정

    # 헤론의 공식을 이용하여 삼각형의 넓이를 구하고 반환
    return math.sqrt(s * (s - side1) * (s - side2) * (s - side3))
