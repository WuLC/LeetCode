# -*- coding: utf-8 -*-
# @Author: LC
# @Date:   2016-09-14 21:25:04
# @Last modified by:   WuLC
# @Last Modified time: 2016-09-14 21:34:14
# @Email: liangchaowu5@gmail.com

# TLE
class Solution(object):
    def lexicalOrder(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        result = []
        self.helper('', n, result)
        return result
        
    def helper(self, tmp, n, result):
        for i in xrange(10):
            if len(tmp) == 0 and i == 0:
                continue
            if int(tmp + str(i)) <= n:
                result.append(int(tmp+ str(i)))
                self.helper(tmp+str(i), n, result)
            else:
                return 
                

# the same logic as the above solution, but deal with integer instead of  string
# AC
class Solution(object):
    def lexicalOrder(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        result = []
        self.helper(0, n, result)
        return result
        
    def helper(self, tmp, n, result):
        for i in xrange(10):
            if tmp == 0 and i == 0:
                continue
            if tmp*10+i <= n:
                result.append(tmp * 10+ i)
                self.helper(tmp * 10 + i, n, result)
            else:
                return 