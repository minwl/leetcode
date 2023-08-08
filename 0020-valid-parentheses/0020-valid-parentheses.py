class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        paren = {
            '(' : ')',
            '{' : '}',
            '[' : ']'
        }
        stack = []
        for i in s:
            if i in paren:
                stack.append(paren[i])
            else:
                if stack and i == stack[-1]:
                    stack.pop()
                else:
                    return False
        if len(stack) == 0:
            return True
