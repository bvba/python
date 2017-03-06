fileName = input("파일명을 입력하세요 : ")

fileBefore = open(fileName, "r")    # 원본 파일
fileAfter = open(fileName.replace(".txt", "After.txt"), "w")    # 수정 파일

before = input("교체될 이전 문자열을 입력하세요 : ")  # 교체될 문자열 입력
after = input("이전 문자열을 대체할 새로운 문자열을 입력하세요 : ")
# 교체할 문자열 입력

for line in fileBefore :
    fileAfter.write(line.replace(before, after))
    # 원본 line에 있는 before 문자열을 after문자열로 바꿔서 수정 파일에 입력
    
fileBefore.close()
fileAfter.close()
print("완료되었습니다.")
