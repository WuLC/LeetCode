#
# @lc app=leetcode id=34 lang=python
#
# [34] Find First and Last Position of Element in Sorted Array
#

# @lc code=start
class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        def find_idx(first_idx):
            left, right = 0, len(nums) - 1
            while left < right:
                mid = left + ((right - left)>>1)
                if nums[mid] == target:
                    if first_idx:
                        right = mid
                    else:
                        if mid + 1 < len(nums):
                            if nums[mid+1] != target:
                                left = mid
                                break
                            else:
                                left = mid + 1
                elif nums[mid] > target:
                    right = mid - 1
                else:
                    left = mid + 1
            
            return left if left < len(nums) and nums[left] == target else -1
        
        return [find_idx(True), find_idx(False)]
            

        
# @lc code=end

