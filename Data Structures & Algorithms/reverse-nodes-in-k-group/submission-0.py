# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:

    def findKNode(self, head, k):
        temp = head
        while temp and k-1 > 0:
            k -= 1
            temp = temp.next
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
        
        temp = head
        prev_node, next_node = None, None

        while temp:
            kth_node = self.findKNode(temp, k)
            if not kth_node: break

            next_node = kth_node.next
            kth_node.next = None

            self.reverseList(temp)

            if head == temp:
                head = kth_node

            if prev_node: prev_node.next = kth_node
            prev_node = temp
            temp.next = next_node
            temp = temp.next  
        
        return head
