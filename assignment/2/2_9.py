tOutside = eval(input("화씨 -58도와 41도 사이의 온도를 입력하세요 : "))
vWind = eval(input("풍속을 시간당 마일 단위로 입력하세요 : "))

tSensibleTemperature = 35.74 + 0.6215 * tOutside - 35.75 * (vWind ** 0.16) + 0.4275 * tOutside * (vWind ** 0.16)
# tSensibleTemperature 수식을 이용하여 계산

tSensibleTemperature = round(tSensibleTemperature, 5)

print("체감온도는", tSensibleTemperature, "입니다.")
