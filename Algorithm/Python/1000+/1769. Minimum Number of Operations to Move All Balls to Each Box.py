class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        n = len(boxes)
        left_pre, right_pre = [0]*n, [0]*n
        cnt = 0
        for i in range(n):
            left_pre[i] = left_pre[i-1]+cnt if i > 0 else 0
            if boxes[i] == '1':
                cnt += 1
        
        cnt = 0
        for i in range(n-1, -1, -1):
            right_pre[i] = right_pre[i+1]+cnt if i < n-1 else 0
            if boxes[i] == '1':
                cnt += 1
        
        return [left_pre[i]+right_pre[i] for i in range(n)]