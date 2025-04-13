# greedy, get number of shared food as many as possible with gaps between hamsters
class Solution(object):
    def minimumBuckets(self, hamsters):
        """
        :type hamsters: str
        :rtype: int
        """
        n, last_h, h_count = len(hamsters), 0, 0
        gaps = []
        for i in range(n):
            if hamsters[i] == 'H':
                h_count += 1
                if h_count == 1:
                    gaps.append(i - last_h)
                else:
                    gaps.append(i - last_h - 1)
                last_h = i
        gaps.append(n - 1 - last_h)

        result = h_count
        shared = [False] * len(gaps)
        for i in range(1, len(gaps)):
            if gaps[i] == 0 and gaps[i-1] == 0:
                return -1
            if gaps[i] == 1 and not shared[i-1] and i != len(gaps)-1:
                result -= 1
                shared[i] = True
        return result
