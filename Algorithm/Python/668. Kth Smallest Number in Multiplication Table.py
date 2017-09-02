# -*- coding: utf-8 -*-
# @Author: WuLC
# @Date:   2017-09-02 23:58:47
# @Last Modified by:   WuLC
# @Last Modified time: 2017-09-02 23:59:00

# binary search
class Solution(object):
    def findKthNumber(self, m, n, k):
        """
        :type m: int
        :type n: int
        :type k: int
        :rtype: int
        """
        left, right = 1, m * n + 1
        while left < right:
            mid = left + ((right - left)>>1)
            c = self.count(m, n, mid)
            if c >= k:
                right = mid
            else:
                left = mid + 1
        return right
    
    def count(self, m, n, num):
        return sum([min(num/i, n) for i in xrange(1, m+1)])
            
        
        
        