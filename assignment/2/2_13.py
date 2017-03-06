num = eval(input("정수를 입력하세요 : "))

print( int(num / 1000))
#       num의 1000의 자리 수

print(int((num % 1000) / 100))
#       num의 100의 자리 수

print(int((num % 100) / 10))
#       num의 10의 자리 수

print(num % 10)
#       num의 1의 자리 수

