class Solution:
    def isPalindrome(self, x: int) -> bool:
        ans = 0
        temp1 = temp2 = abs(x)
        while temp1 > 0:
            ans = ans * 10 + temp1 % 10
            temp1 //= 10
            
        if ans == x:
            return True
        return False
        