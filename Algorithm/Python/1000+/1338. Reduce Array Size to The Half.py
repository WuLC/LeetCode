from collections import Counter
class Solution(object):
    def minSetSize(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        counter = Counter(arr)
        sorted_counter = sorted(counter.items(), key = lambda x: x[1], reverse=True)
        result, curr_count = 0, 0
        for k, v in sorted_counter:
            result += 1
            curr_count += v
            if curr_count >= (len(arr)>>1):
                break
        return result
