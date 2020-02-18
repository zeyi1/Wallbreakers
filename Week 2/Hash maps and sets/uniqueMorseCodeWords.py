"""
Solution 1

Procedure:
Use index to access each morse code, to get the correct index we subtract the ascii code of every letter by the ascii code of 'a'.
Use a set to maintain uniqueness, and add the corresponding morseCode of every word.
The length of the set will be the unique codes.

Complexity:
n -> number of words, m -> length of longest word, p -> length of morse code of a word
Time: O(n * m)
Space: O(n * p)
"""

class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        if not words:
            return 0
        
        morseCodes = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        
        a = ord('a')
        uniqueMorseCodes = set()
        
        for word in words:
            ls = []
            for letter in word:
                index = ord(letter) - a
                ls.append(morseCodes[index])
                
            uniqueMorseCodes.add(''.join(ls))
            
        return len(uniqueMorseCodes)



"""
Solution 2

Procedure:
Same logic, but instead of using index, create a dictionary and retrieve the codes from it.

Complexity:
Same
"""

import string

class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        if not words:
            return 0
        
        lowerCase = string.ascii_lowercase
        morseCodes = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        
        
        encoding = dict(zip(lowerCase, morseCodes))
        uniqueMorseCodes = set()
        
        for word in words:
            ls = []
            for letter in word:
                ls.append(encoding[letter])
                
            uniqueMorseCodes.add(''.join(ls))
            
        return len(uniqueMorseCodes)