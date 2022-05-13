class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        ans = []
        n = len(nums)
        def backtrack(nums, arr):
            if len(arr) == n and arr not in ans:
                ans.append(arr)

            for i in range(len(nums)):
                backtrack(nums[:i]+nums[i+1:], arr+[nums[i]])
        backtrack(nums, [])
        return ans