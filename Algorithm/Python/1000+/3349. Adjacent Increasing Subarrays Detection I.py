class Solution(object):
    def hasIncreasingSubarrays(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        def is_increase(idx):
            for i in range(idx+1, idx+k):
                if nums[i] <= nums[i-1]:
                    return False
            return True
            
        for i in range(len(nums)-2*k+1):
            if is_increase(i) and is_increase(i+k):
                return True
        return False

        