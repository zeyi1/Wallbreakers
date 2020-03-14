"""
Procedure:
Use a set to capture all characters, and a dictionary of lists consisting of key as character
and value as the precedence characters. To achieve this, loop every 2 words, and the first
mismatch will represent the character at the first word has higher precedence.
Add all keys from the dictionary to our result list and at the same time delete them from the
set, the remaining characters in the set will be the lowest precedence, so add all of them to
the result list.

Complexity:
n -> number of words, m -> length of each word
Time: O(n*m)
Space: O(n*m)
"""

from collections import defaultdict

def findPrecedenceCharacters(words, numChars):
    if numChars == 0 or len(words) == 0:
        return []
    
    graph = defaultdict(list)
    seen, result = set(), []
    
    for i in range(numChars):
        seen.add(chr(i + ord('a')))
        
    for i in range(len(words) - 1):
        curWord = words[i]
        nextWord = words[i+1]
        for c1, c2 in zip(curWord, nextWord):
            if c1 != c2:
                graph[c1].append(c2)
                break
    
    for key in graph:
        result.append(key)
        seen.remove(key)
    
    for char in seen:
        result.append(char)
        
        
    return result


testSuite = [(["baa", "abcd", "abca", "cab", "cad"], 4), (["caa", "aaa", "aab"], 3)]

for test in testSuite:
    print(findPrecedenceCharacters(test[0], test[1]))