# 해당 도시를 기준으로 나머지 도시들까지의 거리의 합을 구하는 함수
def distance(lst, cri) :
    sum = 0
    for i in range(len(lst)) :
        # 기준이 되는 도시에서 나머지 도시까지의 도달거리를 구해준다.
        # 제자리로 오는 경우 거리가 0이 되므로 예외처리를 해줄 필요가 없다
        sum += ((lst[i][0] - lst[cri][0]) ** 2 +
                (lst[i][1] - lst[cri][1]) ** 2) ** 0.5
    return sum

cityNum = eval(input("도시의 개수를 입력하세요 : "))
lst = [eval(i) for i in str(input("도시의 좌표를 입력하세요 : ")).split(' ')]
points = [[lst[i * 2], lst[i * 2 + 1]] for i in range(cityNum)]

# 각 도시들까지의 도달거리가 가장 작은 도시의 인덱스를 저장하는 minn
# 첫번째 도시가 최솟값을 갖는다고 가정한다
minn = 0
for i in range(1, cityNum) :
    # 반복문을 통해 기존의 최솟값보다 더 작은 도달거리를 갖는 도시가 있다면
    # 최솟값을 재설정해준다
    if distance(points, minn) > distance(points, i) :
        minn = i

print("중심도시는 " + "(" + str(points[minn][0]) + ", " +
      str(points[minn][1]) + ") 에 있습니다.")
