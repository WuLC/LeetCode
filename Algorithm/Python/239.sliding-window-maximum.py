#
# @lc app=leetcode id=239 lang=python
#
# [239] Sliding Window Maximum
#

# @lc code=start
from collections import deque


class Solution(object):
    def maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        result, idx = [], deque()
        for i in range(len(nums)):
            while len(idx) > 0 and nums[i] >= nums[idx[-1]]:
                idx.pop()
            idx.append(i)
            if i - idx[0] >= k:
                idx.popleft()
            if i >= k-1:
                result.append(nums[idx[0]])
        return result
        
# @lc code=end

