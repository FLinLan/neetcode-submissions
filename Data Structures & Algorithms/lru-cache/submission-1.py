class Node:
    def __init__(self, key=0, value=0, prev=None, next=None):
        self.key = key
        self.value = value
        self.prev = prev
        self.next = next
    
class LRUCache:

    def __init__(self, capacity: int):
        self.cache = {} # {key : Node}
        self.capacity = capacity

        # dummy nodes to prevent edge cases
        self.head, self.tail = Node(), Node()
        self.head.next = self.tail
        self.tail.prev = self.head

    def delete(self, node):
        front, back = node.prev, node.next
        front.next = back
        back.prev = front
    
    def insertFront(self, node):
        temp = self.head.next
        self.head.next = node
        temp.prev = node
        node.next = temp
        node.prev = self.head

    def get(self, key: int) -> int:
        if key not in self.cache: return -1

        node = self.cache[key]
        self.delete(node)
        self.insertFront(node) # most recently used
        
        return node.value

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            old_node = self.cache[key]
            self.delete(old_node)
        
        node = Node(key, value)
        self.cache[key] = node
        self.insertFront(node)
        
        if len(self.cache) > self.capacity:
            lru_node = self.tail.prev
            self.delete(lru_node)
            del self.cache[lru_node.key]
        
        return
        