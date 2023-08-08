class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        dp = [0 for _ in range(n)]
        def minCost(cost, n, dp):
            if n == 0 or n == 1 :
                return cost[n]
            if dp[n] != 0:
                return dp[n]
            dp[n] = cost[n] + min(minCost(cost, n-1, dp), minCost(cost, n-2, dp))
            return dp[n]
        return min(minCost(cost, n-1, dp), minCost(cost, n-2, dp))
                    