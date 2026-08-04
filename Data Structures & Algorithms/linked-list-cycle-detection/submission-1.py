# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if head == None or head.next == None:
            return False
        
        seen = set()
        current = head.val
        while head.next != None:
            if current in seen:
                return True
            else:
                seen.add(current)
            head = head.next
            current = head.val
        
        return False