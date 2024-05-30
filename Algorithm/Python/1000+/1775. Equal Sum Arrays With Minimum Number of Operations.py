#greedy
class Solution(object):
    def minOperations(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: int
        """
        n1, n2 = len(nums1), len(nums2)
        if 6*n2 < n1 or  6*n1 < n2:
            return -1
        nums1.sort()
        nums2.sort()
        result = 0
        s1, s2 = sum(nums1), sum(nums2)
        diff = s2 - s1
        # always make s2 > s1
        if diff < 0:
            nums1, nums2 = nums2, nums1
            n1, n2 = n2, n1
            diff = abs(diff)
        
        idx1, idx2 = 0, n2 - 1
        while diff > 0 and (idx1 < n1 or idx1 >= 0):
            diff1 = 0 if idx1 >= n1 else 6 - nums1[idx1]
            diff2 = 0 if idx2 < 0 else nums2[idx2] - 1
            if diff1 > diff2:
                diff -= diff1
                idx1 += 1
            else:
                diff -= diff2
                idx2 -= 1
            result += 1
        return result    


