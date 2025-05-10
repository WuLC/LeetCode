# AC solution
# use str as key instead of float with gcd
# str key can also be divied into a matrix
from collections import defaultdict

class Solution(object):
    def numberOfSubsequences(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # use str as key instead of float
        # python3.5 can use math.gcd
        def gcd(a, b):
            while b != 0:
                a, b = b, a%b
            return abs(a)
        
        n, result = len(nums), 0
        prefix = defaultdict(int)
        for q in range(2, n):
            # update prefix
            for p in range(q-2, -1, -1):
                _gcd = gcd(nums[p], nums[q])
                prefix[str(int(nums[p]/_gcd))+'/'+str(int(nums[q]/_gcd))] += 1

            # calc result with prefix
            r = q + 2
            for s in range(r+2, n):
                _gcd = gcd(nums[r], nums[s])
                result += prefix[str(int(nums[s]/_gcd))+'/'+str(int(nums[r]/_gcd))]
        return result
                

# MLE solution
# use prefix and suffix map will lead to MLE
from collections import defaultdict

class Solution(object):
    def numberOfSubsequences(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # use str as key instead of float
        def gcd(a, b):
            a, b = max(a, b), min(a, b)
            while a%b > 0:
                a, b = b, a%b
            return b
        
        n = len(nums)
        prefix, suffix = [defaultdict(int) for _ in range(n)], [defaultdict(int) for _ in range(n)]
        for i in range(n):
            l, r = i-2, i+2
            while l >= 0:
                l_gcd = gcd(nums[l], nums[i])
                prefix[i][str(int(nums[l]/l_gcd))+'/'+str(int(nums[i]/l_gcd))] += 1
                l -= 1
            while r < n:
                r_gcd = gcd(nums[i], nums[r])
                suffix[i][str(int(nums[r]/r_gcd))+'/'+str(int(nums[i]/r_gcd))] += 1
                r += 1

        result = 0
        for i in range(2, n):
            for j in range(i+2, n-2):
                for k, v in prefix[i].items():
                    result += suffix[j][k]*v
        return result
                

# TLE solution
# naive backtracking will lead to TLE
class Solution(object):
    def numberOfSubsequences(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        result = [0]

        def dfs(idx, cands, result):
            if len(cands) == 4:
                if nums[cands[0]] * nums[cands[2]] == nums[cands[1]] * nums[cands[3]]:
                    result[0] += 1
                return
            else:
                for i in range(idx, len(nums)):
                    if len(cands) == 0 or i - cands[-1] > 1:
                        cands.append(i)
                        dfs(i+1, cands, result)
                        cands.pop()

        dfs(0, [], result)
        return result[0]