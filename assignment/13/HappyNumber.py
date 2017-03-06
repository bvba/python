class Solution:
    # @param {int} n an integer
    # @param {set} sett 나왔던 숫자를 저장하는 set
    # @return {boolean} true if this is a happy number or false
    def isHappy(self, n, sett = set()):
        summ = 0    # 각 자리 숫자의 제곱의 합을 저장
        for i in range(len(str(n))) :
            summ += int(str(n)[i]) ** 2
            # 각 자리 숫자의 제곱을 더함
        if summ == 1 : return True  # 더한 결과가 1인 경우 True 반환
        if summ in sett : return False
        # 더한 결과가 sett에 있다면 무한 반복이므로 False 반환

        sett.add(summ)  # 이외의 경우 결과를 sett에 추가하고
        return self.isHappy(summ, sett) # 위의 과정을 반복한다

n = eval(input("Input Number : "))
s = Solution()
print(s.isHappy(n))
