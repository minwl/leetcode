class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        ans = []
        for row in range(numRows):
            if row < 2 :
                ans.append([1]*(row+1))
            else:
                ans.append(self.element(ans[row-1]))
        return ans


    
    def element(self, prev):
        next=[]
        nextlen = len(prev)+1
        for i in range(nextlen):
            if i == int(0) or i == len(prev):
                next.append(1)
            else:
                sub = prev[i-1]+prev[i]
                next.append(sub)
        return next




