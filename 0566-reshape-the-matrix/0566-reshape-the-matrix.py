class Solution(object):
    def matrixReshape(self, mat, r, c):
        """
        :type mat: List[List[int]]
        :type r: int
        :type c: int
        :rtype: List[List[int]]
        """
        
        m = len(mat)
        n = len(mat[0])
        if m*n != r*c:
            return mat
        newmat = [[0 for _ in range(c)]for _ in range(r)]
        ni = 0
        nj = 0
        for i in range(m):
            for j in range(n):
                if nj == c:
                    nj = 0
                    ni += 1 
                newmat[ni][nj] = mat[i][j]
                nj+=1

        return newmat
            


