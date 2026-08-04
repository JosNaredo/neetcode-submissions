# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def add_beafore(node: Optional[ListNode], head2: Optional[ListNode]) -> Optional[ListNode]:
            if node == None:
                return None
            temp = ListNode(node.val)
            temp.next = head2
            head2 = temp

            return head2
        
        if head == None:
            return None
        
        if head.next == None:
            return head
        
        current = head
        dummy = ListNode(head.val)
        dummy.next = None

        while current.next != None:
            current = current.next
            dummy = add_beafore(current, dummy)


        return dummy