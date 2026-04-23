# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:

        
        ans = ListNode()
        temp = ans
        carry = 0

        # check if carry != 0 or edge cases
        while l1 or l2 or carry != 0:
            # find sum of ones place if possible
            v1 = l1.val if l1 else 0
            v2 = l2.val if l2 else 0

            # commpute for next carry and ones place
            val = v1 + v2 + carry
            ones, tens = val % 10, val // 10 

            carry = tens
            temp.next = ListNode(ones) # value at ones place

            # progress pointers if possible
            temp = temp.next
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
        
        return ans.next
        