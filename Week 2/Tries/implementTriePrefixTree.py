"""
Procedure:
Using the Trie datastructure created in longestWordInDictionary.py
Search - After verifying every character is within children dictionary, it will return True
         if the leaf flag of that word is True, otherwise False.
StartsWith - Similar to search, but will return True only after verifying every character is
             in the children dictionary, otherwise False.

Complexity:
n -> length of the word to be added
Insert -> Time: O(n)
          Space: O(n)
Search -> Time: O(n)
          Space: O(1)
StartsWith -> Time: O(n)
              Space: O(1)
"""

class TrieNode:
    def __init__(self):
        self.children = {}
        self.leaf = False


class Trie:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = TrieNode()
        

    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        curNode = self.root
        for char in word:
            if char not in curNode.children:
                nextNode = TrieNode()
                curNode.children[char] = nextNode
                curNode = nextNode
                
            else:
                curNode = curNode.children[char]
                
        curNode.leaf = True
        

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        node = self.root
        for char in word:
            if char not in node.children:
                return False
            
            node = node.children[char]
            
        return node.leaf
        

    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        node = self.root
        for char in prefix:
            if char not in node.children:
                return False
            
            node = node.children[char]
            
        return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)