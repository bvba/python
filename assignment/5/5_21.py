import math

for i in range(0, 8):
    for j in range(0, 8 + i):   # 열의 값은 (중앙 + 행) 까지 증가
        if j < 8 - i - 1:   # 열이 (중앙 - 행) 보다 작은 경우 공백 출력
            print("    ", end = "")
        if j >= 8 - i - 1:  # 열이 (중앙 - 행) 보다 큰 경우 위치에 맞는 수 출력
            print(format(2 ** (i - abs(7 - j)), "4d"), end = "")
            # 2 ^ (행 - (중앙에서 떨어진 거리)) 출력
    print()
