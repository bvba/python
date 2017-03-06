
cnt = 0
maxNum = 0  # 양수만 들어온다고 가정
num = 1     # while문을 처음 한 번 수행시키기 위한 초기값
while num : # 0 이 입력되면 반복문 종료
    num = eval(input("숫자를 입력하세요.(0은 입력 종료) : "))
    if num > maxNum :   # 입력받은 숫자가 기존의 최댓값보다 큰 경우
        maxNum = num    # 최댓값 초기화
        cnt = 0         # 최댓값 빈도수 초기화
    if num == maxNum :  # 최댓값인경우 빈도수 + 1
        cnt = cnt + 1
print("가장 큰 수는", maxNum, "입니다.")
print("가장 큰 수가 나나탄 빈도수는", cnt, "번 입니다.")
