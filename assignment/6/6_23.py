def convertMillis(millis) :
    h = int(millis / 1000 / 60 / 60)
    # 밀리 초에서 시간이 얼마인지 구하여 h에 저장
    millis %= (1000 * 60 * 60)
    # 밀리 초에서 저장한 시간만큼 빼준다
    
    m = int(millis / 1000 / 60)
    # 밀리 초에서 분이 얼마인지 구하여 m에 저장
    millis %= (1000 * 60)
    # 밀리 초에서 저장한 분만큼 빼준다.

    s = int(millis / 1000)
    # 밀리 초를 초로 변환하여 s로 저장
    return str(h) + ":" + str(m) + ":" + str(s)
    # 시간, 분, 초를 문자열로 바꾸어 형식에 맞게 반환

millis = eval(input("밀리초를 입력하세요 : "))
print(convertMillis(millis))
# 입력받은 밀리 초 값을 시, 분, 초로 변환한 값을 출력
