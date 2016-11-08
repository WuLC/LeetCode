# -*- coding: utf-8 -*-
# @Author: WuLC
# @Date:   2016-11-08 19:58:20
# @Last modified by:   WuLC
# @Last Modified time: 2016-11-08 20:09:02
# @Email: liangchaowu5@gmail.com


# binary search and greedy
# referer: https://discuss.leetcode.com/topic/61324/clear-explanation-8ms-binary-search-java
# the range of the largest sum is between max(nums) and sum(nums)
class Solution(object):
    def splitArray(self, nums, m):
        """
        :type nums: List[int]
        :type m: int
        :rtype: int
        """
        if len(nums) == 0:
            return 0
        left, right = max(nums), sum(nums)
        while left<right:
            count, tmp = 1, 0
            # find the number of times to split when the largest sum is mid, compare it with m and adjust left or right
            mid = left + ((right-left)>>1) 
            for i in xrange(len(nums)):
                if tmp + nums[i] > mid:
                    count += 1
                    tmp = nums[i]
                else:
                    tmp += nums[i]
            if count == m:
                right = mid
            elif count > m:
                left = mid + 1
            else:
                right = mid - 1
        return left
            