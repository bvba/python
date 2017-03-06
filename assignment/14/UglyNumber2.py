class Solution:
    """
    @param {int} n an integer.
    @return {int} the nth prime number as description.
    """
    def nthUglyNumber(self, n):
        ugly = [1]
        # 기초가 되는 ugly num
        # n번째 ugly num에 (2 or 3 or 5)를 곱한 수는 ugly num임을 활용하여
        # ugly[n] * (2 or 3 or 5)의 결과를 중복 없이 ugly에 추가하고
        # 마지막에 오름차순으로 정렬하여 n번째 ugly num을 구한다
        
        sett = set(ugly)    # ugly num을 추가할 때 중복 검사를 하기 위한 set
        mul = [2, 3, 5]     # ugly[n] * (2 or 3 or 5)를 반복문에서 수행하기 위한 리스트
        for i in range(n * 3) :
        # ugly[n] * (2 or 3 or 5)가 순서대로 n + 1, n + 2, n + 3번째 ugly num이 아니고,
        # 중복되는 경우도 있으므로 구하려는 범위의 3배까지 반복문을 실행한다
            for j in range(3) : # ugly[n] * (2 or 3 or 5)를 수행
                if ugly[i] * mul[j] not in sett :   # 중복이 아닌 경우
                    ugly.append(ugly[i] * mul[j])   # ugly num을 추가
                    sett.add(ugly[i] * mul[j])      # set에도 추가
        ugly.sort() # ugly를 오름차순으로 정렬
        return ugly[n - 1]  # n번째 ugly num 반환

s = Solution()
n = eval(input("Input Number : "))
print(str(n) + "th Ugly Number is " + str(s.nthUglyNumber(n)) + ".")
