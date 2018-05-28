# -*- coding: utf-8 -*-
# Created on Thu May 24 2018 10:18:58
# Author: WuLC
# EMail: liangchaowu5@gmail.com

# recursive with cache, TLE
class Solution(object):     
    def new21Game(self, N, K, W):
        """
        :type N: int
        :type K: int
        :type W: int
        :rtype: float
        """
        self.cache = {}
        base = 1.0/W
        def helper(curr, N, K, W):
            if curr > N:
                return 0
            if K <= curr <= N:
                return 1
            if curr not in self.cache:
                prob = 0
                for i in xrange(1, W+1):
                    if curr+i > N:
                        break
                    if curr+i not in self.cache:
                        self.cache[curr+i] = helper(curr+i, N, K, W)
                    prob += base*self.cache[curr+i]
                self.cache[curr] = prob
            return self.cache[curr]
        return helper(0, N, K, W)


# dp, O(n) time, AC
class Solution(object):
    def new21Game(self, N, K, W):
        """
        :type N: int
        :type K: int
        :type W: int
        :rtype: float
        """
        dp = [1]
        curr_sum = 1
        base = 1.0/W
        for i in xrange(1, N+1):
            if i > W:
                curr_sum -= dp[i-W-1]
            dp.append(base*curr_sum)
            if i < K:
                curr_sum += dp[-1]
        return min(1.0, sum(dp[i] for i in xrange(K, N+1)))