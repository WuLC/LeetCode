class Solution(object):
    def containsPattern(self, arr, m, k):
        """
        :type arr: List[int]
        :type m: int
        :type k: int
        :rtype: bool
        """
        for i in range(len(arr) - m*k + 1):
            if arr[i:i+m*k] == arr[i:i+m] * k:
                return True
        return False