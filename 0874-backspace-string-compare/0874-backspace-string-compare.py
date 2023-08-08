class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        i,j = 0,0
        while '#' in s and i < len(s):
            if s[0] == '#':
                s = s[1:]
                i = 0
            if s[i] == "#":
                s = s[0:i-1] + s[i+1:]
                i =0

            i += 1
            
        while '#' in t and j < len(t):
            if t[0] == '#':
                t = t[1:]
                j =0
            elif t[j] == "#":
                t = t[0:j-1] + t[j+1:]
                j = 0
            j += 1
            
        return s == t
        