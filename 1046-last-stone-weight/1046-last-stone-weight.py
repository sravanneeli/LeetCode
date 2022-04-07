from bisect import bisect_left

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones.sort()
        
        while stones:
            s1 = stones.pop()
            if not stones:
                return s1
            s2 = stones.pop()
            
            if s1 > s2:
                stones.insert(bisect_left(stones, s1-s2), s1-s2)
                # print(stones)
        
        return 0