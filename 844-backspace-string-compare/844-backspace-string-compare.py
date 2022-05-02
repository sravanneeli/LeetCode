class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        lst1, lst2 = [], []
        
        for char in s:
            if char == '#':
                if lst1:
                    lst1.pop()
            else:
                lst1.append(char)
        
        for char in t:
            if char == '#':
                if lst2:
                    lst2.pop()
            else:
                lst2.append(char)
        
        if "".join(lst1) == "".join(lst2):
            return True
        return False
        