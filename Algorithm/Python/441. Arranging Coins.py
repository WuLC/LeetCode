# -*- coding: utf-8 -*-
# @Author: WuLC
# @Date:   2016-11-01 23:44:30
# @Last modified by:   WuLC
# @Last Modified time: 2016-11-02 00:07:51
# @Email: liangchaowu5@gmail.com


# pay attention to overflow,thus set the right to be sqrt(2n) 
class Solution(object):
    def arrangeCoins(self, n):
        """
        :type n: int
        :rtype: int
        """
        left, right = 1, 2*int(math.sqrt(n)+1)#int(math.sqrt(2)*math.sqrt(n))+1
        while left < right:
            mid = left + ((right - left)>>1)
            total = ((1 + mid)*mid)>>1
            if total == n:
                return mid
            elif total > n:
                right = mid - 1
            else:
                left = mid + 1
        return left if ((1+left)*left)>>1 <= n else left-1
        
            
        