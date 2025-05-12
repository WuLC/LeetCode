class Solution(object):
    def minSum(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: int
        """
        def get_zeros_and_sum(nums):
            zeros, _sum = 0, 0
            for num in nums:
                if num == 0:
                    zeros += 1
                _sum += num
            return zeros, _sum

        zeros1, sum1 = get_zeros_and_sum(nums1)
        zeros2, sum2 = get_zeros_and_sum(nums2)
        if (zeros1 == 0 and sum1 - sum2 < zeros2) or (zeros2 == 0 and sum2 - sum1 < zeros1):
            return -1
        return max(sum1 + zeros1, sum2 + zeros2)

