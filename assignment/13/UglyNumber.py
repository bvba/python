class Solution:
    # @param {int} num an integer
    # @return {boolean} true if num is an ugly number or false
    def isUgly(self, num):
        while num % 2 == 0 :    # 약수 중 2 모두 제거
            num //= 2
        while num % 3 == 0 :    # 약수 중 3 모두 제거
            num //= 3
        while num % 5 == 0 :    # 약수 중 5 모두 제거
            num //= 5
        # 2, 3, 5 이외의 약수가 없다면 num 은 1이 된다
        # num이 1이 아닌 경우 ugly number가 아니다
        if num == 1 : return True
        else : return False

n = eval(input("Input Number : "))
s = Solution()
print(s.isUgly(n))
