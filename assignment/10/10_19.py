import random

numBall = eval(input("떨어뜨릴 공의 개수를 입력하세요 : "))
numSlot = eval(input("콩 기계의 슬롯 개수를 입력하세요 : "))

cnt = [0 for x in range(numSlot)]
# 해당 슬롯에 공이 몇개 있는지 나타내는 리스트
for i in range(numBall) :
    #공을 떨어트린다
    pos = numSlot / 2
    # 공의 위치를 나타냄
    # 처음에는 슬롯의 중간에 위치함
    for j in range(numSlot - 1) :
        # 공은 슬롯 - 1 개의 분기점을 지남
        dir = random.randint(0, 1)
        # 공이 떨어지는 방향을 난수로 설정(0 : L, 1 : R)
        pos += -0.5 if dir == 0 else 0.5
        # 왼쪽인 경우 공의 위치는 -0.5, 오른쪽인 경우 +0.5
        print('L' if dir == 0 else 'R', end = '')
        # 공의 방향 출력
    print()
    pos -= 0.5
    # 공의 위치를 인덱스로 사용하기 위해 -0.5를 해준다(배열의 시작은 0이기 때문)
    cnt[int(pos)] += 1
    # 공이 떨어진 위치에 공의 개수를 1 만큼 추가

numMax = max(cnt)
# 가장 많이 쌓인 공의 개수 저장
for i in range(numMax) :
    # 행의 높이는 가장 많이 쌓인 공의 개수로 설정
    for j in range(numSlot) :
        # 열은 슬롯의 개수만큼 설정
        if cnt[j] == numMax - i :
            # 위에서 i번째에 공이 있는 경우 공이 있음을 출력
            print('0', end = '')
            cnt[j] -= 1             # 공을 한 개 빼준다(출력했기 때문에)
        else : print(' ', end = '') # 공이 없는 경우 공백 출력
    print() # 줄 바꿈

# 몇 번째 열인지 보기 쉽도록 UI 설정
print('-' * numSlot)
for x in range(1, numSlot + 1) :
    print(x, end = '')
