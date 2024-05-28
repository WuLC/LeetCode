from collections import defaultdict

class Solution(object):
    def maximumLength(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        counter = defaultdict(int)
        for num in nums:
            counter[num] += 1
        
        result = 1
        for num in nums:
            # early stop
            if num**2 > nums[-1]:
                break

            cnt = 0
            while counter[num] > 0:
                if counter[num] >= 2 and counter[num**2] > 0:
                    cnt += 2
                    counter[num] -= 2 
                else:
                    cnt += 1
                    break
                num = num**2
            result = max(result, cnt)
        # special case
        if result&1 == 0:
            result -= 1
        return result
