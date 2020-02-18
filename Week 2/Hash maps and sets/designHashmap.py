"""
Procedure:
Use a list for fast access using index. To get the index, use (key value) % length of the list. The length of the list
is recommended to be a prime number to avoid less collitions.
For collision handling, use linkedlist nodes.

Complexity:
n -> number of nodes in the linked list.
Put ->    Time: O(n) if there are many collisions
Get ->    Time: O(n) if there are many collisions
Remove -> Time: O(n) if there are many collisions
"""

class Node:
    def __init__(self, key, val):
        self.data = (key, val)
        self.next = None
        
        
class MyHashMap:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.size = 1009
        self.hashmap = [None] * self.size
        

    def put(self, key: int, value: int) -> None:
        """
        value will always be non-negative.
        """
        index = key % self.size
        if self.hashmap[index]:
            temp = self.hashmap[index]
            
            while temp:
                if temp.data[0] == key:
                    temp.data = (key, value)
                    return
                
                if not temp.next:
                    node = Node(key, value)
                    temp.next = node
                    return
                
                temp = temp.next
            
        else:
            node = Node(key, value)
            self.hashmap[index] = node

            
    def get(self, key: int) -> int:
        """
        Returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key
        """

        index = key % self.size
        if not self.hashmap[index]:
            return -1
        
        temp = self.hashmap[index]
        
        while temp:
            print(temp.data[0])
            if temp.data[0] == key:
                return temp.data[1]
            
            if not temp.next:
                return -1
            
            temp = temp.next
            

    def remove(self, key: int) -> None:
        """
        Removes the mapping of the specified value key if this map contains a mapping for the key
        """
        index = key % self.size
        if not self.hashmap[index]:
            return 
        
        if self.hashmap[index].data[0] == key:
            self.hashmap[index] = self.hashmap[index].next
            return
        
        temp = self.hashmap[index]
        prev = Node(0, 0)
        
        while temp:
            if temp.data[0] == key:
                prev.next = temp.next
                return
                
            prev = temp
            temp = temp.next
            
        return


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)