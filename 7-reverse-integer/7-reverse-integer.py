class Solution:
    def reverse(self, x: int) -> int:
        ans = 0
        flag = 1
        if x < 0:
            flag = -1
            x = abs(x)
            
        while x > 0:
            digit = x % 10
            ans = ans * 10 + digit
            x //= 10
            
        if ans > (2**31 - 1) or ans < -1 * 2**31:
            return 0
        
        return flag * ans
        