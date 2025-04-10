class Solution(object):
    def maxFreeTime(self, eventTime, k, startTime, endTime):
        """
        :type eventTime: int
        :type k: int
        :type startTime: List[int]
        :type endTime: List[int]
        :rtype: int
        """
        free_time = [startTime[0]]
        n = len(startTime)
        for i in range(n-1):
            free_time.append(startTime[i+1] - endTime[i])
        free_time.append(eventTime - endTime[n-1])


        left, right = 0, 0
        tmp, result = 0, 0
        while right < len(free_time):
            tmp += free_time[right]
            if right - left == k:
                result = max(result, tmp)
                tmp -= free_time[left]
                left += 1
            right += 1
        return result