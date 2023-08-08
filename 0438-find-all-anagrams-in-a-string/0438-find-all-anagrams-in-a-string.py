class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        cnt = [0]*26
        for ch in p:
            idx = ord(ch) - 97
            cnt[idx] += 1
        ans = []
        l = 0
        for r, c in enumerate(s):
            idx = ord(c)-97
            cnt[idx] -= 1
            while cnt[idx] < 0:  
                l_idx = ord(s[l])-97
                cnt[l_idx] += 1 
                l += 1
            if r - l + 1 == len(p):  
                ans.append(l)  # Add left index `l` to our result
                
        return ans
            
                
            