class Solution(object):
    def countValidSelections(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        curr_sum, total_sum = [0]*(n+1), 0
        for i in range(n):
            total_sum += nums[i]
            curr_sum[i+1] = curr_sum[i] + nums[i]

        result = 0
        for i in range(n):
            if nums[i] == 0: 
                if curr_sum[i+1] == total_sum - curr_sum[i+1]:
                    result += 2
                elif abs(total_sum - 2*curr_sum[i+1]) == 1:
                    result += 1
        return result