class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        
        self.ans = []

        def subpath(start, path, k, targetsum):
            if k ==0 and targetsum == 0:
                self.ans.append(path)
            if k < 0 or targetsum <= 0:
                return
            for i in range(start, 10):
                subpath(i+1, path+[i], k-1, targetsum-i)

        subpath(1,[],k,n)
        return self.ans