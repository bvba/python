def binaryToDecimal(binaryString) :
    if type(binaryString) == type('') : # 타입 검사
        bi = 1      # 2 ^ x 를 나타냄
        num = 0     # 10진수를 저장
        for i in range(len(binaryString) - 1, 0 - 1, -1) :
            # 가장 작은 숫자 (2^0 부터 계산)
            if int(binaryString[i]) >= 2 :
                # 이진수가 아닌 경우 오류 메세지 출력
                print("잘못된 입력입니다")
                return -1   # 오류임을 알려주는 반환값
            num += int(binaryString[i]) * bi
            # (1 or 0) * 2^x 를 num에 추가
            bi *= 2     # bi = 2^(x+1)
        return num  # 십진수 반환

binaryString = input("이진수를 입력해주세요 : ")
decimal = binaryToDecimal(binaryString)
if decimal >= 0 :
    print(binaryString + "는 십진수로 " + str(binaryToDecimal(binaryString)))
# 정상적인 입력인 경우에만 결과 화면 출력
