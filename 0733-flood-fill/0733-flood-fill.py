class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        r = len(image)
        c = len(image[0])
        ori_color = image[sr][sc]
        if ori_color == color:
            return image
        def dfs(image, i, j, r,c,color,ori_color):
            if 0<=i<r and 0<=j<c:
                if image[i][j]==ori_color:            
                    adj = [(0,1), (0,-1),(1,0),(-1,0)]
                    image[i][j] = color
                    for idx in adj:
                        x = i + idx[0]
                        y = j + idx[1]
                        dfs(image, x,y,r,c,color,ori_color)
                    return image
        dfs(image, sr,sc,r,c,color,ori_color)
        return image
        
