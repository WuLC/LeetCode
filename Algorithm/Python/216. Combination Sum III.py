# -*- coding: utf-8 -*-
# @Author: LC
# @Date:   2016-07-06 14:18:31
# @Last modified by:   WuLC
# @Last Modified time: 2016-07-06 14:18:44
# @Email: liangchaowu5@gmail.com

class Solution(object):
    def combinationSum3(self, k, n):
        """
        :type k: int
        :type n: int
        :rtype: List[List[int]]
        """
        result= []
        self.helper(k, n, 0, [], result)
        return result
    
    def helper(self, k, n, last, tmp, result):
        if k == len(tmp):
            if n == sum(tmp):
                result.append(tmp[:])
                return True
            return 
        for i in xrange(last+1, 10):
            tmp.append(i)
            if self.helper(k, n, i, tmp, result):
                tmp.pop()
                return
            tmp.pop()
            
            
                
                
        