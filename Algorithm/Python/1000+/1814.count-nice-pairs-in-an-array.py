#
# @lc app=leetcode id=1814 lang=python3
#
# [1814] Count Nice Pairs in an Array
#

# @lc code=start

from collections import Counter
class Solution:
    def countNicePairs(self, nums: List[int]) -> int:
        counter = Counter(nums[i] - self.rev(nums[i]) for i in range(len(nums)))
        return sum(int((v-1)*v/2) for _, v in counter.items()) % (10**9+7)

    
    def rev(self, num: int) -> int:
        return int(str(num)[::-1])


# TLE using brute-force
class Solution:
    def countNicePairs(self, nums: List[int]) -> int:
        result = 0
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if self.isNice(nums[i], nums[j]):
                    result += 1
        return result % (10**9 + 7)
    
    def isNice(self, num1: int, num2: int) -> bool:
        def rev(num: int) -> int:
            result = 0
            while num > 0:
                result = result * 10 + (num % 10)
                num = int(num/10)
            return result
        return num1 + rev(num2) == rev(num1) + num2
        
# @lc code=end

