class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        
        m = len(costs)
        ans = 0
        
        refund = []
        for i in range(m):
            ans += costs[i][0]
            refund.append(costs[i][1] - costs[i][0])
        
        refund.sort()
        # print(refund)
        for i in range(m//2):
            ans += refund[i]
        
        return ans
            
        