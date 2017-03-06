import math

def isPrime(number) :
    if number == 2 : return True        # 2는 짝수 소수이므로 예외처리
    if number % 2 == 0 : return False   # 짝수인경우 False 반환
    i = 3
    while i <= math.sqrt(number) :
        # 약수는 쌍을 이루기때문에 sqrt(num)까지만 검사해도 충분
        if number % i == 0 :
            return False    # 한 번이라도 약수가 있다면 False 반환
        i += 2
    return True             # 약수가 한개도 없다면 True 반환

print("2 ", end = '')
for i in range(3, 10000 + 1, 2) :
    if(isPrime(i)) :    # i가 소수인경우 출력
        print(i,'', end = '')
