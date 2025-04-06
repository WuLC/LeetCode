# use prefix max and sufffix max to avoid brute-force iterating, thus to reduce time complexity to O(n)
# AC solution
class Solution(object):
    def maxFreeTime(self, eventTime, startTime, endTime):
        """
        :type eventTime: int
        :type startTime: List[int]
        :type endTime: List[int]
        :rtype: int
        """
        n = len(startTime)
        free_time = []
        for i in range(n-1):
            if i == 0:
                free_time.append(startTime[i] - 0)
            free_time.append(startTime[i+1] - endTime[i])
        free_time.append(eventTime - endTime[-1])

        largetst_left, largetst_right = [0]*n, [0] * n
        for i in range(1, n):
            largetst_left[i] = max(largetst_left[i-1], free_time[i-1])
        for i in range(n-2, -1, -1):
            largetst_right[i] = max(largetst_right[i+1], free_time[i+2])

        result = 0
        for i in range(n):
            result = max(result, free_time[i] + free_time[i+1])
            interval = endTime[i] - startTime[i]
            if interval <= largetst_left[i] or interval <= largetst_right[i]:
                result = max(result, free_time[i] + free_time[i+1] + interval)
        return result


# Failed solution, search with sorted index, worst time complexity O(n^2), still TLE
from collections import defaultdict
class Solution(object):
    def maxFreeTime(self, eventTime, startTime, endTime):
        """
        :type eventTime: int
        :type startTime: List[int]
        :type endTime: List[int]
        :rtype: int
        """
        n = len(startTime)
        free_time = []
        for i in range(n-1):
            if i == 0:
                free_time.append(startTime[i] - 0)
            free_time.append(startTime[i+1] - endTime[i])
        free_time.append(eventTime - endTime[-1])

        record = defaultdict(list)
        for i in range(n+1):
            record[free_time[i]].append(i)
        sorted_keys = sorted(record.keys(), reverse=True)

        result = 0
        for i in range(n):
            result = max(result, free_time[i] + free_time[i+1])
            interval = endTime[i] - startTime[i]
            for k in sorted_keys:
                if k >= interval and any(i!= idx and i+1!=idx for idx in record[k]):
                    result = max(result, free_time[i] + free_time[i+1] + interval)
        return result


# Failed solution, brute-force, TLE, time complexity O(n^2)
class Solution(object):
    def maxFreeTime(self, eventTime, startTime, endTime):
        """
        :type eventTime: int
        :type startTime: List[int]
        :type endTime: List[int]
        :rtype: int
        """
        n = len(startTime)
        free_time = []
        for i in range(n-1):
            if i == 0:
                free_time.append(startTime[i] - 0)
            free_time.append(startTime[i+1] - endTime[i])
        free_time.append(eventTime - endTime[-1])

        result = 0
        for i in range(n):
            result = max(result, free_time[i] + free_time[i+1])
            interval = endTime[i] - startTime[i]
            for j in range(n+1):
                if free_time[j] >= interval and (i != j and i+1 != j):
                    result = max(result, free_time[i] + free_time[i+1] + interval)
        return result


