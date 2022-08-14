#
# @lc app=leetcode id=860 lang=python
#
# [860] Lemonade Change
#

# @lc code=start
from collections import defaultdict

class Solution(object):
    def lemonadeChange(self, bills):
        """
        :type bills: List[int]
        :rtype: bool
        """
        remains = defaultdict(int)
        for b in bills:
            remains[b] += 1
            change = b - 5
            for candidate in [10, 5]:
                while change > 0 and change >= candidate and remains[candidate] > 0:
                    change -= candidate
                    remains[candidate] -= 1
            if change > 0:
                return False
        return True

# @lc code=end

