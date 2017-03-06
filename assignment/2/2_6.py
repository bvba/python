num = eval(input("0과 1000사이의 숫자를 입력하세요 : "))

sum = 0
sum += num % 10             # 1의 자리 수 합
num = int(num / 10)         # num의 맨 뒤 숫자를 없앰
sum += num % 10             # 10의 자리 수 합
num = int(num / 10)         # num의 맨 뒤 숫자를 없앰
sum += num % 10             # 100의 자리 수 합

print("각 자릿수의 합은", sum, "입니다.")
