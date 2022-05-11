class Solution:
    
    def countVowelStrings(self, n: int) -> int:
        dp = [0] + [1] * 5
        
        for i in range(1, n+1):
            for j in range(1, 6):
                dp[j] += dp[j-1]
            # print(dp)
        return dp[5]
                
            
        