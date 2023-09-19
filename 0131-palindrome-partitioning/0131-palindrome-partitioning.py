class Solution:
    def pal(self, s):
        return s == s[::-1]

    def partition(self, s: str) -> List[List[str]]:
        sub = []
        ans = []

        def backtracking(i):

            if i >= len(s):
                ans.append(sub[:])
                return

            for j in range(i, len(s)):
                if (self.pal(s[i:j+1])):
                    sub.append(s[i:j+1])
                    backtracking(j+1)
                    sub.pop()
            
        backtracking(0)
        return ans




        

                

