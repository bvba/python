# 두 점 사이의 거리를 구하는 함수
def distance(p1, p2) :
    x = (p1[0] - p2[0]) ** 2
    y = (p1[1] - p2[1]) ** 2
    z = (p1[2] - p2[2]) ** 2
    return round((x + y + z) ** 0.5, 3)

# 좌표를 저장하는 리스트
points = [[-1, 0, 3], [-1, -1, -1], [4, 1, 1], [2, 0.5, 9],
          [3.5, 2, -1], [3, 1.5, 3], [-1.5, 4, 2], [5.5, 4, -0.5]]

# 서로 가장 가까운 두 점의 인덱스를 저장하는 리스트
# 처음 두 점이 가장 가깝다고 가정한 후 반복문을 통해 실제로 가장 가까운 두 점을 구해준다
minn = [0, 1]
for i in range(len(points)) :
    for j in range(i + 1, len(points)) :
        # 반복문을 통해 두 점 사이의 거리가 기존의 최솟값 보다 작은 경우 최솟값을 재설정
        if distance(points[i], points[j]) < distance(points[minn[0]], points[minn[1]]) :
            minn[0] = i
            minn[1] = j

# 두 점 사이의 거리가 가장 가까운 두 점을 출력
# 두 점 사이의 거리도 같이 출력해준
print(points[minn[0]], points[minn[1]],
      'distance : ', distance(points[minn[0]], points[minn[1]]))
