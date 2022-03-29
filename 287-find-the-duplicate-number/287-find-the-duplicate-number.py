class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        nums_dict = {}
        for num in nums:
            nums_dict[num] = nums_dict.get(num, 0) + 1
        
        for num in nums_dict:
            if nums_dict[num] > 1:
                return num