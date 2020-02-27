"""
Procedure:
Create a dictionary, character as keys and last index of that character as values.
Use three pointers, 
- left -> points at the beginning of the substring
- lastIndex -> points the position of max(left character's index, right character's index)
- right -> if any character within left - lastIndex has greater index than lastIndex, right will point to it
At each iteration, convert the substring into a set, and find the greatest index from all these characters
by using right and updating lastIndex accordingly, if all characters' index within the substring are lower than 
lastIndex, then we found the correct partition.

Complexity:
n -> length of input string
Time: O(n)
Space: O(n)     # if the slice is the entire string
"""

class Solution:
    def partitionLabels(self, S: str) -> List[int]:
        if len(S) == 1:
            return 1
        
        d = {}
        
        for index, char in enumerate(S):
            d[char] = index
            
        left, right = 0, 0
        result = []
        flag = False
        
        while left < len(S):
            lastIndex = max(d[S[left]], d[S[right]])
            temp = set(S[left:lastIndex+1])
            for char in temp:
                if d[char] > lastIndex:
                    right = d[char]
                    flag = True
                    break
                    
            if flag:
                flag = False
                continue
  
            result.append(lastIndex - left + 1)
            left = lastIndex + 1
            
        return result