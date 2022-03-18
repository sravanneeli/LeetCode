class Solution:
    def reverse(self, x: int) -> int:
        ans = 0
        temp1 = temp2 = abs(x)
        prod = 1
        if x != abs(x):
            prod = -1
        while temp1:
            ans = ans * 10 + temp1 % 10
            temp1 //= 10
            
        if ans < 2**31:
            return prod * ans
        
        return 0
        