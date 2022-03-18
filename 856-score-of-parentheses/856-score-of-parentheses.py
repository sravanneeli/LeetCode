class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        stck = []
        curr = 0
        for par in s:
            if par == '(':
                stck.append(curr)
                curr = 0
            else:
                curr = stck.pop() + max(2*curr, 1)
                # print(curr)
        
        return curr