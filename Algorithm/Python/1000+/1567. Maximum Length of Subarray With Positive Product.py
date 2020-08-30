from collections import defaultdict

class Solution(object):
    def getMaxLen(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        sign = lambda x: x and (1, -1)[x < 0] 
        counter = defaultdict(int)
        left, right, result = 0, 0, 0
        n = len(nums)
        while right < len(nums) or left < right:
            if (right < n and sign(nums[right]) == 0) or\
               (right == n and left < right):
                while left < right:
                    if counter[-1]%2 == 0:
                        result = max(right - left, result)
                    counter[sign(nums[left])] -= 1
                    left += 1
                if right < n:
                    left = right = right + 1
                    continue
            if right < n:
                counter[sign(nums[right])] += 1
                if counter[-1]%2 == 0:
                    result = max(right - left + 1, result)
                right += 1
        return result
                    