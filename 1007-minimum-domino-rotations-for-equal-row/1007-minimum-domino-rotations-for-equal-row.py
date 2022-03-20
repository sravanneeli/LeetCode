class Solution:
    def minDominoRotations(self, tops: List[int], bottoms: List[int]) -> int:
        tops_dict = {i: 0 for i in range(1, 7)}
        bottoms_dict = {i: 0 for i in range(1, 7)}
        same_dict = {i:0 for i in range(1, 7)}
        for top, bottom in zip(tops, bottoms):
            tops_dict[top] += 1    
            bottoms_dict[bottom] += 1
            if top == bottom:
                same_dict[top] += 1
            
        # print(same_dict)
        n = len(tops)
        for i in range(1, 7):
            if tops_dict[i] + bottoms_dict[i] - same_dict[i] == n:
                return n - max(tops_dict[i], bottoms_dict[i])
        return -1