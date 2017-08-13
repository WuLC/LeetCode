# -*- coding: utf-8 -*-
# @Author: WuLC
# @Date:   2017-08-13 10:08:28
# @Last Modified by:   WuLC
# @Last Modified time: 2017-08-13 10:09:07


# two pointers
class Solution(object):
    def findClosestElements(self, arr, k, x):
        """
        :type arr: List[int]
        :type k: int
        :type x: int
        :rtype: List[int]
        """
        if arr[0] >= x:
            return arr[:k]
        elif arr[-1] <= x:
            return arr[-k:]
        
        result = []
        idx = None
        for i in xrange(len(arr)):
            if arr[i] >= x:
                idx = i
                break
        p1, p2 = idx - 1, idx
        while len(result) < k:
            if p1 >= 0 and p2 < len(arr):
                if x - arr[p1] <= arr[p2] - x:
                    result.insert(0, arr[p1])
                    p1 -= 1
                else:
                    result.append(arr[p2])
                    p2 += 1
            elif p1 < 0:
                result.append(arr[p2])
                p2 += 1
            else:
                result.insert(0, arr[p1])
                p1 -= 1
        return result