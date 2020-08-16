class Solution(object):
    def threeConsecutiveOdds(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        cnt = 0
        for num in arr:
            if num&1:
                cnt += 1
                if cnt == 3:
                    return True
            else:
                cnt = 0
        return False