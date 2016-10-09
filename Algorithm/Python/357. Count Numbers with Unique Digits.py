# -*- coding: utf-8 -*-
# @Author: WuLC
# @Date:   2016-07-20 20:45:22
# @Last modified by:   WuLC
# @Last Modified time: 2016-07-20 21:03:09
# @Email: liangchaowu5@gmail.com


# backtracking, TLE
class Solution(object):
    def countNumbersWithUniqueDigits(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n==0: return 1
        result, visited = [0], set()
        for i in xrange(1, n+1):
            self.helper(0, i, visited, result)
        return result[0]
        
    def helper(self, count, n, visited, result):
        if count == n:
            result[0] += 1
            return
        for i in xrange(10):
            if i==0 and count == 0 and n!=1:
                continue
            if i not in visited:
                visited.add(i)
                self.helper(count+1, n, visited, result)
                visited.remove(i)


# DP and permutation, AC
class Solution(object):
    def countNumbersWithUniqueDigits(self, n):
        """
        :type n: int
        :rtype: int
        """
        dp = [0 for i in xrange(n+1)]
        for i in xrange(n+1):
            if i==0:
                dp[i] = 1
            elif i==1:
                dp[i] = 9
            else:
                dp[i]= dp[i-1]*(11-i)
        return sum(dp)
                
            
        