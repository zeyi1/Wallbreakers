"""
Procedure:
Loop through every cpdomain, split by white space to get the count and address, then split the address by dot to get every level.
Use a counter to have the address as the key and count as the value.
Use string join for every key value pair in the counter.

Complexity:
n -> length of input list, m -> length of each string in the list
Time: O(n * m)
Space: O(n * m)
"""

from collections import Counter

class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        if not cpdomains:
            return []
        
        d = Counter()
        
        for domain in cpdomains:
            num, address = domain.split(' ')
            address = address.split('.')
            for i in range(len(address)):
                tempAddress = '.'.join(address[i:])
                d[tempAddress] += int(num)
                
        result = [' '.join((str(value), address)) for address, value in d.items()]
        
        return result