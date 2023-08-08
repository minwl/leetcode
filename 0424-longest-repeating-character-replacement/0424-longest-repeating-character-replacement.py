class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        freq = [0]*26
        maxfreq = 0
        maxlen = 0
        i, j = 0, 0
        for j, c in enumerate(s):
            idx = ord(c)-65
            freq[idx] += 1
            maxfreq = max(maxfreq, freq[idx])
            
            if ((j-i+1) - maxfreq) > k:
                i_idx = ord(s[i])-65 #invalid
                freq[i_idx] -= 1
                i += 1
            else: #valid
                maxlen = max(maxlen, (j-i+1))
            j += 1
        return maxlen
                
            