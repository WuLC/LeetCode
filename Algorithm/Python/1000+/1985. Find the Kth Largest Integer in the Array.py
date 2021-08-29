import heapq
class StrNum(object):
    def __init__(self, s: str):
        self.val = s
    
    def __lt__(self, other) -> bool:
        if len(self.val) != len(other.val):
            return len(self.val) < len(other.val)
        for i in range(len(self.val)):
            if self.val[i] != other.val[i]:
                return self.val[i] < other.val[i]
        return False

    
class Solution:
    def kthLargestNumber(self, nums: List[str], k: int) -> str:
        heap = []
        heapq.heapify(heap)
        for i in range(len(nums)):
            if len(heap) > k:
                heapq.heappushpop(heap, StrNum(nums[i]))
            else:
                heapq.heappush(heap, StrNum(nums[i]))
        while len(heap) > k:
            heapq.heappop(heap)
        return heapq.heappop(heap).val
            
        