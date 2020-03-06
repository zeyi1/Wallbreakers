"""
Procedure:
To solve in O(1) for both operations, we need a dictionary and a double linked list.
1)  Initialiaze a dictionary, and two nodes, one for the head and one for the tail. The head's next would be the tail and the tail's prev would be the head. 
    This is useful so that at each step when adding or deleting nodes, we do not need to check for null values.

2)  We need 2 helper functions, add and delete a node. 
    Add - Simply get the last node before the tail node (self.tail.prev), and assign the next of this node to be the node we going to add.
          Then the node to add's prev would be the node we got and the next would be tail.
          Tail's prev now becomes this new node.
          The last node will always be the most recently used and the first node will be the least recently used.
          
    Remove - Simply get the prev and next of the node we are going to remove as two new nodes, then assign the node.next = node2 and node2.prev = node

3)  The get function, our dictionary will have keys as integers and values as nodes that contain a key and a value.
    a) Check if the key we are getting is in the dictionary, if it is not just return -1
    b) If it is in the dictionary, we first get the node from that key. We remove it from wherever it was before and add it back so that it now becomes the most recently used
    
    
4)  The put function, 
    a) Need to check if the key is in the dictionary, if it is just remove it from the double linkedlist by retrieving it from the dictionary[key]. 
    b) Create the new node with the give key and value, and add it to the dictionary and the double linked list. 
    c) If adding this node goes over capacity, get the node after the head and remove it from the dictionary and the double linkedlist.

"""

class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.next, self.prev = None, None

        
class LRUCache:

    def __init__(self, capacity: int):
        self.d = {}
        self.capacity = capacity
        self.head, self.tail = Node(0, 0), Node(0, 0)
        self.head.next = self.tail
        self.tail.prev = self.head

        
    def get(self, key: int) -> int:
        if key in self.d:
            node = self.d[key]
            self.removeNode(node)
            self.addNode(node)
            return node.val
            
        return -1

    
    def put(self, key: int, value: int) -> None:
        if key in self.d:
            self.removeNode(self.d[key])
        
        node = Node(key, value)
        self.d[key] = node
        self.addNode(node)
        
        if len(self.d) > self.capacity:
            nodeToRemove = self.head.next
            self.removeNode(nodeToRemove)
            del self.d[nodeToRemove.key]
    
    
    def addNode(self, node):
        lastNode = self.tail.prev
        lastNode.next = node
        node.prev, node.next = lastNode, self.tail
        self.tail.prev = node
        
        
    def removeNode(self, node):
        previousNode, nextNode = node.prev, node.next
        previousNode.next = nextNode
        nextNode.prev = previousNode

        
# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)