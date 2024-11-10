class Solution(object):
    def maxIncreasingSubarrays(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        pre_len, curr_len = 1, 1
        result = 1
        for i in range(1, len(nums)):
            if (nums[i] > nums[i-1]):
                curr_len += 1
            else:
                pre_len, curr_len = curr_len, 1
            result = max(result, max(curr_len/2, min(pre_len, curr_len)))
        return result