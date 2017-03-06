def multiplyMatrix(mat1, mat2, size) :
    mat3 = [[0 for j in range(size)] for i in range(size)]

    # 반복분을 통해 행렬의 곱 연산을 수행한다
    for i in range(size) :           # 행렬1의 행, 행렬3의 행
        for j in range(size) :       # 행렬1의 열, 행렬2의 행
            for k in range(size) :   # 행렬2의 열, 행렬3의 열
                mat3[i][k] += mat1[i][j] * mat2[j][k]
                # 행렬의 곱 연산 결과를 mat3에 저장
    mat3 = [[round(mat3[i][j],1) for j in range(size)] for i in range(size)]
    return mat3
    

mat1 = [eval(x) for x in input("행렬1을 입력하세요 : ").split(' ')]
mat2 = [eval(x) for x in input("행렬2를 입력하세요 : ").split(' ')]

if len(mat1) != len(mat2) :
    # 행렬의 사이즈가 다른 경우 연산 불가능 출력
    print("행렬의 곱 연산 불가능")
else :
    row = col = int(len(mat1) ** 0.5)
    mat1 = [[mat1[(i * 3) + j] for j in range(col)] for i in range(row)]
    mat2 = [[mat2[(i * 3) + j] for j in range(col)] for i in range(row)]
    mat3 = multiplyMatrix(mat1, mat2, row)

    # 행렬의 곱 연산 결과를 양식에 맞게 출력
    for i in range(row) :   # 행렬의 행
        for j in range(3) : # 행렬 1, 2, 3
            for k in range(col) :   # 행렬의 열
                if j == 0 :     print(format(mat1[i][k], "6.1f"), end = '')
                elif j == 1 :   print(format(mat2[i][k], "6.1f"), end = '')
                elif j == 2 :   print(format(mat3[i][k], "6.1f"), end = '')
            if i == int(row / 2) :
                if j == 0 : print('\t*\t', end = '')
                if j == 1 : print('\t=\t', end = '')
            else : print('\t \t', end = '')
        print()
