total, tip = eval(input("소계와 팁 비율을 입력하세요 : "))
tip = total * tip * 0.01        # tip 계산
total += tip                    # 전체 가격에 tip 추가
tip = round(tip, 2)             # 소수점 뒤 2자리
total = round(total, 2)
print("팁은", tip, "이고, 총액은", total, "입니다.")
