# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]):
        prev, curr = None, head
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        return prev
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        reversed_list = self.reverseList(head)
        ans = ListNode()
        ans.next = reversed_list
        temp = ans
        for _ in range(n-1):
            temp = temp.next
        temp.next = temp.next.next

        return self.reverseList(ans.next)

        