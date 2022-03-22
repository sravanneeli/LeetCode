class Solution:
    def getSmallestString(self, n: int, k: int) -> str:
        ans = ""
        num_arr = [chr(i+97) for i in range(0, 26)]
        
        for i in range(n, 0, -1):
            temp = k - (i - 1)
            # print(temp)
            if temp >= 26:
                ans = num_arr[25] + ans
                k -= 26
            else:
                ans = num_arr[temp-1] + ans
                k -= temp
                
        return ans