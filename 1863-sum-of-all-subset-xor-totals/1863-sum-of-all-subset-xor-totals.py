class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        
        self.xor_sum = 0
        self.backtrack(nums, [])
        return self.xor_sum
        
    def backtrack(self, arr, nums):
        temp = 0
        for num in nums:
            temp ^= num
        self.xor_sum += temp
        for i in range(len(arr)):
            self.backtrack(arr[i+1:], nums + [arr[i]])