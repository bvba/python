import random

player = eval(input("가위(0), 바위(1), 보(2) : "))
com = random.randint(0, 2)

print("컴퓨터는 ", end="")
if com == 0:
    print("가위", end="")
elif com == 1:
    print("바위", end="")
else:
    print("보", end="")
print("입니다. 당신은 ", end="")

if player == 0:
    print("가위", end="")
elif player == 1:
    print("바위", end="")
else:
    print("보", end="")
print("입니다. ", end="")
# 컴퓨터와 플레이어의 가위바위보 상태를 출력

if player - com == 1 or player - com == -2:
    # 차이가 1 이거나 -2 인경우 플레이어의 승리
    print("당신이 이겼습니다.")
elif player == com:
    # 같은경우 무승부
    print("비겼습니니다.")
else:
    # 이외의 경우 패배 출력
    print("당신이 졌습니다.")
