# -*- coding: utf-8 -*-
# @Author: WuLC
# @Date:   2017-05-30 15:13:36
# @Last Modified by:   WuLC
# @Last Modified time: 2017-05-30 15:57:56


# naive solution
# O(n) space, O(n^2) time, TLE
class Solution(object):
    def arrayNesting(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        result = 0
        for num in nums:
            visited = set()
            idx = num
            while idx not in visited:
                visited.add(idx)
                idx = nums[idx]
            if len(visited) == len(nums):
                return len(nums)
            result = max(result, len(visited))
        return result



# optimize based on the last solution, roughly O(n) time, O(n) space
# since all visited numbers from the start number will not have longer nesting than the start number
class Solution(object):
    def arrayNesting(self, nums):
        result = 0
        visited = set()
        for num in nums:
            if num in visited:
                continue
            idx = num
            curr_visited = set()
            while idx not in curr_visited:
                curr_visited.add(idx)
                visited.add(idx)
                idx = nums[idx]
            if len(curr_visited) == len(nums):
                return len(nums)
            result = max(result, len(curr_visited))
        return result


# optimize based on the last solution
# remove the set curr_visited since the mapping is one-to-one, loop appears only when the start number is revisited again
class Solution(object):
    def arrayNesting(self, nums):
        result = 0
        visited = set()
        for num in nums:
            if num in visited:
                continue
            visited.add(num)
            count = 1
            idx = nums[num]
            while idx != num :
                visited.add(idx)
                idx = nums[idx]
                count += 1
            if count == len(nums):
                return count
            result = max(result, count)
        return result