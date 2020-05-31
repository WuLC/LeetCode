class Solution(object):
    def maxArea(self, h, w, horizontalCuts, verticalCuts):
        """
        :type h: int
        :type w: int
        :type horizontalCuts: List[int]
        :type verticalCuts: List[int]
        :rtype: int
        """
        def max_len(nums):
            result = 0
            for i, num in enumerate(nums):
                result = max(result, num - nums[i-1])
            return result
        return (max_len([0] + sorted(horizontalCuts) + [h]) * max_len([0] + sorted(verticalCuts) + [w])) % (10**9+7)