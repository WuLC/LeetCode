# -*- coding: utf-8 -*-
# Created on Thu Oct 25 2018 8:45:2
# Author: WuLC
# EMail: liangchaowu5@gmail.com

# O(n) time, O(1) space
# at each position, flip all 1s on its left and 0s on its right
class Solution(object):
    def minFlipsMonoIncr(self, S):
        """
        :type S: str
        :rtype: int
        """
        left, right = 0, 0
        for c in S:
          if c == '0':
            right += 1
        
        result = right
        for c in S:
          if c == '1':
            left += 1
          else:
            right -= 1
          result = min(left + right, result)  
        return result