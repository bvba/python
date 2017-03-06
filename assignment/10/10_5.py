s = input("10개의 숫자를 입력하세요 : ")
items = s.split()   # 입력된 문자열을 숫자마다 분할하여 저장(문자열로 저장됨)
list1 = [eval(x) for x in items]    # 분할된 숫자(문자열)을 숫자로 변환하여 저장
list2 = []  # 빈 리스트 생성
for x in list1 :
    if x not in list2 :
        # list1의 원소가 list2에 없는 경우에만 list2에 추가
        list2.append(x)

print("중복을 제거한 고유한 숫자 :", list2)
