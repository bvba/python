import math

for i in range(2, 10000 + 1) :
    sum = 1
    for j in range(2, int(math.sqrt(i)) + 1) :
        # 약수는 쌍을 이루기 때문에 sqrt(num)까지만 검사해도 충분하다
        if i % j == 0 :     # j가 약수인경우
            sum += j        # j를 sum에 더함
            if j != i / j : # j가 제곱근이 아닌 경우에만
                sum += i / j# j와 쌍을 이루는 약수를 sum에 더함
    if sum == i :   # i가 완전수인경우 i출
        print(i)
