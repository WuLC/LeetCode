class Solution(object):
    def minSwaps(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n, digit_sum = len(nums), []
        for i in range(n):
            digit_sum.append([sum(int(c) for c in str(nums[i])), nums[i], i])
        digit_sum.sort(key = lambda x:(x[0], x[1]))

        result = 0
        for i in range(n):
            _, _, idx = digit_sum[i]
            while idx != i:
                result += 1
                digit_sum[i], digit_sum[idx] = digit_sum[idx], digit_sum[i]
                _, _, idx = digit_sum[i]
        return result