# -*- coding: utf-8 -*-
# @Author: LC
# @Date:   2016-06-29 19:48:17
# @Last modified by:   WuLC
# @Last Modified time: 2016-06-30 17:17:24
# @Email: liangchaowu5@gmail.com


# method 1, time complexity O(kn)
class Solution(object):
    def containsNearbyAlmostDuplicate(self, nums, k, t):
        """
        :type nums: List[int]
        :type k: int
        :type t: int
        :rtype: bool
        """
        n = len(nums)
        for i in xrange(n):
            j = 1
            while j<=k and i+j<n:
                if abs(nums[i]-nums[i+j])<=t:
                    return True
                j += 1
        return False

# buckets, time complexity, O(n)
class Solution(object):
    def containsNearbyAlmostDuplicate(self, nums, k, t):
        """
        :type nums: List[int]
        :type k: int
        :type t: int
        :rtype: bool
        """
        bucket = {}
        for i in xrange(len(nums)):
            count, offset = (nums[i]/t, 1) if t!=0  else (nums[i], 0)
            for j in xrange(count - offset, count + offset + 1):
                if j in bucket and abs(bucket[j] - nums[i])<=t:
                    return True
            bucket[count] = nums[i]
            if len(bucket) > k:
                if t != 0:
                    del(bucket[nums[i-k]/t])
                else:
                    del(bucket[nums[i-k]])
        return False