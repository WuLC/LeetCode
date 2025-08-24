# coding: utf8

# WA solution
# 基于 stack 来做
# s ="((()(()()))()((()()))))()((()(()"
# locked ="10111100100101001110100010001001"
# 最终剩下的是 8 和 31 的不能改变的 ')', 但如果不将 6 和 7 的可变的 '(' 相互抵消，最终 6、7 可以跟 8、31 的 ')' 抵消掉

class Solution:
    def canBeValid(self, s: str, locked: str) -> bool:
        stack, n = [], len(s)
        for i in range(n):
            if s[i] == '(':
                if locked[i] == '0' and len(stack) > 0 and (locked[stack[-1]] == '0' or s[stack[-1]] == '('):
                    stack.pop()
                else:
                    stack.append(i)
            else:
                if len(stack) > 0 and (locked[stack[-1]] == '0' or s[stack[-1]] == '('):
                    stack.pop()
                else:
                    stack.append(i)
        return len(stack) == 0


# AC solution
# 也是基于 stack 来做，但有 2 个 stack，分别存储 locked 的左括号的 index 和 unlocked 的 index
# 然后优先消耗 locked 的左括号与 locked 的有括号匹配
# 最终判断剩下的 locked 的左括号和 unlocked 的 index 能否匹配
class Solution:
    def canBeValid(self, s: str, locked: str) -> bool:
        n = len(s)
        if n&1:
            return False

        left, dynamic = [], []
        for i in range(len(s)):
            if locked[i] == '0':
                dynamic.append(i)
            elif s[i] == '(':
                left.append(i)
            else:
                if len(left) > 0:
                    left.pop()
                elif len(dynamic) > 0:
                    dynamic.pop()
                else:
                    return False
        
        while len(left) > 0 and len(dynamic) > 0 and left[-1] < dynamic[-1]:
            left.pop()
            dynamic.pop()
        
        return len(left) == 0

      