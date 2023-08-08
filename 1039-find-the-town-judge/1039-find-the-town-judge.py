class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        if not trust and n <= 1:
            return 1
        if not trust and n > 1:
            return -1

        in_ = dict()
        out = dict()
        for link in trust:
            x = link[0]
            y = link[1]
            if y in in_:
                in_[y].append(x)
            else:
                in_[y] = [x]
            if x in out:
                out[x].append(y)
            else:
                out[x] = [y]

        for x_ in in_:

            if len(in_[x_]) == n-1 and x_ not in out:
                return x_
        return -1


