# -*- coding: utf-8 -*-
# Created on Fri Dec 08 2017 20:5:43
# Author: WuLC
# EMail: liangchaowu5@gmail.com

# dynamic programming
# transfer the problem to House Robbers: https://leetcode.com/problems/house-robber/description/
class Solution(object):
    def deleteAndEarn(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count = {}
        length = 0
        for num in nums:
            count.setdefault(num, 0)
            count[num] += num
            length = max(num, length)
        points = [0] * (length + 1)
        dp = [0] * (length + 2)
        for k, v in count.items():
            points[k] = v
        result = 0
        for i in range(len(points)):
            if i == 0:
                dp[i+1] = points[i]
            else:
                dp[i+1] = max(dp[i], dp[i-1] + points[i])
            result = max(dp[i+1], result)
        return result
            
            