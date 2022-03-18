class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        sum_dict = {}
        for idx, num in enumerate(nums):
            temp = target - num
            if sum_dict.get(temp) is not None:
                return [sum_dict.get(temp)-1, idx]
        
            sum_dict[num] = idx+1
        