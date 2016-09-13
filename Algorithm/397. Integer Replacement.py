# -*- coding: utf-8 -*-
# @Author: WuLC
# @Date:   2016-09-13 19:56:38
# @Last modified by:   WuLC
# @Last Modified time: 2016-09-13 20:01:50
# @Email: liangchaowu5@gmail.com


# recursive, AC
class Solution(object):
    dp = {}
    def integerReplacement(self, n):
        
        """
        :type n: int
        :rtype: int
        """
        if n == 1:
            return 0
        if n in Solution.dp:
            return Solution.dp[n]
        count = 0
        if n%2 == 0:
            count = self.integerReplacement(n/2) + 1
        else:
            count = min(self.integerReplacement(n + 1), self.integerReplacement(n - 1)) + 1
        Solution.dp[n] = count
        return count
            
        
         
        
        