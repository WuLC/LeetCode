# -*- coding: utf-8 -*-
# @Author: LC
# @Date:   2017-06-18 10:45:52
# @Last modified by:   LC
# @Last Modified time: 2017-06-18 10:47:59
# @Email: liangchaowu5@gmail.com

# get digit one by one(from 9 to 1)
# then sort and join, and check if it is in the range of integer
class Solution(object):
    def smallestFactorization(self, a):
        """
        :type a: int
        :rtype: int
        """
        if a == 1:
            return a
        digits = []
        while a != 1:
            i = 9
            while i > 1:
                if a % i == 0:
                    digits.append(str(i))
                    a /= i
                    break
                i -= 1
            if i == 1:
                break
        if a != 1:
            return 0
        num  = int(''.join(sorted(digits)))
        return 0 if num > pow(2,31) else num
            
        
                
            
                
        