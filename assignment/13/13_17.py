# assistant 조교수
# associate 부교수
# full      정교수

import urllib.request

count = [0, 0, 0]
money = [0, 0, 0]   # 순서대로 assistant, associate, full

file = urllib.request.urlopen("http://cs.armstrong.edu/liang/data/Salary.txt")
# 웹에서 데이터를 읽어온다
line = '.'  # do while 구현을 위한 설정
while line != '' :  # 입력이 없을 때 까지(파일의 끝) 
    line = file.readline().decode() # line을 입력받음
    if(line == '') : break  # 입력이 없는 경우(파일의 끝) 반복문 탈출

    lst = line.split(' ')   # line을 ' '을 기준으로 분리하여 lst에 저장
    if lst[2] == 'assistant' :  # 세 번째 원소가 assistant 인 경우
        count[0] += 1           # assistant의 count 증가
        money[0] += eval(lst[3])# assistant의 총 급여 증
        
    elif lst[2] == 'associate' :# 세 번째 원소가 associate 인 경우
        count[1] += 1           # associate의 count 증가
        money[1] += eval(lst[3])# associate의 총 급여 증가
        
    elif lst[2] == 'full' :     # 세 번째 원소가 full 인 경우
        count[2] += 1           # full의 count 증가
        money[2] += eval(lst[3])# full의 총 급여 증가
file.close()

# 각 직급별 총 급여와 평균 출력
print("Assistant\t Total :", format(money[0], ".2f"))
print("\t\t Average :", format(money[0] / count[0], ".2f"), '\n')

print("Associate\t Total :", format(money[1], ".2f"))
print("\t\t Average :", format(money[1] / count[1], ".2f"), '\n')

print("Full\t\t Total :", format(money[2], ".2f"))
print("\t\t Average :", format(money[2] / count[2], ".2f"), '\n')

# 전체 총 급여와 평균 출력
print("All\t\t Total :", format(sum(money), ".2f"))
print("\t\t Average :", format(sum(money) / sum(count), ".2f"), '\n')
