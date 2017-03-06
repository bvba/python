year, month = eval(input("년도와 월을 입력하세요 : "))

if month in [1, 3, 5, 7, 8, 10, 12]:
    # month 가 1, 3, 5, 7, 8, 10, 12 중 하나라면 31일 까지 있음을 출력
    print(year, "년", month, "월은 31일까지 있습니다.")
elif month in [4, 6, 9, 11]:
    # month 가 4, 6, 9, 11 중 하나라면 30일 까지 있음을 출력
    print(year, "년", month, "월은 30일까지 있습니다.")
else:   # 2월인 경우
    if (year % 4 == 0) and (year % 100 != 0 or year % 400 == 0):
        # 윤년인 경우 29일 출력
        print(year, "년", month, "월은 29일까지 있습니다.")
    else:
        # 윤년이 아닌 경우 28일 출력
        print(year, "년", month, "월은 28일까지 있습니다.")
