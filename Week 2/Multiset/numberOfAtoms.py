"""
Procedure:
A chemical element can be a single uppercase letter or a uppercase and a lowercase letter.
Start from the end of the string and traverse back.
Use a dictionary to keep the chemical element as the key and the count as the value.
Use a list to keep track of numbers that appear after a closing parenthesis, and a variable to count the number
of closing parenthesis we encounter, which will be used to access the elements in this list.

There are 3 cases:
    1. The current index is either uppercase or lowercase, in this case just add to the dictionary with value 1.
    2. The current index is a number and the following index is a letter, add to dictionary with value number.
       For numbers, need to keep traversing until the index does not point to a number.
    3. The current index is a number and the following index is a close parenthesis, in this case, we add the 
       current number to the list and increase the number of closing parenthesis by 1, keep looping until we find
       an open parenthesis and the number of close parenthesis is 0. And for each open parenthesis encountered,
       reduce the number of close parenthesis by one and remove the last number from the list because this number
       cannot longer be used. For every chemical element we find, we need to multiply by every number on the list.
       Repeat step 1,2,3 until the index gets to 0.

Complexity:
n -> length of input string
Time: O(nlogn)      // because of the sorting at the end
Space: O(n)
"""

from collections import defaultdict
import string

class Solution:
    def countOfAtoms(self, formula: str) -> str:
        uppercase = string.ascii_uppercase
        lowercase = string.ascii_lowercase
        numbers = '0123456789'        

        length = len(formula) - 1
        d = defaultdict(int)
        numClose = 0
        nums = []

        while length >= 0:
            if formula[length] in lowercase:
                element = formula[length-1:length+1]
                d[element] += 1
                length -= 2

            elif formula[length] in uppercase:
                d[formula[length]] += 1
                length -= 1

            elif formula[length] in numbers:
                temp = length
                length -= 1
                while formula[length] in numbers:
                    length -= 1

                curNum = int(formula[length+1:temp+1])

                if formula[length] in lowercase:
                    element = formula[length-1:length+1]
                    d[element] += curNum
                    length -= 2

                elif formula[length] in uppercase:
                    d[formula[length]] += curNum
                    length -= 1

                elif formula[length] == ')':
                    nums.append(curNum)
                    length -= 1
                    numClose += 1
                    while formula[length] != '(' or numClose > 0:
                        if formula[length] in numbers:
                            temp = length
                            length -= 1
                            while formula[length] in numbers:
                                length -= 1   

                            newNum = int(formula[length+1:temp+1])
                            if formula[length] != ')':
                                prod = 1
                                if formula[length] in uppercase:
                                    for i in range(numClose):
                                        prod *= nums[i]

                                    prod *= newNum
                                    d[formula[length]] += prod
                                    length -= 1

                                else:
                                    element = formula[length-1:length+1]
                                    for i in range(numClose):
                                        prod *= nums[i]

                                    prod *= newNum
                                    d[element] += prod
                                    length -= 2

                            else:    
                                nums.append(newNum)
                            
                            continue

                        if formula[length] == ')':
                            numClose += 1

                        elif formula[length] == '(':
                            numClose -= 1
                            del nums[len(nums)-1]
                            if numClose == 0:
                                length -= 1
                                break

                        elif formula[length] in uppercase:
                            prod = 1
                            for i in range(numClose):
                                prod *= nums[i]
                            d[formula[length]] += prod

                        elif formula[length] in lowercase:
                            element = formula[length-1:length+1]
                            prod = 1
                            for i in range(numClose):
                                prod *= nums[i]
                            d[element] += prod
                            length -= 1

                        length -= 1
                        
        result = ''.join(element+str(atoms) if atoms > 1 else element for element, atoms in sorted(d.items()))
        
        return result