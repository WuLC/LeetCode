# -*- coding: utf-8 -*-
# Created on Wed Jan 16 2019 20:19:47
# Author: WuLC
# EMail: liangchaowu5@gmail.com

# for problems about "sum of contiguous subarray", prefix sum is a common technique
# referer: https://leetcode.com/problems/subarray-sums-divisible-by-k/discuss/217980/Java-O(N)-with-HashMap-and-prefix-Sum
class Solution(object):
    def subarraysDivByK(self, A, K):
        """
        :type A: List[int]
        :type K: int
        :rtype: int
        """
        mod_count = [0] * K
        mod_count[0] = 1
        result, prefix = 0, 0
        for num in A:
            prefix = (prefix + num) % K
            if prefix < 0:
                prefix += K
            result += mod_count[prefix]
            mod_count[prefix] += 1
        return result