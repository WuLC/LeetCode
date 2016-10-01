# -*- coding: utf-8 -*-
# @Author: WuLC
# @Date:   2016-10-01 20:31:59
# @Last modified by:   WuLC
# @Last Modified time: 2016-10-01 21:06:38
# @Email: liangchaowu5@gmail.com

# divide and conquer, merge sort, 
# in terms of main theory, time complexity O(n(logn)^2)
# referer: https://discuss.leetcode.com/topic/33770/short-simple-o-n-log-n


class Solution(object):
    def countRangeSum(self, nums, lower, upper):
        """
        :type nums: List[int]
        :type lower: int
        :type upper: int
        :rtype: int
        """
        prefix_sum = []
        for num in nums:
            if prefix_sum:
                prefix_sum.append(prefix_sum[-1] + num)
            else:
                prefix_sum.append(num)
        def helper(left, right):
            if left > right:
                return 0 
            if left == right:
                return 1 if lower <= prefix_sum[left] <= upper else 0
            mid = left + (right - left)/2
            count = helper(left, mid) + helper(mid+1, right)
            p1, p2 = mid+1, mid+1
            for idx in xrange(left, mid+1):
                while p1 <= right and prefix_sum[p1] - prefix_sum[idx] < lower: p1 += 1
                while p2 <= right and prefix_sum[p2] - prefix_sum[idx] <= upper: p2 += 1
                count += (p2 - p1)
            prefix_sum[left:right+1] = sorted(prefix_sum[left:right+1])
            return count
        return helper(0, len(prefix_sum)-1)
                
            