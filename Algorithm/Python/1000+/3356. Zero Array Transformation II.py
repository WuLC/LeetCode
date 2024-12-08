class Solution(object):
    def minZeroArray(self, nums, queries):
        """
        :type nums: List[int]
        :type queries: List[List[int]]
        :rtype: int
        """
        curr_sum, idx = 0, 0
        count = [0] * (len(nums)+1)
        for i in range(len(nums)):
            curr_sum += count[i]
            while nums[i] > curr_sum and idx < len(queries):
                l, r, v = queries[idx]
                count[l] += v
                count[r+1] -= v
                if l <= i and i <= r:
                    curr_sum += v
                idx += 1
            if idx == len(queries) and curr_sum < nums[i]:
                return -1
        return idx