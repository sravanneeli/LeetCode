class Solution:
    def calPoints(self, ops: List[str]) -> int:
        stck = []
        
        for char in ops:
            if char.isnumeric():
                stck.append(int(char))
            elif char[0] == '-':
                stck.append(-int(char[1:]))
            elif char == "+":
                stck.append(stck[-1] + stck[-2])
            elif char == "D":
                stck.append(stck[-1] * 2)
            elif char == "C":
                stck.pop()
            # print(stck)
        return sum(stck)