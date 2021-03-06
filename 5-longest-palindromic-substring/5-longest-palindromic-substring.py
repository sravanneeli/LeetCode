class Solution:
    def longestPalindrome(self, s: str) -> str:
        res = ""
        n = len(s)
        for i in range(n):
            tmp = self.helper(s, i, i)
            if len(tmp) > len(res):
                res = tmp
            tmp = self.helper(s, i, i+1)
            if len(tmp) > len(res):
                res = tmp
        
        return res
    
    
    def helper(self, s, l, r):
        # print(l, r)
        while l >= 0 and r < len(s) and s[l] == s[r]:
            l -= 1
            r += 1
        
        return s[l+1:r]
        