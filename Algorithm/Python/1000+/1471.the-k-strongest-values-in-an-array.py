#
# @lc app=leetcode id=1471 lang=python3
#
# [1471] The k Strongest Values in an Array
#

# @lc code=start
        
class Solution:
    def getStrongest(self, arr: List[int], k: int) -> List[int]:
        arr.sort()
        n = len(arr)
        mid = arr[int((n-1)/2)]
        
        left, right, result = 0, n-1, []
        while k > 0:
            if abs(arr[right] - mid) >= abs(arr[left] - mid):
                result.append(arr[right])
                right -= 1
            else:
                result.append(arr[left])
                left += 1
            k -= 1
        return result
    
# @lc code=end

