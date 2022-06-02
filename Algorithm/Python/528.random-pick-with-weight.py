#
# @lc app=leetcode id=528 lang=python
#
# [528] Random Pick with Weight
#

# @lc code=start
import random
class Solution(object):

    def __init__(self, weights):
        """
        :type w: List[int]
        """
        _sum = sum(weights)
        prob = [w*1.0/_sum for w in weights]
        self.range, curr_sum = [], 0
        for i in range(len(prob)):
            self.range.append((curr_sum, curr_sum + prob[i]))
            curr_sum += prob[i]        
        
    def pickIndex(self):
        """
        :rtype: int
        """
        num = random.uniform(0, 1)
        left, right = 0, len(self.range) - 1
        while right > left:
            mid = left + ((right - left)>>1)
            if self.range[mid][0] <= num < self.range[mid][1]:
                return mid
            elif self.range[mid][0] > num:
                right = mid - 1
            else:
                left = mid + 1
        return left
        


# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()
# @lc code=end

