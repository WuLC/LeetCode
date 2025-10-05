# simple logic can AC
# since we are looking for the longest subsequence and order doesn't matter in this case
# we can take the xor result of the entire array, there are two cases
# 1) if it's not 0, then the length of the array is the result 
# 2) if it's 0, we only need 1 element that's not 0 to get the final subsequence
class Solution:
    def longestSubsequence(self, nums: List[int]) -> int:
        xor_res, n, has_non_zero = 0, len(nums), False
        for num in nums:
            xor_res ^= num
            if num > 0:
                has_non_zero = True
        
        if xor_res != 0:
            return n
        else:
            return n-1 if has_non_zero else 0


# TLE dp solution
# each idx has two status with xor operation ends with it,(1) result is 0 (2) result is not 0
# for each status, use a dp array to store the length of the longest subsequence
# for the non-zero reult, we also need to store the result the longest length
class Solution:
    def longestSubsequence(self, nums: List[int]) -> int:
        result, n = 0, len(nums)
        zero_len, non_zero_len, non_zero_res = [0]*n, [0]*n, [[] for _ in range(n)]
        
        for i in range(n):
            # init first element
            if i == 0:
                if nums[i] > 0:
                    non_zero_len[i] = 1
                    non_zero_res[i].append(nums[i])
                else:
                    zero_len[i] = 1
            else:
                for j in range(i-1, -1, -1):
                    # non-zero iteration
                    for _num in non_zero_res[j]:
                        _len, _res = non_zero_len[j]+1, _num^nums[i]
                        if _res == 0:
                            zero_len[i] = max(zero_len[i], _len)
                        else:
                            if _len > non_zero_len[i]:
                                non_zero_len[i] = _len
                                non_zero_res[i].clear()
                                non_zero_res[i].append(_res)
                            elif _len == non_zero_len[i]:
                                non_zero_res[i].append(_res)
                    
                    # zero iteration
                    _len = zero_len[j]+1
                    if nums[i] > 0:
                        if _len > non_zero_len[i]:
                            non_zero_len[i] = _len
                            non_zero_res[i].clear()
                            non_zero_res[i].append(nums[i])
                        elif _len == non_zero_len[i]:
                            non_zero_res[i].append(nums[i])
                    else:
                        zero_len[i] = max(zero_len[i], zero_len[j]+1)
                
            result = max(result, non_zero_len[i])
        return result
                    