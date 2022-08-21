#
# @lc app=leetcode id=763 lang=python
#
# [763] Partition Labels
#

# @lc code=start
from filecmp import cmp


class Solution(object):
    def partitionLabels(self, s):
        """
        :type s: str
        :rtype: List[int]
        """
        intervals = dict()
        for i in range(len(s)):
            if s[i] not in intervals:
                intervals[s[i]] = [i, i]
            else:
                intervals[s[i]][1] = i
        
        def comparator(x1, x2):
            if x1[0] == x2[0]:
                return x1[1] - x2[1]
            else:
                return x1[0] - x2[0]    
        
        sorted_intervals = sorted(intervals.values(), cmp = comparator)
        pre_start, pre_end = sorted_intervals[0]
        result = []
        for i in range(1, len(sorted_intervals)):
            s, e = sorted_intervals[i]
            if s < pre_end:
                pre_end = max(pre_end, e)
            else:
                result.append(pre_end - pre_start + 1)
                pre_start, pre_end = s, e
        result.append(pre_end - pre_start + 1)
        return result
                
# @lc code=end

