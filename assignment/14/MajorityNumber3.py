class Solution:
    """
    @param nums: A list of integers
    @param k: As described
    @return: The majority number
    """
    def majorityNumber(self, nums, k):
        dic = {}    # num 리스트에 있는 숫자와 빈도수를 저장하는 dict
        for i in range(len(nums)) :
            if nums[i] not in dic : # dic에 들어있지 않은 경우
                dic[nums[i]] = 1    # dic에 해당 숫자를 추가
            else :                  # 들어있는 경우 값(빈도수) + 1
                dic[nums[i]] += 1
        major = None    # 가장 많이 나온 숫자
        for key in dic :
            if major == None :  # 초기화되지 않은 경우
                if dic[key] >= len(nums) / k :
                # 어떤 숫자가 전체의 1/k 보다 많이 나온 경우
                    major = key # 그 수를 major로 설정
            else :  # major가 설정된 경우                
                if dic[key] > dic[major] :
                # major보다 많이 나온 숫자가 있다면 major 재설정
                # (==가장 많이 나온 숫자를 major로 설정)
                    major = key
        return major    # 해당하는 숫자가 없다면 반환값은 None이다

s = Solution()
lst = [eval(x) for x in (input("Input Numbers : ")).split()]
k = eval(input("Input k for 1/k : "))
print(s.majorityNumber(lst, k))
