class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        slow = 0
        n = len(nums)
        for i in range(n):
            if nums[i] % 2 == 0:
                nums[slow], nums[i] = nums[i], nums[slow]
                slow += 1
        
        return nums
        