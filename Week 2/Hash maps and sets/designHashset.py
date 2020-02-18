"""
Procedure:
Same idea as designHashmap.py.

Complexity:
Same for all methods.
"""

class Node:
    def __init__(self, val):
        self.val = val
        self.next = None
        

class MyHashSet:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.size = 1009
        self.hashset = [None] * self.size
        

    def add(self, key: int) -> None:
        index = key % self.size
        
        if not self.hashset[index]:
            node = Node(key)
            self.hashset[index] = node
            return
        
        if self.hashset[index].val == key:
            return 
        
        temp = self.hashset[index]
        while temp:
            if temp.val == key:
                return
            
            if not temp.next:
                node = Node(key)
                temp.next = node
                return
            
            temp = temp.next


    def remove(self, key: int) -> None:
        index = key % self.size
        
        if not self.hashset[index]:
            return
        
        if self.hashset[index].val == key:
            self.hashset[index] = self.hashset[index].next
            return
        
        temp = self.hashset[index]
        prev = Node(0)
        
        while temp:
            if temp.val == key:
                prev.next = temp.next
                return
            
            prev = temp
            temp = temp.next
            

    def contains(self, key: int) -> bool:
        """
        Returns true if this set contains the specified element
        """
        index = key % self.size
        
        if not self.hashset[index]:
            return False
        
        temp = self.hashset[index]
        
        while temp:
            if temp.val == key:
                return True
            
            temp = temp.next
            
        return False


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)