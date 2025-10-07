class Solution:
    def removeSubstring(self, s: str, k: int) -> str:
        stack = []
        for c in s:
            n = len(stack)
            if c == ')' and n+1 >= 2*k\
                and all(stack[i]== ')' for i in range(n-k+1, n))\
                and all(stack[i]== '(' for i in range(n-k*2+1, n-k+1)):
                    for _ in range(k*2-1):
                        stack.pop()
            else:
                stack.append(c)
        
        return ''.join([c for c in stack])