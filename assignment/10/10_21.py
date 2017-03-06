#   lock = [False for x in range(100)]
#   사물함의 상태를 나타내는 리스트


#   for i in range(100) :
#       for j in range(i, 100, i + 1) :
#           # 번호가 i + n * (i + 1)인 사물함의 상태를 바꿈
#           lock[j] = not lock[j]
#
#   for i in range(100) :
#       if lock[i] :
#           # 열려있는 사물함의 번호 출
#           print(i + 1)


# 약수의 개수가 짝수인 경우 open, close 가 반복되어
# 결국에는 닫힌 상태가 된다

# 결과적으로 약수의 개수가 홀수인 사물함만 열려있게 되는데
# 약수의 개수가 홀수인 경우는 제곱수뿐이다.
# 모든 제곱수를 출력하면 된다.
i = 1
while i * i <= 100 :
    print(i * i)
    i += 1
