class Solution:
    """
    @param A : An integer array
    @return : Two integer
    """
    def singleNumberIII(self, A):
        dic = {}    # 숫자와 각 숫자의 빈도수를 저장하는 dict
        for i in range(len(A)) :
            if A[i] not in dic :    # dic에 등록되지 않은 경우
                dic[A[i]] = 1       # 해당 숫자를 dic에 등록
            else :                  # 등록된 경우
                dic[A[i]] += 1      # 값(빈도수) + 1
        ans = []    # 1번 출현한 숫자를 저장하는 리스트(정답을 저장)
        for key in dic :
            if dic[key] == 1 :      # 값(빈도수)가 1인 숫자를
                ans.append(key)     # ans 리스트에 추가한다
        return ans

s = Solution()
lst = [eval(x) for x in (input("Input Numbers : ")).split()]
print(s.singleNumberIII(lst))
