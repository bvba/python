def isProper(pw) :
    if type(pw) == type('') :   # pw 타입 검사
        if len(pw) >= 8 :       # pw 길이가 8 이상인지 검사
            if pw.isalnum() :   # pw 가 숫자와 알파벳으로 이루어져있는지 검사
                cnt = 0         # 숫자의 개수를 세기 위한 변수
                for ch in pw :  # 문자열의 처음부터 끝까지 확인
                    if ch.isdigit() :   # 문자가 숫자인 경우
                        cnt += 1        # 개수 추가
                        if cnt >= 2 :   # 숫자가 2개 이상이면
                            return True # True 반환
    return False
    # 위의 조건을 하나라도 만족하지 못하면 False 반

pw = input("패스워드를 입력하세요 : ")

if(isProper(pw)) :  # 함수 반환값에 따라 결과 메세지 출력
    print("올바른 패스워드 입니다.")
else :
    print("올바르지 않은 패스워드 입니다.")
