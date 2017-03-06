import random

def roll() :
    return random.randint(1, 6), random.randint(1, 6)

def printRoll(num1, num2) :
    print("주사위", num1, "+", num2, "=", num1 + num2, "이/가 나왔습니다.")

def craps() :
    first = roll()
    firstSum = sum(first)
    printRoll(first[0], first[1])
    
    if firstSum in [7, 11] :
        print("당신이 이겼습니다.")
    elif firstSum in [2, 3, 12] :
        print("당신이 졌습니다.")
    else :
        print(firstSum, "점 입니다.")
        second = roll()
        secondSum = sum(second)
        while not(secondSum in [7, firstSum]) :
            second = roll()
            secondSum = sum(second)
        if secondSum == 7 :
            printRoll(second[0], second[1])
            print("당신이 졌습니다.")
        elif secondSum == firstSum :
            printRoll(second[0], second[1])
            print("당신이 이겼습니다.")
        
craps()
