class Solution:
    # @param n: an integer
    # @return an integer f(n)
    def fibonacci(self, n):
        ans = [0, 0, 1] # 피보나치 수열의 초기값 설정
        for i in range(3, n + 1) :
            ans.append(ans[i - 1] + ans[i - 2])
            # 피보나치 수열 설정
        return ans[n]   # 피보나치 수열의 n번째 원소 반환
s = Solution()
n = eval(input("Input Number : "))
print(n, "번째 피보나치 수는", s.fibonacci(n), "입니다.")
