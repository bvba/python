from QuadraticEquation import QuadraticEquation
# QuadraticEquation 파일에서 QuadraticEquation 클래스 import

a, b, c = eval(input("a, b, c를 입력하세요 : "))  # 입력값을 받음

q = QuadraticEquation(a, b, c)  # a, b, c로 q1 객체를 생성

dis = q.getDiscriminant()   # q의 판별식 저장

if dis > 0 :    # 판별식이 양수인 경우 두개의 해 출력
    print("Ans1 :", format(q.getRoot1(), ".3f"))
    print("Ans2 :", format(q.getRoot2(), ".3f"))
elif dis == 0 : # 판별식이 0인 경우 중근 출력
    print("Ans :", format(q.getRoot1(), ".3f"))
else :          # 판별식이 음수인 경우 해가 없음을 출력
    print("이 방정식은 해가 없습니다.")
