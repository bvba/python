def decimalToBinary(value) :
    binaryString = ''   # 이진수를 저장하기위한 문자열
    bi = 1              # 십진수를 나누는 수 2^x 
    while bi < value :  # 2^x 를 십진수보다 크도록 설정
        bi *= 2
    while bi > 0 :      # 나누는 수가 1일때 까지 수행
        binaryString += str(value // bi)    # 십진수를 bi로 나눴을때의 몫을 추가
        value %= bi     # 십진수에 십진수를 bi로 나눈 나머지 저장
        bi = int(bi / 2)# bi = 2^(x-1)
    return binaryString # 2진수 배열 반환

value = eval(input("십진수를 입력해주세요 : "))
print(str(value) + "(은)는 이진수로 " + decimalToBinary(value) + "입니다.")
# 결과 화면 출력
