class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        found = False
        n = len(nums)
        for i in range(n-2, -1, -1):
            if nums[i] < nums[i+1]:
                found = True
                break
        
        def get_next_max(arr, start, end, curr):
            min_val = float('inf')
            next_max_idx = 0
            for i in range(start, end):
                if arr[i] > curr and min_val >= arr[i]:
                    min_val = arr[i]
                    next_max_idx = i
            
            return next_max_idx
                    
        print(found)
        if found:
            m = get_next_max(nums, i+1, n, nums[i])
            nums[m], nums[i] = nums[i], nums[m]
            nums[i+1:] = nums[i+1:][::-1]
            # print(m)
            return nums
        else:
            i = 0
            j = n-1
            while i < j:
                nums[i], nums[j] = nums[j], nums[i]
                i += 1
                j -= 1
            return nums
            