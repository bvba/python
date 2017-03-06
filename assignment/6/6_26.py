import math

def isPrime(num) :
    if num == 1 : return False  # 1은 소수가 아니므로 False
    if num == 2 : return True   # 2는 소수이므로 True
    if num % 2 == 0 : return False  # 2를 제외한 짝수는 False
    for i in range(3, int(math.sqrt(num) + 1), 2) :
        # 3부터 sqrt(num) 까지 num의 약수인지 검사 짝수는 검사하지 않음
        if num % i == 0 : return False  # 약수이면 False 반환
    return True # sqrt(num) 까지 약수가 나오지 않으면 True 반환

print(format('p', ">7s"), format("2^p - 1", ">12s"))
for i in range(1, 32) : # 지수의 범위는 1부터 31까지
    if isPrime(2 ** i - 1) :    # 2^i 가 소수인경우
        print(format(i, "7d"), format(2 ** i - 1, "12d"))
        # 메르센 소수임을 출력
