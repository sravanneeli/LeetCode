class Solution:
    def minDominoRotations(self, tops: List[int], bottoms: List[int]) -> int:
        ans = float('inf')
        for i in range(1, 7):
            count = 0
            for top, bottom in zip(tops, bottoms):
                if top == i:
                    continue
                if bottom != i:
                    count = float('inf')
                    break
                count += 1
            ans = min(ans, count)
            # print(ans)
            
        for i in range(1, 7):
            count = 0
            for bottom, top in zip(bottoms, tops):
                if bottom == i:
                    continue
                if top != i:
                    count = float('inf')
                    break
                count += 1
            ans = min(ans, count)
        
        return ans if ans != float('inf') else -1
                    