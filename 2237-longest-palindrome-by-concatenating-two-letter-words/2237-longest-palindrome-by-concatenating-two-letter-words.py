class Solution:
    def longestPalindrome(self, words: List[str]) -> int:
        freqs = Counter(words)

        ans = 0
        check = False
        for word, count in freqs.items():
            rev = word[::-1]
            if word == rev:
                if count == 1:
                    if not check:
                        ans += 2
                        check = True

                else:
                    if count%2 == 0:
                        ans += count*2

                    else:
                        if not check:
                            ans += count*2
                            check = True
                        else:
                            ans += (count-1)*2
                        


            elif rev in freqs:
                ans += 2*(min(count, freqs[rev]))
 
        return ans
                