class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        left, top = 0,0
        bot, right = len(matrix), len(matrix[0])
        ans = []
        visit = set()
        while left < right and top < bot:
            for j in range(left, right):
                if (top, j) not in visit:
                    visit.add((top, j))
                    ans.append(matrix[top][j])
            top += 1
            for i in range(top, bot):
                if (i, right-1) not in visit:
                    visit.add((i,right-1))
                    ans.append(matrix[i][right-1])
            right -= 1
            for j in range(right-1, left-1,-1):
                if (bot-1, j) not in visit:
                    visit.add((bot-1, j))
                    ans.append(matrix[bot-1][j])
            bot -= 1
            for i in range(bot-1, top-1,-1):
                if (i,left) not in visit:
                    visit.add((i,left))
                    ans.append(matrix[i][left])
            left += 1
        return ans    