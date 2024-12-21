class Solution(object):
    def buttonWithLongestTime(self, events):
        """
        :type events: List[List[int]]
        :rtype: int
        """
        idx, t = events[0]
        for i in range(1, len(events)):
            diff = events[i][1] - events[i-1][1]
            if diff > t:
                idx, t = events[i][0], diff
            elif diff == t:
                idx = min(idx, events[i][0])
        return idx