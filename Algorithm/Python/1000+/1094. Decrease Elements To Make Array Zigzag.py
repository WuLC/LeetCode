class Solution(object):
    def movesToMakeZigzag(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        odd, even = 0, 0 
        for i in xrange(0, len(nums)):
            l_decrease, r_decrease = 0, 0
            if i != len(nums) - 1:
                if (i&1) == 0:
                    r_decrease = max(0, nums[i] - nums[i+1] + 1)
                else:
                    r_decrease = max(0, nums[i] - nums[i+1] + 1)
            if i != 0:
                if (i&1) == 0:
                    l_decrease = max(0, nums[i] - nums[i-1] + 1)
                else:
                    l_decrease = max(0, nums[i] - nums[i-1] + 1)
            if (i&1) == 0:
                odd += max(l_decrease, r_decrease)
            else:
                even += max(l_decrease, r_decrease)
        return min(odd, even)