# -*- coding: utf-8 -*-
# Created on Mon Apr 23 2018 15:35:57
# Author: WuLC
# EMail: liangchaowu5@gmail.com

# stupid dp, TLE
from collections import defaultdict
class Solution(object):
    def numFactoredBinaryTrees(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        dp = defaultdict(int)
        A.sort()
        result = 0
        for num in A:
            dp[num] = 1
            for sub in range(1, int(num**0.5)+1):
                if num % sub == 0:
                    dp[num] += dp[sub]*dp[num/sub] if sub == num/sub else dp[sub]*dp[num/sub]*2
            dp[num] %= 10 ** 9 + 7
            result += dp[num]
        return result


# faster dp, AC
from collections import defaultdict
class Solution(object):
    def numFactoredBinaryTrees(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        dp = defaultdict(int)
        A.sort()
        result = 0
        for i in xrange(len(A)):
            dp[A[i]] = 1
            for j in xrange(i):
                if A[i] % A[j] == 0:
                    dp[A[i]] += dp[A[j]]*dp[A[i]/A[j]]
            dp[A[i]] %= 10 ** 9 + 7
            result += dp[A[i]]
            result %= 10 ** 9 + 7
        return result