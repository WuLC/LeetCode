# try stack when meeting adjacent comparing problem
class Solution:
    def resultingString(self, s: str) -> str:
        stack = []
        for i in range(len(s)):
            if len(stack) > 0 and abs(ord(s[stack[-1]]) - ord(s[i])) in (1, 25):
                stack.pop()
            else:
                stack.append(i)
        return ''.join(s[i] for i in stack)
            