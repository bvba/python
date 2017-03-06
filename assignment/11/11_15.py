# 점들이 한 직선 위에 있는지 검사하는 함수
def sameLine(points) :
    x = [points[i * 2] for i in range(len(points) // 2)]
    y = [points[i * 2 + 1] for i in range(len(points) // 2)]
    # 점들의 x, y좌표를 각각 따로 저장한다

    # 점들이 수직으로 분포하는지 나타내는 flag
    isVertical = 1
    for i in range(1, len(y)) :
        if y[i] != y[0] : isVertical = 0
        # y좌표가 다른 경우가 있다면 수직이 아니다
    if isVertical : return True
    # 수직인 경우 모두 한 직선 위에 있으므로 True 반환
    
    else :
        # 처음 두 점의 기울기를 구한다
        m = round((x[0] - x[1]) / (y[0] - y[1]), 2)
        for i in range(2, len(x)) :
            # 처음 두 점의 좌표를 통해 직선의 방정식을 만들고
            # 나머지 점들이 그 직선 위에 있지 않은 경우 Fals 반환
            if round(m * (x[i] - x[0]) - (y[i] - y[0]), 2) != 0 : return False
        # 모든 점이 동일 직선위에 있는 경우 True 반환
        return True
        
points = [eval(i) for i in str(input("다섯 개의 점을 입력하세요 : ")).split(' ')]
if sameLine(points) : print("다섯 개의 점은 같은 직선 위에 있습니다.")
else : print("다섯 개의 점은 같은 직선 위에 있지 않습니다.")
