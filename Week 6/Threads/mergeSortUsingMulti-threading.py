"""
This multithreaded mergesort returns a new array, and a queue is used to store these lists.

Complexity:
n -> length of input array
Time: O(nlogn)
Space: O(nlogn)
"""

import threading
import time
import random
import math
from queue import Queue


def mergeSort(arr):
    # Base case when there is only one element, means it is already sorted
    if len(arr) <= 1:
        return arr
    
    mid = len(arr) // 2
    # Recursively split the list in two halves until it reaches the base case
    leftArr, rightArr = mergeSort(arr[:mid]), mergeSort(arr[mid:])
    
    return merge(leftArr, rightArr)


def merge(leftArr, rightArr):
    
    result = []
    leftPtr, rightPtr = 0, 0
    # Combines the two slices into a sorted list
    while leftPtr < len(leftArr) and rightPtr < len(rightArr):
        if leftArr[leftPtr] < rightArr[rightPtr]:
            result.append(leftArr[leftPtr])
            leftPtr += 1
            
        else:
            result.append(rightArr[rightPtr])
            rightPtr += 1

    # Get the rest of missing elements        
    result += leftArr[leftPtr:]
    result += rightArr[rightPtr:]
    
    return result


if __name__ == '__main__':
    
    a = [random.randrange(1, 1000000, 1) for i in range(1000000)]

    startTime = time.time()

    numOfThreads = 4
    size = int(math.ceil(len(a) / numOfThreads))    # size of each slice
    left, right = 0, size

    queue = Queue()
    threadList = []
    
    
    # Use 4 threads to sort each slice
    for _ in range(numOfThreads):
        subarray = a[left:right]
        t = threading.Thread(target=lambda f, arg1: queue.put(mergeSort(arg1)), args=(queue, subarray))
        t.start()
        threadList.append(t)
        left, right = right, right + size

    for thread in threadList:
        thread.join()

    remainingLists = []
    while not queue.empty():
        list1, list2 = queue.get(), queue.get()
        remainingLists.append(merge(list1, list2))

    mergedList = merge(remainingLists[0], remainingLists[1])
    
    endTime = time.time()
    
    print(f'Run in {endTime - startTime} seconds.')


