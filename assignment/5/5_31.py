year, dayOfTheWeek = eval(input("연도와 요일을 입력하세요(일~토 = 0~6) : "))
# 일 : 0, 월 : 1, ..., 토 : 6

for month in range(1, 12 + 1):
    if month == 2:  # 2월인 경우 윤년체크
        if (year % 4 == 0) and (year % 100 or year % 400 == 0):
            maxDay = 29 # 윤년인 경우 2월의 마지막 날은 29
        else :
            maxDay = 28 # 윤년이 아닌 경우 2월의 마지막 날은 28
    elif month in [1, 3, 5, 7, 8, 10, 12]:
        maxDay = 31     # 1, 3, 5, 7, 8, 10, 12월의 마지막 날은 31
    else :
        maxDay = 30     # 나머지 달의 마지막 날은 30

    print("       ", year, "년", month, "월")
    print("-----------------------------")
    print("  일  월  화  수  목  금  토 ")

    # 새로운 달을 출력 할 때 시작 요일까지 공백을 몇 번 출력했는지 세주는 변수
    cnt = 0
    # cnt가 해당 달의 시작 요일보다 작은 경우 공백 출력
    while cnt < dayOfTheWeek:
        print("    ", end = "")
        cnt += 1

    # 달력의 일 출력
    for day in range(1, maxDay + 1):
        print(format(day, "4d"), end = '')
        # 요일을 1증가
        dayOfTheWeek += 1
        if dayOfTheWeek == 7:   # 요일이 7(토요일을 넘긴경우)이면
            print()             # 줄바꿈
            dayOfTheWeek = 0    # 요일을 0으로 설정
    print()
