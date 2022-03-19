class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        res = n * (n+1) // 2
        for i in range(n):
            res -= nums[i]
        
        return res