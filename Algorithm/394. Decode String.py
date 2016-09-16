class Solution(object):
    def decodeString(self, s):
        """
        :type s: str
        :rtype: str
        """
        stack, tmp, result, i  = [], '', '', 0
        while i < len(s):
            if '1' <= s[i] <= '9':
                if tmp: stack.append(tmp)
                num = ''
                # multiple digits
                while '0' <= s[i] <= '9':
                    num += s[i]
                    i += 1
                stack.append(int(num))
                continue
            elif s[i] == '[':
                tmp = ''
            elif s[i] == ']':
                while stack:
                    e = stack.pop()
                    if isinstance(e, int):
                        tmp = tmp * e
                        break
                    else:
                        tmp = e + tmp
                stack.append(tmp)
                tmp = ''
            else:
                tmp += s[i]
            i += 1
        if tmp:
            result = tmp
        while stack:
            tmp = stack.pop()
            if isinstance(tmp, int):
                result = result * tmp
            else:
                result = tmp + result
        return result
