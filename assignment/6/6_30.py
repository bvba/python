import random

def roll() :
    return random.randint(1, 6), random.randint(1, 6)
    # 주사위를 굴리는 함수, 두 개의 주사위 값을 반환한다

def craps() :
    first = roll()  # 처음으로 굴린 주사위 값을 저장
    firstSum = sum(first)   # 두 개의 주사위 값의 합을 저장
    
    if firstSum in [7, 11] :    # 합이 7, 11 중 하나이면
        return True             # True(win) 반환
    elif firstSum in [2, 3, 12] :   # 합이 2, 3, 12 중 하나이면
        return False            # False(lose) 반환
    else :
        second = roll()         # 이외의 경우 주사위를 새로 굴린다.
        secondSum = sum(second)
        while not(secondSum in [7, firstSum]) :
            # 새로 굴린 주사위의 합이 7
            # 또는 처음의 주사위 값의 합과 같을때까지
            # 주사위를 굴린다.
            second = roll()
            secondSum = sum(second)
            
        if secondSum == 7 : # 새로 굴린 주사위의 합이 7인경우
            return False    # False(lose) 반환
        elif secondSum == firstSum :    # 처음의 주사위 값의 합과 같은 경우
            return True     # True(win) 반환

win = 0;
for i in range(0, 10000) :
    win += craps()  # craps() 가 True(win)을 반환할 경우 win++
print("10,000번 중", win, "번 이겼습니다. 승률은", win / 100.0, "입니다.")
# 총 이긴 횟수와 승률 출력
