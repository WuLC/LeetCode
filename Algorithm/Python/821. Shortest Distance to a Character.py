# -*- coding: utf-8 -*-
# Created on Sun Apr 22 2018 23:4:33
# Author: WuLC
# EMail: liangchaowu5@gmail.com


# binary search, time complexity: O(nlogk), n is the length of S, k is the number of C in S
class Solution(object):
    def shortestToChar(self, S, C):
        """
        :type S: str
        :type C: str
        :rtype: List[int]
        """
        idx = []
        for i in xrange(len(S)):
            if S[i] == C:
                idx.append(i)
                
        result = []
        for i in xrange(len(S)):
            if S[i] == C:
                result.append(0)
            else:
                result.append(self.binarySearch(i, idx))
        return result
        
        
    def binarySearch(self, i, idx):
        if i < idx[0]:
            return idx[0] - i
        if i > idx[-1]:
            return i - idx[-1]
        left, right = 0, len(idx) - 1
        while left < right:
            mid = left + ((right-left)>>1)
            if idx[mid] > i:
                right = mid
            else:
                left = mid + 1
        return min(idx[left] - i, i - idx[left-1])
            
        