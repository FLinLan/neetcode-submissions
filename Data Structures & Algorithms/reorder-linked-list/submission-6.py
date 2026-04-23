# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def splitListFromMiddle(self, head):
        temp, slow, fast = head, head, head 
        while fast and fast.next:
            temp = slow
            slow = slow.next
            fast = fast.next.next
        temp.next = None

        return head, slow # first half, second half
    
    def reverseList(self, head):
        prev, curr = None, head
        
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        
        return prev
    
    def mergeTwoList(self, list1, list2):
        ans = ListNode() # dummy node to avoid edge cases
        l1, l2, temp = list1, list2, ans
        alternateFlag = True

        # merge two lists starting with list1
        while l1 and l2:
            if alternateFlag:
                temp.next = l1
                l1 = l1.next
                temp = temp.next
                alternateFlag = False
            else:
                temp.next = l2
                l2 = l2.next
                temp = temp.next
                alternateFlag = True
        
        while l1:
            temp.next = l1
            l1 = l1.next
            temp = temp.next
        
        while l2:
            temp.next = l2
            l2 = l2.next
            temp = temp.next
        
        return ans.next # remove dummy node

    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head or not head.next: return

        l1, l2 = self.splitListFromMiddle(head)

        l2 = self.reverseList(l2)
        
        head = self.mergeTwoList(l1, l2)
