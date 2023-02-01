#
# @lc app=leetcode id=941 lang=python
#
# [941] Valid Mountain Array
#

# @lc code=start
class Solution(object):
    def validMountainArray(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        idx = 0
        for i in range(1, len(arr)):
            if arr[i] > arr[idx]:
                idx = i
                
        if len(arr) < 3 or idx == 0 or idx == len(arr)-1:
            return False
        
        return all([arr[i-1] < arr[i] for i in range(1, idx)]) and\
                all([arr[i] > arr[i+1] for i in range(idx, len(arr)-1)])
         
# @lc code=end

