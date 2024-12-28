class Solution(object):
    def constructTransformedArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        return [nums[(i+nums[i])%len(nums)] for i in range(len(nums))]