# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None

        currNode = head
        prevNode = None

        while currNode:
            nextNode = currNode.next
            currNode.next = prevNode #reverse pointer
            prevNode = currNode
            currNode = nextNode
        return prevNode

        

        