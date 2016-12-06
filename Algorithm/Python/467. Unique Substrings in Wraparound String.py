# -*- coding: utf-8 -*-
# @Author: LC
# @Date:   2016-12-06 15:12:56
# @Last modified by:   WuLC
# @Last Modified time: 2016-12-06 15:20:59
# @Email: liangchaowu5@gmail.com

# time complexity: O(n)
# find the longest continuous substrings that end with different characters in p
# thus the length of the longest continous substring that ends with certain character 
# is the number of the substrings in p that ends with certain character 
# for example: 'abcbc', the longest continous substring the ends with 'c' is 'abc', thus the number of substrings that in s is 3(abc,bc,c)
class Solution(object):
    def findSubstringInWraproundString(self, p):
        """
        :type p: str
        :rtype: int
        """
        count = [0 for i in xrange(26)]
        left, right = 0, 0
        while right < len(p):
            idx = ord(p[right])-97
            if right-1 >=0 and ord(p[right]) - ord(p[right-1]) not in {1, -25}:
                left = right
            count[idx] = max(count[idx], right-left+1) 
            right += 1
        return sum(count)