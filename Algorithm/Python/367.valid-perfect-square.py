#
# @lc app=leetcode id=367 lang=python
#
# [367] Valid Perfect Square
#

# @lc code=start
class Solution(object):
    def isPerfectSquare(self, num):
        """
        :type num: int
        :rtype: bool
        """
        left, right = 0, num
        while left <= right:
            mid = left + ((right-left)>>1)
            val = mid**2
            if val == num:
                return True
            elif val > num:
                right = mid - 1
            else:
                left = mid + 1
        return False
        
# @lc code=end

