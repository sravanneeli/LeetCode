class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        m, n = len(mat), len(mat[0])
        arr = []
        for i in range(m):
            arr.append((i, sum(mat[i])))
        
        print(arr)
        arr.sort(key = lambda x: x[1])
        print(arr)
        ans = []
        for tup in arr:
            ans.append(tup[0])
        return ans[:k]