class Solution(object):
    def minOperations(self, n):
        """
        :type n: int
        :rtype: int
        """
        return sum([n-2*i-1 for i in range(n>>1)])