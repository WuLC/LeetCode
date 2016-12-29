# -*- coding: utf-8 -*-
# @Author: WuLC
# @Date:   2016-12-17 11:35:46
# @Last modified by:   WuLC
# @Last Modified time: 2016-12-29 18:15:57
# @Email: liangchaowu5@gmail.com



# greddy, get wrong answer for some solution ,like
# strs = ["111","1000","1000","1000"], m = 9,  n=3
class Solution(object):
    def findMaxForm(self, strs, m, n):
        """
        :type strs: List[str]
        :type m: int
        :type n: int
        :rtype: int
        """
        def compare(s1, s2):
            if len(s1) != len(s2):
                return len(s1) - len(s2);
            else:
                return cmp(s1,s2)
            
        strs.sort(cmp = compare)
        count = 0
        for s in strs:
            for char in s:
                if char == '0' and m > 0:
                    m -= 1
                elif char == '1' and n > 0:
                    n -= 1
                else:
                    return count
            count += 1
        return count
            


# DP, from higher indices to lower indices
# get right answer, but TLE 
from collections import Counter
class Solution(object):
    def findMaxForm(self, strs, m, n):
        """
        :type strs: List[str]
        :type m: int
        :type n: int
        :rtype: int
        """
        dp = [[0 for i in xrange(n+1)] for j in xrange(m+1)]
        for s in strs:
            count = Counter(s)
            for i in reversed(xrange(m+1)):
                if i < count['0']:
                    break
                for j in reversed(xrange(n+1)):
                    if j < count['1']:
                        break
                    dp[i][j] = max(dp[i-count['0']][j-count['1']]+1, dp[i][j])
        return dp[m][n]
                    
# use self-constructed count function can AC, WTF
class Solution(object):
    def findMaxForm(self, strs, m, n):
        """
        :type strs: List[str]
        :type m: int
        :type n: int
        :rtype: int
        """
        def count(str):
            zero, one = 0, 0
            for char in str:
                if char == '0':
                    zero += 1
                else:
                    one += 1
            return zero, one
            
        dp = [[0 for i in xrange(n+1)] for j in xrange(m+1)]
        for str in strs:
            zeros, ones = count(str)
            for i in reversed(xrange(m+1)):
                if i < zeros:
                    break
                for j in reversed(xrange(n+1)):
                    if j < ones:
                        break
                    dp[i][j] = max(dp[i-zeros][j-ones]+1, dp[i][j])
        return dp[m][n]