# -*- coding: utf-8 -*-
# Created on Wed Jan 30 2019 0:21:10
# Author: WuLC
# EMail: liangchaowu5@gmail.com

# dp, O(n) time, O(n) space
class Solution(object):
    def mincostTickets(self, days, costs):
        """
        :type days: List[int]
        :type costs: List[int]
        :rtype: int
        """
        dp = [0]
        for i in xrange(len(days)):
            dp.append(dp[i] + costs[0])
            for j in xrange(i-1, max(-1, i-31), -1):
                if days[j] > days[i] - 7:
                    dp[i+1] = min(dp[i+1], dp[j] + costs[1])
                if days[j] > days[i] - 30:
                    dp[i+1] = min(dp[i+1], dp[j] + costs[2])
                if days[j] < days[i] - 30:
                    break
        return dp[-1]


    #def binary_search(days, left, right):
