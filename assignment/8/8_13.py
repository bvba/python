def prefix(s1, s2) :
    preStr = '' # 공통 접두어
    if type(s1) == type(s2) == type('') :   # 타입 검사
        for i in range(0, min(len(s1), len(s2))) :
            # 두 배열 중 짧은 배열의 길이만큼 반복문 수
            if s1[i] == s2[i] : # 두 배열의 원소가 같으면 공통 접두어에 추가
                preStr += s1[i]
            else :  # 다른 경우 공통 접두어 반환
                return preStr
        return preStr
        # 공통 접두어가 없는 경우 '' 반환

s1 = input("문자열을 입력해주세요 : ")
s2 = input("문자열을 입력해주세요 : ")
print("최장 공통 접두어는 \"" + prefix(s1, s2) + "\" 입니다.")
# 결과 화면 출력
