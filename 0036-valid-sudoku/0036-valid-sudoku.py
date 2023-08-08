class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        r = len(board)
        c = len(board[0])
        for row in board:
            rowdic = {}
            for rowval in row:
                if rowval in rowdic and rowval != ".":
                    return False
                else:
                    rowdic[rowval] = 1


        #check column
        for col in range(c):
            coldic = {}
            for row in range(r):
                colval = board[row][col]
                if colval in coldic and colval != ".":
                    return False
                else:
                    coldic[colval] = 1
        
        #check subbox
        for b in range(3):
            for a in range(3):
                boxdic = {}
                for i in range(3):
                    for j in range(3):
                        boxval = board[i+a*3][j+b*3]
                        if boxval in boxdic and boxval != ".":
                            return False
                        else:
                            boxdic[boxval] = 1
        
        return True

            
        