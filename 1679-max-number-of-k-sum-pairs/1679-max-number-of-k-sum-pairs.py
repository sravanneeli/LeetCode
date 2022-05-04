class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        freq_dict = {}
        op = 0
        for num in nums:
            res = k - num
            if freq_dict.get(res) is not None:
                op += 1
                if freq_dict.get(res) == 1:
                    freq_dict.pop(res)
                else:
                    freq_dict[res] -= 1
            else:
                freq_dict[num] = freq_dict.get(num, 0) + 1
        
        return op
        