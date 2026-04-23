# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def splitList(self, head):
        temp, fast, slow = head, head, head
        while fast and fast.next:
            temp = slow
            slow = slow.next
            fast = fast.next.next
        
        temp.next = None
        return head, slow # left, right
    
    def reverseList(self, head):
        prev, curr = None, head

        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        
        return prev # reversed list
    
    def mergeTwoList(self, list1, list2):
        ans = ListNode()
        temp, l1, l2 = ans, list1, list2

        first_turn = True # alternate between two lists
        while l1 and l2:
            if first_turn:
                temp.next = l1
                l1 = l1.next
                temp = temp.next
                first_turn = False
            else:
                temp.next = l2
                l2 = l2.next
                temp = temp.next
                first_turn = True
        
        # add remaining list if exists
        while l1:
            temp.next = l1
            l1 = l1.next
            temp = temp.next
        
        # add remaining list if exists
        while l2:
            temp.next = l2
            l2 = l2.next
            temp = temp.next
        
        return ans.next # remove the dummy node
        
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head or not head.next: return
        
        # split list evenly into first half and second hafl
        l1, l2 = self.splitList(head) 
        
        # reverse the second part of the list
        l2 = self.reverseList(l2)

        # merged the reversed list and the first list
        head = self.mergeTwoList(l1, l2)
