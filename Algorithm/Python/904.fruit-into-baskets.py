#
# @lc app=leetcode id=904 lang=python
#
# [904] Fruit Into Baskets
#

# @lc code=start

from collections import Counter

class Solution(object):
    def totalFruit(self, fruits):
        """
        :type fruits: List[int]
        :rtype: int
        """
        counter = Counter()
        left, right, result, valid_fruit = 0, 0, 0, 0
        while right <= len(fruits):
            while valid_fruit > 2:
                counter[fruits[left]] -= 1
                if counter[fruits[left]] == 0:
                    valid_fruit -= 1
                left += 1
            result = max(result, right - left)
            if right < len(fruits):
                if counter[fruits[right]] == 0:
                    valid_fruit += 1
                counter[fruits[right]] += 1
            right += 1
        return result
        
# @lc code=end

