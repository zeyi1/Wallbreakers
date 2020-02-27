"""
Procedure:
We only need five and ten bills, as with twenties we cannot make change. 
If the bill is five, increase our five bills.
If the bill is ten, decrease a five bill and increase our ten bills.
If the bill is twenty, we can give change with 1 ten bill and 1 five bill
or with 3 five bills if we do not have a ten bill.
Since our five bills decrease with 10 or 20, we can just check if we have remaining five bills.

Complexity:
n -> length of input array
Time: O(n)
Space: O(1)
"""

class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        if not bills:
            return False
        
        if bills[0] in (10, 20):
            return False
        
        five, ten = 0, 0
        
        for bill in bills:
            if bill == 5:
                five += 1
                
            elif bill == 10:
                five, ten = five - 1, ten + 1
                
            elif ten > 0:
                ten, five = ten - 1, five - 1
                    
            else:
                five -= 3
            
            if five < 0:
                return False
                    
        return True