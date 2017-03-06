weight = eval(input("몸무게를 파운드로 입력하세요 : "))
height = eval(input("키를 인치로 입력하세요 : "))

weight *= 0.45359237
# lb -> kg 으로 변환
height *= 0.0254
# inch -> m 로 변환

bmi = weight / (height ** 2)
# bmi 계산

bmi = round(bmi, 4)

print("BMI는", bmi, "입니다.")
