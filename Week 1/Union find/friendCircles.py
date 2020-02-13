"""
Solution 1

Procedure:
Students are represented as rows and students' friends are the column values that are 1 in that row.
Loop through all students, for each use DFS on the friends, and add all these friends as visited, 
so that when we reach a new student that is not friends with the previous ones, we can get a new circle.

Complexity:
m -> number of rows, n -> number of elements in each row
Time: O(m * n)
Space: O(n)
"""

class Solution:
    def findCircleNum(self, M: List[List[int]]) -> int:
        if not M or len(M[0]) == 0:
            return 0
        
        rowNum, friendCircles = len(M), 0
        visited, stack = set(), []
        
        for i in range(rowNum):
            if i not in visited:
                stack.append(i)
                
                while stack:
                    curStudent = stack.pop()
                    if curStudent not in visited:
                        visited.add(curStudent)
                        for j, val in enumerate(M[curStudent]):
                            if val == 1 and j not in visited:
                                stack.append(j)
                                
                friendCircles += 1
                
        return friendCircles



"""
Solution 2

Procedure:
Implement UnionFind object, and initialize it with the number of students.
For each student (row index), check the friendship with other students (cols indexes in the row).
If the value of other students is 1, check if they already belong to the same set, if not then unite them.
The count from the unionfind object will be number of distinct sets.

Complexity:
m -> number of rows, n -> number of columns in the row
Time: O(n * m)
Space: O(m)
"""

class UnionFind:
    def __init__(self, numSize):
        """
        parents list -> index represent the actual element, and index's value represent the parent of that element.
        Initially every element is a singleton that points to itself.
        size list -> number of elements that are in the set at a particular index.
        Since every element is a singleton, then initialize them as size 1.
        count -> counts the total number of sets in the object.
        """
        self.parents = [i for i in range(numSize)]      
        self.size = [1 for _ in range(numSize)]
        self.count = numSize
    
    
    def findRoot(self, num):
        """
        Returns the root element of the current element.
        Since we started with singletons, the condition to reach the root element will be if parents[element] == element is True.
        """
        while self.parents[num] != num:
            self.parents[num] = self.parents[self.parents[num]]
            num = self.parents[num]
            
        return num
    
    
    def union(self, x, y):
        """
        Unite two sets together. Need to first find the root of both elements we trying to unite.
        If both roots are the same, both elements are already in the same set, so we do not need to do anything.
        Compare the size of both sets by checking the size[root] since the index of the roots will always contain the current sets' size.
        Set the smaller set to point to the bigger set, parents[smallerSet] = parents[biggerSet].
        Add the smaller set size into the bigger set size, and set the smaller set size to 0.
        Reduce the count by one.
        """
        rootX, rootY = self.findRoot(x), self.findRoot(y)
        if rootX == rootY:
            return
        
        if self.size[rootX] < self.size[rootY]:
            self.parents[rootX] = self.parents[rootY]
            self.size[rootY] += self.size[rootX]
            self.size[rootX] = 0
            
        else:
            self.parents[rootY] = self.parents[rootX]
            self.size[rootX] += self.size[rootY]
            self.size[rootY] = 0
            
        self.count -= 1
            
            
    def find(self, x, y):
        """
        Returns True if the parents are the same, useful because it tells us when we need to call union.
        findRoot takes care of cases when an element is an indirect child, when the parents may be different,
        but the grandparent is the same.
        """
        if self.parents[x] == self.parents[y]:
            return True
        
        return False
    
    
    def getSetsCount(self):
        """
        Returns the sets count.
        """
        return self.count
    

class Solution:
    def findCircleNum(self, M: List[List[int]]) -> int:
        if not M or len(M[0]) == 0:
            return 0
        
        friends, rowNum = 0, len(M)
        uf = UnionFind(rowNum)
        
        for student, friendships in enumerate(M):
            for others, friendship in enumerate(friendships):
                if friendship == 1 and not uf.find(student, others):
                    uf.union(student, others)
        
        return uf.getSetsCount()