class Solution:
    def reverse(self, x: int) -> int:
        ans = 0
        temp = abs(x)
        prod = 1
        if x != temp:
            prod = -1
        while temp:
            ans = ans * 10 + temp % 10
            temp //= 10
            
        if ans < 2**31:
            return prod * ans
        
        return 0
        