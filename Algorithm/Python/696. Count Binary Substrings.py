# -*- coding: utf-8 -*-
# @Author: WuLC
# @Date:   2017-10-18 23:34:40
# @Last Modified by:   WuLC
# @Last Modified time: 2017-10-19 17:23:37

# time complexity O(n^2), TLE
class Solution(object):
    def countBinarySubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        count = 0
        for i in xrange(len(s)):
            length = 1
            idx = i
            while idx + 1 < len(s) and s[idx] == s[idx + 1]:
                length += 1
                idx += 1
            if idx + 1 != len(s):
                idx += 1
                length -= 1
            while idx + 1 < len(s) and s[idx] == s[idx + 1] and length != 0:
                length -= 1
                idx += 1
            if length == 0:
                count += 1
        return count


# count the length of continuous number subsequent
# then take the min value of the neighbor length
# time complexity, O(n)
class Solution(object):
    def countBinarySubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        lengths = []
        idx, count = 1, 1
        while idx < len(s):
            if s[idx] == s[idx - 1]:
                count += 1
            else:
                lengths.append(count)
                count = 1
            idx += 1
        lengths.append(count)
        
        result = 0
        for i in xrange(len(lengths) - 1):
            result += min(lengths[i], lengths[i+1])
        return result
