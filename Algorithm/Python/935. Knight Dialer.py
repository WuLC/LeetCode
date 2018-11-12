# -*- coding: utf-8 -*-
# Created on Sat Nov 10 2018 12:20:44
# Author: WuLC
# EMail: liangchaowu5@gmail.com


# 2-d dp, O(n) time, O(n) space
class Solution(object):
    def knightDialer(self, N):
        """
        :type N: int
        :rtype: int
        """
        pre, curr = [0] * 10, [1] * 10
        mod = 10 ** 9 + 7
        while N > 1:
            pre = curr
            curr = [0] * 10
            curr[0] = (pre[4] + pre[6]) % mod
            curr[1] = (pre[6] + pre[8]) % mod
            curr[2] = (pre[7] + pre[9]) % mod
            curr[3] = (pre[4] + pre[8]) % mod
            curr[4] = (pre[0] + pre[3] + pre[9]) % mod
            curr[6] = (pre[0] + pre[1] + pre[7]) % mod
            curr[7] = (pre[2] + pre[6]) % mod
            curr[8] = (pre[1] + pre[3]) % mod
            curr[9] = (pre[2] + pre[4]) % mod
            N-= 1
        return sum(curr) % mod

# more elegant
class Solution:
    def knightDialer(self, N):
        """
        :type N: int
        :rtype: int
        """ 
        mapping = {1:[6, 8], 2:[7, 9], 3:[4, 8], 4:[0, 3, 9], 5:[], 6:[0, 1, 7], 7:[2, 6], 8:[1, 3], 9:[2, 4], 0:[4, 6]}
        
        pre = [1] * 10
        for _ in range(N - 1):
            curr = [0] * 10
            for i in range(10):
                for j in mapping[i]:
                    curr[j] += pre[i]
            pre = curr
        
        return sum(pre) % (10 ** 9 + 7)