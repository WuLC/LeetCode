#
# @lc app=leetcode id=406 lang=python
#
# [406] Queue Reconstruction by Height
#

# @lc code=start
class Solution(object):
    def reconstructQueue(self, people):
        """
        :type people: List[List[int]]
        :rtype: List[List[int]]
        """
        def comparator(x1, x2):
            if x1[0] == x2[0]:
                return x1[1] - x2[1]
            else:
                return x2[0] - x1[0]
        
        sp = sorted(people, cmp = comparator)

        for i in range(len(sp)):
            _, k = sp[i]
            if i > k:
                # insert in to (k+1)th
                idx = i
                while idx > k:
                    sp[idx], sp[idx-1] = sp[idx-1], sp[idx]
                    idx -= 1
        return sp
                

                    
# @lc code=end

