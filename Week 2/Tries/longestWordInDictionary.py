"""
Solution 1 - Using sets

Procedure:
Sort the list by length and then alphabetically, and add all length 1 strings into a set.
For each word check if the substring without the last character is in the set, if it is, 
update the result to be the current string.
If the length of the current string is equal to our result, just add it into the set
without updating the result, since we want the string with smallest lexicographical order.
For early termination, check if the length of the current string is larger by 2.

Complexity:
n -> length of input list, m -> length of longest string
Time: O(n * m)        // because for every string, we getting a slice (O(m))
Space: O(max(n, m))
"""

class Solution:
    def longestWord(self, words: List[str]) -> str:
        sortedWords = sorted(words, key=lambda x: (len(x), x))      # Same as just sorted(words), python 
        if len(sortedWords[0]) != 1:
            return ""
        
        seen = set()
        result = sortedWords[0]
        maxLength = 0

        for word in sortedWords:
            if len(word) == 1:
                seen.add(word)
                maxLength = 1
                continue
                
            if len(word) - maxLength > 1:
                break
            
            if word[:-1] in seen:
                if maxLength == len(word):
                    seen.add(word)
                    continue
                    
                result = word
                seen.add(word)
                maxLength = len(word)
                
        return result



"""
Solution 2 - Creating and using a Trie datastructure

Procedure:
A trie consists of various trie nodes, each trie node has 
    - Children: a dictionary containing other trie nodes
    - Leaf: a flag indicating the end of the word or if a trie contains the word
    - Word: the word itself
Inserting into a trie, for each new word we start at the root, loop every character, if the character is not
in the children dictionary, create the character as a key and assign it a new trie node, advance the root to be
this character.
Once a word is completely added, leaf becomes True and the root node's word becomes word.

Add all the words into the trie, and perform BFS to retrieve the longest word that can be created.
The longest word can be identified if all prefixes up to length 1 have the leaf flag as True.

Complexity:
n -> number of words, m -> average length of the words
Time: O(n * m)
Space: O(n * m)
"""

from collections import deque

class TrieNode:
    def __init__(self):
        self.children = {}
        self.leaf = False
        self.word = ''
        
        
class Trie:
    def __init__(self):
        self.root = TrieNode()
        
        
    def insert(self, word):
        node = self.root
        
        for char in word:
            if char not in node.children:
                nextNode = TrieNode()
                node.children[char] = nextNode
                node = nextNode
                
            else:
                node = node.children[char]
                
        node.leaf = True
        node.word = word
                
                
    def BFS(self):
        queue = deque([self.root])
        longestWord = ''
        
        while queue:
            curNode = queue.popleft()
            
            for child in curNode.children.values():       
                if child.leaf:
                    queue.append(child)
                    if len(longestWord) < len(child.word) or child.word < longestWord:
                        longestWord = child.word
            
        return longestWord
                
        
class Solution:
    def longestWord(self, words: List[str]) -> str:
        root = Trie()
        
        for word in words:
            root.insert(word)
                
        return root.BFS()