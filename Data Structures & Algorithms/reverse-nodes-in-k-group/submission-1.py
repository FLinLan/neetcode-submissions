# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:

    def findKNode(self, head, k):
        temp = head

        while temp and k-1 > 0:
            temp = temp.next
            k -= 1
        return temp
    
    def reverseList(self, head):
        prev, curr = None, head

        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        
        return prev
    
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        """
        find the kth node of the list, if can't: break
        preserve next node of k, break k link 
        reverse the section of k length
        preserve previous node
        
        """

        temp = head
        prev_node = None
        while temp:
            kth_node = self.findKNode(temp, k)

            # kth node too small, break
            if not kth_node: break
            
            # ensure we're reversing our desired portion
            next_node = kth_node.next
            kth_node.next = None

            self.reverseList(temp)

            # start of the list, reassign head
            if temp == head:
                head = kth_node
            
            # reassigning pointers after reversing the portion
            if prev_node: prev_node.next = kth_node
            prev_node = temp
            temp.next = next_node
            temp = temp.next
        
        return head
