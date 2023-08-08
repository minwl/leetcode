class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        i = 0
        while i < len(s):
            if "0" <= s[i] <= "9":
                start = i
                while "0" <= s[i] <= "9":
                    i += 1
                stack.append(int(s[start:i]))
            elif s[i] != "]":
                stack.append(s[i])
                i+=1
            elif s[i] == ']':
                ans = ""
                while stack[-1] != '[':
                    ans += stack.pop()
                #ans = ans[::-1]
                stack.pop()
                num = int(stack.pop())
                stack.append(num*ans)
                i+=1
        return "".join([i[::-1] for i in stack])
                