# -*- coding: utf-8 -*-
# @Author: LC
# @Date:   2016-01-24 11:02:34
# @Last modified by:   WuLC
# @Last Modified time: 2016-10-11 21:34:35
# @Email: liangchaowu5@gmail.com


# Two pointers, Hash table
# use hash table to store the max index of a character
# use two pointers to represent the current unrepeating substring
# when metting a character in the hash table, calculate the current length and update the index of the character

class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        result = 0
        left, right = 0, 0
        indices = {}
        while right < len(s):
            if s[right] in indices and indices[s[right]] >= left:
                result = max(result, right - left)
                left = indices[s[right]] + 1
            indices[s[right]] = right
            right += 1
        return max(result, right - left) # the last substring need to be considered