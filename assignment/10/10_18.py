# list1 은 n * n 배열에서 각 열에 있는 퀸의 행을 저장한다.
# ex) ['1', '2'] 는 (1, '1'), (2, '2')에 퀸이 위치함.

# col 은 list1의 열을 나타낸다.
# ex) list1[col] -> (col, list1[col])
# ex) list1[0] == 3 인 경우 퀸은 (0, 3)에 위치함.

completeFlag = 0
# global 변수로, 해가 나오면 더 이상 해를 찾지 않도록 해준다.


def Promising(list1, col) :
    # 현재 체스판 상황에서 퀸끼리 공격 가능한지 체크하는 함수
    # 공격 가능하면 False 반환
    
    if col < 1 : return True
    # 첫 번째 퀸을 놓는 상황을 뜻함
    # 이 경우에는 퀸이 어디에 있든 퀸끼리 공격 불가
    else :
        # 0행부터 col행 까지 퀸끼리 공격 가능한지 체크
        # 퀸을 같은 열에 배치하지 않으므로 같은 열인지는 체크하지 않아도 됨
        # list1[i] == list1[col] : 같은 행인지 체크
        # abs(list1[i] - list1[col]) == abs(i - col) : 대각선(기울기 1)에 위치하는지 체크
        for i in range(col) :
            if list1[i] == list1[col] or abs(list1[i] - list1[col]) == abs(i - col) :
                # 같은 행 또는 대각선에 위치한 경우 퀸끼리 공격 가능
                return False
        return True
        # 검사가 끝날 때 까지 공격가능한 경우가 없다면 True 반환

def nQueen(list1, col, n) :
    global completeFlag
    # 전역변수
    
    for i in range(n) :
        list1[col] = i
        # col 행의 i열에 퀸을 배치
        if Promising(list1, col) :
            # 퀸끼리 공격 가능한지 검사(공격 불가능한 경우에 실행)
            if col == n - 1 :
                # 퀸의 개수가 n인 경우(col은 인덱스이므로 1 작다)
                # 정답이 완성 된 것 이므로 출력해준다.
                printList(list1, n)
                completeFlag = 1 # 해가 나왔음을 설정
                return
            elif completeFlag != 1  :
                # 해가 나오지 않은 경우에만 해를 찾음
                nQueen(list1, col + 1, n)
                # 다음 열에 퀸을 배치하도록 recursion

def printList(list1, n) :
    # 완성된 체스판 출력 함
    for i in range(n) :
        for j in range(n) :
            print('|', end = '')
            print('Q', end = '') if list1[i] == j else print(' ', end = '')
        print('|', end = '\n\n')

size = 10
list1 = [0] * size
nQueen(list1, 0, size)
