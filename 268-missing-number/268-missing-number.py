class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        pres_dict = {}
        for num in nums:
            pres_dict[num] = True
        for i in range(n+1):
            if pres_dict.get(i) is None:
                return i
                