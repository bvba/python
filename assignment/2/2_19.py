investment = eval(input("투자금을 입력하세요 : "))
interest = eval(input("연이율을 입력하세요(%) : "))
year = eval(input("년수를 입력하세요 : "))

value = investment * (1 + interest / 12 * 0.01) ** (year * 12)
# 가치 계산

value = round(value, 2)

print("누적된 가치는", value, "입니다.")
