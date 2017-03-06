import math

a, b, c = eval(input("a, b, c를 입력하세요 : "))
discriminant = b ** 2 - 4 * a * c
# 판별식을 구하여 저장

if discriminant > 0:    # 판별식이 양수인 경우 두개의 근을 구하여 출력
    ans1 = (-b - math.sqrt(discriminant)) / (2 * a)
    ans2 = (-b + math.sqrt(discriminant)) / (2 * a)
    print("실근은", round(ans1, 3), "이고", round(ans2, 3), "입니다.")
elif discriminant == 0: # 판별식이 0 인경우 중근을 출력
    ans1 = -b / (2 * a)
    print("실근은", round(ans1, 3), "입니다.")
else :                  # 판별식이 음수인 경우 근이 없음을 알려줌
    print("이 방정식은 실근이 존재하지 않습니다.")
