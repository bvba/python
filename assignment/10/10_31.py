def count(s) :
    cnt = [0 for x in range(10)]
    # 길이가 10인 cnt 생성 및 모든 원소를 0으로 초기화
    for i in range(len(s)) :
        # 문자열의 길이만큼 반복
        if int(s[i]) in range(10) :
            # 문자열의 i번째 문자가 0~9 사이의 숫자이면
            cnt[int(s[i])] += 1
            # 해당 숫자의 cnt를 1 증가
    return cnt

string = input("문자열을 입력하세요 : ")
counts = count(string)

for i in range(10) :
    if counts[i] :
        # counts[i]가 1 이상인 경우 해당 숫자의 빈도 수 출력
        print(i, '-', counts[i], "번 나타탑니다.")
