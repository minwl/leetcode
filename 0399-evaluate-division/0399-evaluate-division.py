class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        dct = dict()
        for i in range(len(equations)):
            var1 = equations[i][0]
            var2 = equations[i][1]
            value = values[i]
            if var1 in dct: dct[var1][var2] = value
            else: dct[var1] = {var2 : value}
            if var2 in dct: dct[var2][var1] = 1/value
            else: dct[var2] = {var1 : 1/value}

        def dfs(x, y, dct, visited, ans, temp):
            if x in visited:
                return
            visited.add(x)
            if x == y:
                ans[0] = temp
                return
            
            for node, val in dct[x].items():
                dfs(node, y, dct, visited, ans, temp*val)

        queryans = []
        ans = []
        print(dct)
        for q in queries:
            x = q[0]
            y = q[1]
            if x not in dct or y not in dct:
                ans.append(-1.0)
            else:
                visited = set()
                queryans = [-1.0]
                temp = 1.0
                dfs(x, y, dct, visited, queryans, temp)
                ans.append(queryans[0])
        return ans

        #     if x in dct:
        #         if x == y:
        #             ans.append(1.0)
        #         elif y in dct[x]:
        #             ans.append(dct[x][y])
        #         else:
        #             check = False
        #             for k in dct[x].keys():
        #                 if k in dct and y in dct[k]:
        #                     ans.append(dct[x][k]*dct[k][y])
        #                     check = True
        #                     break
        #                 else:
        #                     continue
        #             if not check : ans.append(-1.0)
        #     else:
        #         ans.append(-1.0)
        # return ans