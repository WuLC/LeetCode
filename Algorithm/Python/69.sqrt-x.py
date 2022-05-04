#
# @lc app=leetcode id=69 lang=python
#
# [69] Sqrt(x)
#

# @lc code=start
class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        left, right = 0, x
        while left <= right:
            mid = left + ((right-left)>>1)
            num = mid**2
            if num == x:
                return mid
            elif num > x:
                right = mid - 1
            else:
                left = mid + 1
        return left if left**2 < x else left-1
            
# @lc code=end

