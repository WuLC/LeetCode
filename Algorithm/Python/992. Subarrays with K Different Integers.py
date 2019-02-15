# -*- coding: utf-8 -*-
# Created on Thu Feb 14 2019 18:19:43
# Author: WuLC
# EMail: liangchaowu5@gmail.com

# two pointers
# refer: https://leetcode.com/problems/subarrays-with-k-different-integers/discuss/235235/C%2B%2B-with-picture-7-lines-56-ms
class Solution(object):
    def subarraysWithKDistinct(self, A, K):
        """
        :type A: List[int]
        :type K: int
        :rtype: int
        """
        left, right = 0, 0
        prefix, result = 0, 0
        count = {}
        while right < len(A):
            count.setdefault(A[right], 0)
            count[A[right]] += 1
            while len(count) > K:
                prefix = 0
                count[A[left]] -= 1
                if count[A[left]] == 0:
                    del count[A[left]]
                left += 1
            if len(count) == K:
                result += 1
                while count[A[left]] > 1:
                    count[A[left]] -= 1
                    prefix += 1
                    left += 1
            result += prefix
            right += 1
        return result