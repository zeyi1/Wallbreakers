"""
Procedure:
Replace all punctuations with whitespaces, then convert to lower and split by any number of whitespaces.
Use a dictionary as a counter, and keep track of the highest count along with its character.

Complexity:
n -> length of paragraph
Time: O(n)
Space: O(n)
"""

class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        punctuation = "!?',;."
        banned = set(banned)

        for p in punctuation:
            paragraph = paragraph.replace(p, " ")
            
        d = {}
        result, count = "", 0

        for word in paragraph.lower().split():
            if word not in banned:
                if word not in d:
                    d[word] = 1
                else:
                    d[word] += 1
                
                if d[word] > count:
                    count = d[word]
                    result = word
        
        return result