class Solution:
    """
    @param A : A string includes Upper Case letters
    @param B : A string includes Upper Case letters
    @return :  if string A contains all of the characters in B return True else return False
    """
    def compareStrings(self, A, B):
        dicA = {} # A문자열의 문자와 각 문자의 빈도수를 저장하는 dict
        for i in range(len(A)) :    # A 문자열의 모든 문자를 dicA에 추가 or 값 + 1
            if A[i] not in dicA :   # 처음 나온 문자인 경우 dicA에 추가
                dicA[A[i]] = 1
            else :                  # 나온 적이 있는 문자인 경우 값 + 1
                dicA[A[i]] += 1
                
        for i in range(len(B)) :    # B 문자열의 모든 문자가 dicA에 있는지 검사
            if B[i] not in dicA :   # 들어있지 않은 경우 False 반환
                return False
            elif dicA[B[i]] == 0 :  # B에 더 많이 들어있는 경우에도 False 반환
                return False
            else :
            # A, B 모두에 들어있는 경우 dicA에서 빈도수를 -1해준다
            # B에 더 많이 들어있는 경우, dicA의 값이 0이 되는 시점이 생긴다(elif문에서 처리됨)
                dicA[B[i]] -= 1
        return True # 검사를 성공적으로 마친 경우 True 반환

s = Solution()
str1 = input("Input String 1 : ")
str2 = input("Input String 2 : ")
print(s.compareStrings(str1, str2))
