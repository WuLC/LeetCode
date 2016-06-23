# -*- coding: utf-8 -*-
# @Author: WuLC
# @Date:   2016-06-23 22:00:39
# @Last modified by:   WuLC
# @Last Modified time: 2016-06-23 22:00:53
# @Email: liangchaowu5@gmail.com

class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dp1,dp2 = nums[:], nums[1:]
        dp1.insert(0, 0)
        dp2.insert(0, 0)
        for i in xrange(3, len(dp1)):
            if i != len(dp1)-1:
                dp2[i] = max(dp2[i]+dp2[i-2], dp2[i]+dp2[i-3])
            dp1[i] = max(dp1[i]+dp1[i-2], dp1[i]+dp1[i-3])
        if dp2[-1] > 0:
            dp1[-1] = dp2[-1]
        max_sum = dp1[0]
        for i in xrange(1, len(dp1)):
            if dp1[i] > max_sum:
                max_sum = dp1[i]
        return max_sum