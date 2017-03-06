# 좌표를 원소로 갖는 리스트를 정렬하는 함수
# bubble 정렬을 이용한다
def sort(points) :
    # 루프를 돌 동안 스왑이 이루어졌는지 확인하는 flag
    swapped = True
    # 루프를 돌 동안 스왑이 이루어지지 않았다면
    # 리스트의 정렬이 완료 된 것이므로 반복을 마친다
    while swapped :
        # 초기 설정
        swapped = False
        i = 0
        for j in range(len(points) - i - 1) :
            # y 좌표 값에 따라 정렬
            if points[j][1] > points[j + 1][1] :
                swap(points, j, j + 1)
                swapped = True
            # y 좌표 값이 같은 경우 x좌표 값에 따라 정렬
            elif points[j][1] == points[j + 1][1] :
                if points[j][0] > points[j + 1][0] :
                    swap(points, j, j + 1
                    swapped = True
        i += 1

# 리스트의 i, j번째 원소를 서로 바꿔주는 함수
def swap(lst, i, j) :
    tmp = lst[i]
    lst[i] = lst[j]
    lst[j] = tmp
    
lst = [eval(i) for i in str(input("점 리스트를 입력해주세요 : ")).split(' ')]
points = [[lst[i * 2], lst[i * 2 + 1]] for i in range(len(lst) // 2)]
sort(points)
print("정렬된 리스트는\n", points, "입니다.")
