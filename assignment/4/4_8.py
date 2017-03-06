n1, n2, n3 = eval(input("세 정수를 입력하세요 : "))

if n1 > n2:
    tmp = n1
    n1 = n2
    n2 = tmp
if n1 > n3:
    tmp = n1
    n1 = n3
    n3 = tmp
# 이 부분 까지가 가장 작은 값을 n1 에 저장하는 과정

if n2 > n3:
    tmp = n2
    n2 = n3
    n3 = tmp
# 가장 작은 수를 제외한 두 수 중 작은 수를 n2, 큰 수를 n3에 저장

print(n1, n2, n3)
