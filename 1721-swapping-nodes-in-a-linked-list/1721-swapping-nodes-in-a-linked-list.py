# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        n = 0
        
        temp = head
        
        while temp:
            n += 1
            temp = temp.next
        temp = head
        temp1 = head.val
        for i in range(k):
            temp1 = temp.val
            temp = temp.next
        temp = head
    
        for i in range(n-k+1):
            if i == (n-k):
                temp2 = temp.val
                temp.val = temp1
            temp = temp.next
        temp = head
        for i in range(k):
            if i == k-1:
                temp.val = temp2
            temp = temp.next
        return head