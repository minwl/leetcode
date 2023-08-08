class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        check = dict()
        curr = 0
        maxlen = 0
        for idx, char in enumerate(s):
            if char not in check or check[char] < curr:
                maxlen = max(maxlen, idx-curr+1)
            else:
                curr = check[char] + 1
            check[char] = idx
            
        return maxlen