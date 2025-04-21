class Solution(object):
    def minCosts(self, cost):
        """
        :type cost: List[int]
        :rtype: List[int]
        """
        result, prefix_min = [], cost[0]
        for i in range(len(cost)):
            prefix_min = min(prefix_min, cost[i])
            result.append(prefix_min)
        return result