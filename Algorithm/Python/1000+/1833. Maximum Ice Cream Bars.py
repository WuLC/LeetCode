class Solution(object):
    def maxIceCream(self, costs, coins):
        """
        :type costs: List[int]
        :type coins: int
        :rtype: int
        """
        costs.sort()
        result = 0
        for cost in costs:
            if cost > coins:
                break
            result += 1
            coins -= cost
        return result
                