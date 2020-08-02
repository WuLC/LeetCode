class Solution(object):
    def getWinner(self, arr, k):
        """
        :type arr: List[int]
        :type k: int
        :rtype: int
        """
        idx, cnt, curr_num = 1, 0, arr[0]
        while idx < len(arr):
            if curr_num < arr[idx]:
                curr_num = arr[idx]
                cnt = 1
            else:
                cnt += 1
            if cnt == k:
                break
            idx += 1
        return curr_num