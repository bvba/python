import math

summ = 0
sq_sum = 0
n = 10
print(str(n)+"개의 숫자를 입력하세요 : ")
for i in range(0, n) :
    num = eval(input()) # 숫자를 입력받음
    summ += num         # 입력받은 숫자를 summ에 추가
    sq_sum += num ** 2  # 입력받은 숫자의 제곱을 sq_sum에 추가
avg = float(summ) / n   # summ을 이용하여 평균값 계산
deviation = math.sqrt((sq_sum - summ ** 2 / n) / (n - 1))
# sq_sum, summ, n을 이용하여 편차 계산
print("평균은", avg, "입니다.")
print("표준 편차는", round(deviation, 5), "입니다.")
