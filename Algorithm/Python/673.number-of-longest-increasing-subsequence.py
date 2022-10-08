#
# @lc app=leetcode id=673 lang=python
#
# [673] Number of Longest Increasing Subsequence
#

# @lc code=start
class Solution(object):
    def findNumberOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        length, count = [1] * n, [1] * n
        max_len = 1
        for i in range(1, n):
            for j in range(i):
                if nums[i] > nums[j] and length[i] <= length[j] + 1:
                    if length[i] == length[j] + 1:
                        count[i] += count[j]
                    else:
                        count[i] = count[j]
                    length[i] = length[j] + 1
            max_len = max(max_len, length[i])
        return sum(count[i] for i in range(n) if length[i] == max_len)
        
# @lc code=end

