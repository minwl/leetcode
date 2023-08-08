class Solution:
    def longestPalindrome(self, s: str) -> int:
        single = set()
        count = 0
        for c in s:
            if c not in single:
                single.add(c)
            else :
                single.remove(c)
                count += 2
        if single:
            count += 1
        return count