import math

a, b, c = eval(input("a, b, c�� �Է��ϼ��� : "))
discriminant = b ** 2 - 4 * a * c
# �Ǻ����� ���Ͽ� ����

if discriminant > 0:    # �Ǻ����� ����� ��� �ΰ��� ���� ���Ͽ� ���
    ans1 = (-b - math.sqrt(discriminant)) / (2 * a)
    ans2 = (-b + math.sqrt(discriminant)) / (2 * a)
    print("�Ǳ���", round(ans1, 3), "�̰�", round(ans2, 3), "�Դϴ�.")
elif discriminant == 0: # �Ǻ����� 0 �ΰ�� �߱��� ���
    ans1 = -b / (2 * a)
    print("�Ǳ���", round(ans1, 3), "�Դϴ�.")
else :                  # �Ǻ����� ������ ��� ���� ������ �˷���
    print("�� �������� �Ǳ��� �������� �ʽ��ϴ�.")
