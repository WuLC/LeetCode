# -*- coding: utf-8 -*-
# @Author: WuLC
# @Date:   2017-03-13 11:55:59
# @Last Modified by:   WuLC
# @Last Modified time: 2017-03-13 11:56:15


# two pointers
class Solution(object):
    def reverseStr(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        chars = [c for c in s]
        idx = 0
        while idx < len(s):
            left, right = idx, min(idx + k-1, len(s)-1)
            while left < right:
                chars[left] , chars[right] = chars[right], chars[left]
                left += 1
                right -= 1
            idx += 2*k
        return ''.join(chars)