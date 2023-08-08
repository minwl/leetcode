class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        dct_s = dict()
        bulls = 0
        cows = 0
        for i, c in enumerate(secret):
            if guess[i] == c:
                bulls += 1
            if c in dct_s:
                dct_s[c] += 1
            else:
                dct_s[c] = 1
        
        for j, c in enumerate(guess):
            if c in dct_s and dct_s[c] > 0:
                cows += 1
                dct_s[c] -= 1
            
        
        ans = str(bulls) + "A" + str(cows-bulls) + "B"
        return ans
                    
        