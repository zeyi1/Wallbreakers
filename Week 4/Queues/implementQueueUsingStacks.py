"""
Procedure:
Use two stacks, instack will contain new elements that will be pushed.
outstack will be used for peek and pop, append all elements from instack
to outstack using pop if outstack is empty.

"""

class MyQueue:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.inStack, self.outStack = [], []
        

    def push(self, x: int) -> None:
        """
        Push element x to the back of queue.
        """
        self.inStack.append(x)
        

    def pop(self) -> int:
        """
        Removes the element from in front of queue and returns that element.
        """
        self.peek()
        return self.outStack.pop()
        

    def peek(self) -> int:
        """
        Get the front element.
        """
        if not self.outStack:
            while self.inStack:
                self.outStack.append(self.inStack.pop())
                
        return self.outStack[len(self.outStack) - 1]
        

    def empty(self) -> bool:
        """
        Returns whether the queue is empty.
        """
        return len(self.inStack or self.outStack) == 0


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()