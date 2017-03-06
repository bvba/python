def count(s1, s2) :
    if type(s1) == type(s2) == type('') :   # 타입 검사
        return s1.count(s2) # s1에 s2가 들어간 횟수를 바환

s1 = input("문자열을 입력해주세요 : ")
s2 = input("문자열을 입력해주세요 : ")

print("\"" + s2 + "\"(은)는 \"" + s1 + "\"에 " + str(count(s1, s2)) + "번 나옵니다.")
# 실행 결과 출력
