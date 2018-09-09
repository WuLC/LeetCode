# -*- coding: utf-8 -*-
# Created on Mon Sep 03 2018 21:8:12
# Author: WuLC
# EMail: liangchaowu5@gmail.com

# dp, O(30n)
# referer: https://leetcode.com/problems/bitwise-ors-of-subarrays/discuss/165881/C++JavaPython-O(30N)
class Solution(object):
    def subarrayBitwiseORs(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        result, curr = set(), set()
        for num in A:
          curr = {e|num for e in curr}|{num}
          result |= curr
        return len(result)