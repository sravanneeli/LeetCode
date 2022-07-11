class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        dp0 = cost[0]
        if n >= 2:
            dp1 = cost[1]
            
        for i in range(2, n):
            curr = cost[i] + min(dp0, dp1)
            dp0 = dp1
            dp1 = curr
            # print(dp0, dp1)
        return min(dp0, dp1)
        
        