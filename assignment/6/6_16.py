def numberOfDaysInYear(year) :
    if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0) :
        return 31 * 7 + 30 * 4 + 29    # 윤년인 경우 2월일 때 29일을 더해줌
    else : return 31 * 7 + 30 * 4 + 28 # 윤년이 아닌 경우 2월일 때 28일을 더해줌

daySum = 0      # 총 일수
for i in range(2010, 2020 + 1) :
    daySum += numberOfDaysInYear(i)     # 해당 년도의 일 수를 더함

print("2010년부터 2020년까지는 총", daySum, "일 입니다.")
