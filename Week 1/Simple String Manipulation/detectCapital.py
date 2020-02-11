"""
Procedure:
Check all 3 conditions by checking the first and second character, and find in which category the word belongs to. 
If none of them, then it is not capital used.
Based on the condition, check the remaining letters.

Complexity:
n -> length of word
Time: O(n)
Space: O(1)
"""

class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        length = len(word)
        if not word or length == 1:
            return True
        
        first, second = word[0], word[1]
        firstLetter, allCaps, allLower = False, False, False
        
        if first == first.upper() and second == second.upper():
            allCaps = True
        elif first == first.upper() and second == second.lower():
            firstLetter = True
        elif first == first.lower() and second == second.lower():
            allLower = True
        else:
            return False
        
        if length == 2:
            return firstLetter or allCaps or allLower
        
        for letter in word[2:]:
            if allCaps:
                if letter == letter.lower():
                    return False
            
            if firstLetter or allLower:
                if letter == letter.upper():
                    return False
        
        return True