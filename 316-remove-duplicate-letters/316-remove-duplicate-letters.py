class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        lst_idx_dict = {}
        for idx, char in enumerate(s):
            lst_idx_dict[char] = idx
        
        # print(lst_idx_dict)
        ans = []
        for idx, char in enumerate(s):
            # print(ans)
            if char not in ans:
                while ans and char < ans[-1] and idx < lst_idx_dict[ans[-1]]:
                    ans.pop()
                ans.append(char)
        return "".join(ans)