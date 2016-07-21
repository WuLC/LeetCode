# -*- coding: utf-8 -*-
# @Author: LC
# @Date:   2016-07-21 08:25:19
# @Last modified by:   WuLC
# @Last Modified time: 2016-07-21 08:25:26
# @Email: liangchaowu5@gmail.com

# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):

class Solution(object):
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        result = [None]
        self.helper(1, n, result)
        return result[0]
        
    def helper(self, left, right, result):
        if left > right:
            return
        mid = (left+right)/2
        if isBadVersion(mid):
            if result[0] == None or result[0] > mid:
                result[0] = mid
            self.helper(left, mid-1, result)
        else:
            self.helper(mid+1, right, result)