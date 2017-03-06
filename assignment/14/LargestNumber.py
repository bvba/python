class Solution:	
    #@param num: A list of non negative integers
    #@return: A string
    def largestNumber(self, num):
        ans = ""    # 정답을 저장하는 문자열
        back = [[] for i in range(10)]
        # 10 이상인 임의의 숫자 *?? 에서 ??를 저장하는 리스트(123 -> 23저장)

        numCnt = [[0, 0] for i in range(10)]
        # 해당 숫자로 시작하는 숫자의 개수를 저장하는 2차원 list
        # 10 미만인 숫자의 개수는 리스트의 0번째 인덱스에 저장한다
        # 10 이상인 숫자의 개수는 리스트의 1번째 인덱스에 저장한다
        # if num < 10 :     numCnt[num][0] += 1
        # if 10 <= num :    numCnt[num의 맨 앞 숫자][1] += 1
        
        for i in range(len(num)) :  # n으로 시작하는 숫자가 몇개인지 count
            if num[i] < 10 :    numCnt[num[i]][0] += 1
            # 숫자가 10 미만일 경우 [해당 숫자의] [0번째 인덱스] + 1
            else :
            # 숫자가 10 이상일 경우 [맨 앞 숫자에 해당하는 숫자의] [1번째 인덱스] + 1
            # 맨 앞 숫자를 제외한 뒷부분의 숫자를 back 리스트에 append
                numCnt[eval(str(num[i])[0])][1] += 1
                back[eval(str(num[i])[0])].append(eval(str(num[i])[1:]))
        
        for i in range(10) :    back[i].sort(reverse = True)
        # 뒷부분의 숫자를 저장해놓은 back 리스트를 내림차순으로 정렬

        for n in range(9, -1, -1) :                 # 9부터 0까지
            while numCnt[n][0] or numCnt[n][1] :    # n으로 시작하는 숫자가 있는 경우
                if numCnt[n][1] :   # n으로 시작하는 10이상의 숫자가 있는 경우
                    if n < back[n][0] or numCnt[n][0] == 0 :
                    # 뒷부분이 n보다 큰 수로 시작하는 경우
                    # or 10보다 작은 n으로 시작하는 수가 없는 경우
                        ans += (str(n) + str(back[n].pop(0)))
                        # ans에 (n + 숫자의 뒷부분) == (num)을 추가
                        numCnt[n][1] -= 1   # 사용한 숫자의 개수 - 1
                        continue            # 루프 재시작
                if numCnt[n][0] :
                # n으로 시작하는 10이상의 수가 없는 경우 이 조건문을 수행한다
                # n으로 시작하는 10미만의 수가 있는 경우
                    ans += str(n)       # ans에 n추가
                    numCnt[n][0] -= 1   # 사용한 숫자의 개수 - 1
                if ans == "00" : ans = '0'  # ans가 00인 경우 0으로 고쳐준다
        return ans # 정답 문자열 반환

s = Solution()
numList = [eval(x) for x in str(input("Input Numbers : ")).split()]
print(s.largestNumber(numList))
