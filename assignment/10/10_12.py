def gcd(number) :
    gcdList = [x for x in range(1, number[0] + 1) if number[0] % x == 0]
    # 첫번째 숫자의 약수를 리스트에 저장
    for i in range(1, len(number)) :
        # 첫번째 숫자의 약수가 2~5번째 숫자의 약수인지 검사
        j = 0
        while j < len(gcdList) :
            # 모든 약수를 검사
            if number[i] % gcdList[j]  != 0 :
                # 만약 첫번째 숫자의 약수가 i번째 숫자의 약수가 아닌 경우
                gcdList.pop(j)
                # 리스트에서 제거
            j += 1
    return gcdList[len(gcdList) - 1]    # 모든 숫자의 최대 공약수 반환

s = input("5개의 정수를 입력하세요 : ")
items = s.split()                   # 문자열을 분할 후
number = [eval(x) for x in items]   # 숫자로 변환하여 저장
print(number, "의 최대 공약수는",gcd(number), "입니다.")
