def isConsecutiveFour(lst) :
    # 2차원 리스트의 모든 점에서 검사를 수행한다
    for i in range(len(lst)) :
        for j in range(len(lst[i])) :
            # 행, 열, 대각선 각각의 방향으로 4개의 연속된 숫자가 있는지 검사한다
            # 검사 결과가 참인 경우 True 반환
            if j < len(lst[i]) - 3 and checkRow(lst, i, j) : return True
            if i < len(lst) - 3 and checkCol(lst, i, j) : return True
            if i < len(lst) - 3 and j < len(lst[i]) - 3 and checkDiagonalRight(lst, i, j) : return True
            if i < len(lst) - 3 and 3 <= j and checkDiagonalLeft(lst, i, j) : return True
    # 모든 점에서 한번이라도 만족하는 경우가 없다면 False 반환
    else : return False

def checkRow(lst, i, j) :   # 해당 행에서 4개의 연속된 숫자가 있는지 검사
    for index in range(1, 4) :
        # 만족하지 않는 경우가 있다면 False 반환
        if lst[i][j] != lst[i][j + index] : return False
    return True # 모두 만족하는 경우 True 반환

def checkCol(lst, i, j) :   # 해당 열에서 4개의 연속된 숫자가 있는지 검사
    for index in range(1, 4) :
        # 만족하지 않는 경우가 있다면 False 반환
        if lst[i][j] != lst[i + index][j] : return False
    return True # 모두 만족하는 경우 True 반환

def checkDiagonalRight(lst, i, j) : # 오른쪽 대각선 검사
    for index in range(1, 4) :
        # 만족하지 않는 경우가 있다면 False 반환
        if lst[i][j] != lst[i + index][j + index] : return False
    return True # 모두 만족하는 경우 True 반환

def checkDiagonalLeft(lst, i, j) :  # 왼쪽 대각선 검사
    for index in range(1, 4) :
        # 만족하지 않는 경우가 있다면 False 반환
        if lst[i][j] != lst[i + index][j  - index] : return False
    return True # 모두 만족하는 경우 True 반환

row = eval(input("행의 개수를 입력하세요 : "))
col = eval(input("열의 개수를 입력하세요 : "))
lst = [[] for i in range(row)]

print("리스트의 값을 입력하세요 : ")
for i in range(row) :
    lst[i] = [eval(i) for i in str(input(str(i) + "행 : ")).split(' ')]

print(isConsecutiveFour(lst))   # 결과 출력
