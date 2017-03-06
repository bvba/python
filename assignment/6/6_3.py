def reverse(number) :
    rvs = ''
    while number > 0 :
        rvs += str(number % 10)     # number의 1의 자리 수를 rvs에 추가
        number = int(number / 10)   # number의 1의 자리 수를 없앰
    return int(rvs) # 뒤집힌 수 반환

def isPalindrome(number) :
    if(number == reverse(number)) : # 뒤집은 수와 기존의 수가 같은 경우
        return True                 # True 반환	
    else :              # 다른 경우
        return False    # False 반환

num = eval(input("숫자를 입력하세요 : "))
print("정수의 역은", reverse(num), "입니다.")   # 뒤집은 수 출력
if isPalindrome(num) :  # 대칭수인지 아닌지 알려준다
    print(num, "은 대칭수입니다.")
else :
    print(num, "은 대칭수가 아닙니다.")
