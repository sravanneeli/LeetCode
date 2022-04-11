class Solution:
    def calPoints(self, ops: List[str]) -> int:
        stck = []
        
        for char in ops:
            if char == "+":
                stck.append(stck[-1] + stck[-2])
            elif char == "D":
                stck.append(stck[-1] * 2)
            elif char == "C":
                stck.pop()
            else:
                stck.append(int(char))
            # print(stck)
        return sum(stck)