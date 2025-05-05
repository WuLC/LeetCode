class Solution(object):
    def returnToBoundaryCount(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        result, curr = 0, 0
        for i in range(len(nums)):
            curr += nums[i]
            if curr == 0:
                result += 1
        return result