# -*- coding: utf-8 -*-
# @Author: WuLC
# @Date:   2016-05-17 10:03:19
# @Last modified by:   WuLC
# @Last Modified time: 2016-05-17 10:03:44
# @Email: liangchaowu5@gmail.com

# backtracking
class Solution(object):
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        result = []
        tmp = []
        self.helper(n+1,k,1,result,tmp)
        return result
        
    def helper(self,n,k,begin,result,tmp):
        if len(tmp) == k:
            result.append(tmp[:])
        for i in xrange(begin,n):
            tmp.append(i)
            self.helper(n,k,i+1,result,tmp)
            tmp.remove(i)
        