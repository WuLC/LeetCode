# -*- coding: utf-8 -*-
# @Author: WuLC
# @Date:   2017-02-19 21:42:03
# @Last modified by:   WuLC
# @Last Modified time: 2017-02-19 22:41:58
# @Email: liangchaowu5@gmail.com

# naive solution, time o(nk), AC
# one trick: ~n = -(n+1), n is a positive number
class Solution(object):
    def medianSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[float]
        """
        window = sorted(nums[:k-1])
        result = []
        for i in xrange(k-1, len(nums)):
            bisect.insort(window, nums[i])
            result.append((window[k/2] + window[~(k/2)])/2.0)
            window.remove(nums[i-k+1])
        return result
            

# two heaps, time O(nlogk), but  python don't support max_heap, need to implement 