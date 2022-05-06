class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        stck = []
        
        for char in s:
            if stck and stck[-1][0] == char:
                stck[-1][1] += 1
            else:
                stck.append([char, 1])
            # print(stck)
            if stck and stck[-1][1] == k:
                stck.pop()
        
        output = ""
        
        for char, count in stck:
            output += char*count
        
        return output
            
        