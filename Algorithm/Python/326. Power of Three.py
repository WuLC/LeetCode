# -*- coding: utf-8 -*-
# @Author: WuLC
# @Date:   2016-08-11 10:33:16
# @Last modified by:   WuLC
# @Last Modified time: 2016-08-11 10:49:53
# @Email: liangchaowu5@gmail.com

# method 1, loop
class Solution(object):
    def isPowerOfThree(self, n):
        """
        :type n: int
        :rtype: bool
        """
        while n > 1:
            if n%3 == 0:
                n /=3
            else:
                return False
        return n == 1
        

# method 2. recursive
class Solution(object):
    def isPowerOfThree(self, n):
        """
        :type n: int
        :rtype: bool
        """
        return n>0 and ( n==1 or (n%3==0 and self.isPowerOfThree(n/3)) )
        

# method 3, no recursive or loop from the code
class Solution(object):
    def isPowerOfThree(self, n):
        """
        :type n: int
        :rtype: bool
        """
        return n>0 and 1162261467%n==0 # 1162261467 is the max number of power of 3 as an int