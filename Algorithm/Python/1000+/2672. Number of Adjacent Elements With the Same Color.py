class Solution(object):
    def colorTheArray(self, n, queries):
        """
        :type n: int
        :type queries: List[List[int]]
        :rtype: List[int]
        """
        result, cnt = [], 0
        colors = [0] * n
        for idx, color in queries:
            for i in (idx-1, idx+1):
                if i >= 0 and i < n:
                    if colors[i] > 0 and colors[i] == colors[idx]:
                        cnt -= 1
                    if colors[i] == color:
                        cnt += 1
            colors[idx] = color
            result.append(cnt)
        return result