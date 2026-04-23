"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head: return None
        
        old_to_new = {}

        temp = head
        while temp:
            old_to_new[temp] = Node(temp.val)
            temp = temp.next
        
        temp = head
        while temp:
            node = old_to_new[temp]

            node.next = old_to_new[temp.next] if temp.next else None
            node.random = old_to_new[temp.random] if temp.random else None
            temp = temp.next
        
        return old_to_new[head]