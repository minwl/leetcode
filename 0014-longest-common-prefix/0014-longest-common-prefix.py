class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        ans = ""
        for char in zip(*strs):
            if len(set(char)) == 1:
                ans += char[0]
            else : break
        return ans