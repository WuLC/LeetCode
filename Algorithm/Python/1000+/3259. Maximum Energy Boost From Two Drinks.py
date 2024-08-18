class Solution(object):
    def maxEnergyBoost(self, energyDrinkA, energyDrinkB):
        """
        :type energyDrinkA: List[int]
        :type energyDrinkB: List[int]
        :rtype: int
        """
        n = len(energyDrinkA)
        dpA, dpB = [0] * (n+1), [0] * (n+1)
        for i in range(n):
            if i == 0:
                dpA[i+1] = energyDrinkA[i]
                dpB[i+1] = energyDrinkB[i]
            else:
                dpA[i+1] = max(dpA[i], dpB[i-1]) + energyDrinkA[i]
                dpB[i+1] = max(dpA[i-1], dpB[i]) + energyDrinkB[i]
        return max(dpA[-1], dpB[-1])