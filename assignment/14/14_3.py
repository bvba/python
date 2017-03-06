import os.path
import sys

# .py 인코딩 형식을 ANSI로 설정해주세요....

fileName = input("파일명을 입력하세요 : ").strip()

if not os.path.isfile(fileName) :   # 파일 존재 여부 확인
    print("error")
    sys.exit()

try :   # 파일이 정상적으로 열렸는지 체크
    file = open(fileName, "r")
except IOError :
    print("IOError")

string = file.read()    # 파일의 문자를 읽음
string.replace(':', ' ')# 키워드와 문자가 붙어있는 경우에도
string.replace('(', ' ')# 키워드를 정상적으로 세기 위해
string.replace(';', ' ')# ':', '(', ';' 문자를 공백으로 바꿔줌

text = string.split()   # 공백 기준으로 문자열을 분리하여 text에 저장

keyWords = {"and", "as", "assert", "break", "class", "continue", "def", "del",
            "elif", "else", "except", "False", "finally", "for", "from",
            "global", "if", "import", "in", "is", "lambda", "None",
            "nonlocal", "not", "or", "pass", "raise", "return", "True",
            "try", "while", "with", "yield"}
# 키워드를 저장하는 set
keyCount = {}
# 소스 코드에 존재하는 키워드의 빈도를 저장하는 dict
for i in range(len(text)) :
    if text[i] in keyWords :    # 키워드이면 빈도수를 설정
        if text[i] in keyCount :# 나온 적 있는 키워드인 경우 빈도수 + 1
            keyCount[text[i]] += 1
        else :                  # 처음 나온 키워드인 경우 dict에 추가 & 값 = 1로 설정
            keyCount[text[i]] = 1
for key in keyCount :   # 출현한 키워드의 종류와 빈도 수 출력
    print(str(key) + ":" + str(keyCount[key]))
file.close()
