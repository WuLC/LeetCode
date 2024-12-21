from collections import defaultdict

class Solution(object):
    def maxAmount(self, initialCurrency, pairs1, rates1, pairs2, rates2):
        """
        :type initialCurrency: str
        :type pairs1: List[List[str]]
        :type rates1: List[float]
        :type pairs2: List[List[str]]
        :type rates2: List[float]
        :rtype: float
        """
        m1, m2 = defaultdict(dict), defaultdict(dict)
        self.convert2Map(pairs1, rates1, m1)
        self.convert2Map(pairs2, rates2, m2)
        m1_visited, m2_visited = set(), set()
        def dfs(curr, currSum, isDay1, result):
            if curr == initialCurrency and not isDay1:
                result[0] = max(result[0], currSum)
                return
            if isDay1:
                m1_visited.add(curr)
                for k, v in m1[curr].items():
                    if k in m1 and k not in m1_visited:
                        m1_visited.add(k)
                        dfs(k, currSum*v, isDay1, result)
                        m1_visited.remove(k)
                    if k in m2 and k not in m2_visited:
                        m2_visited.add(k)
                        dfs(k, currSum*v, not isDay1, result)
                        m2_visited.remove(k)
            if not isDay1:
                for k, v in m2[curr].items():
                    if k not in m2_visited:
                        m2_visited.add(k)
                        dfs(k, currSum*v, isDay1, result)
                        m2_visited.remove(k)
            
        result = [1.0]
        dfs(initialCurrency, 1.0, True, result)
        return result[0]
        

    def convert2Map(self, pairs, rates, m):
        assert len(pairs) == len(rates)
        for i in range(len(pairs)):            
            m[pairs[i][0]][pairs[i][1]] = rates[i]
            m[pairs[i][1]][pairs[i][0]] = 1.0/rates[i]
