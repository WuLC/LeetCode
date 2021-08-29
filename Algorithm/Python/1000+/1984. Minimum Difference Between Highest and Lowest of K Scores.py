class Solution(object):
    def minimumDifference(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        if len(nums) == 0:
            return 0
        nums.sort()
        result = nums[-1] - nums[0]
        for i in range(len(nums) - k + 1):
            result  = min(result, nums[i+k-1] - nums[i])
        return result