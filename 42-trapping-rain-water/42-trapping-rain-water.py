class Solution:
    def trap(self, height: List[int]) -> int:
        left_max = [height[-1]]
        n = len(height)
        for i in range(n-2, -1, -1):
            temp = max(left_max[0], height[i])
            left_max.insert(0, temp)
        
        right_max = [height[0]]
        for i in range(1, n):
            temp = max(right_max[-1], height[i])
            right_max.append(temp)
        # print(left_max)
        # print(right_max)
        ans = 0
        
        for i, h in enumerate(height):
            ans += min(left_max[i], right_max[i]) - h
        # print(ans)
        
        return ans
            
        