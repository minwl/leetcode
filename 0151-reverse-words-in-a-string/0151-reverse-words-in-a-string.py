class Solution:
    def reverseWords(self, s: str) -> str:
        wordlist = []
        word = ""
        for char in s:
            if char != " ":
                word += char
            else:
                wordlist.append(word)
                word = ""
        wordlist.append(word)
        
        ans = ""
        print(wordlist)
        print(s.split())
        for word in wordlist[::-1]:
            if word == '' or word == ' ':
                continue
            ans += word +' '
            
        return ans.strip()