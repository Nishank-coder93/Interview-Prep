"""
# Binary Heap tree (Using Lists instead of nodes and references)

* BinHeap() creates a new, empty, binary heap.
* insertMin(k) adds a new item to the heap.
* findMin() returns the item with the minimum key value, leaving item in the heap.
* delMin() returns the item with the minimum key value, removing the item from the heap.
* isEmpty() returns true if the heap is empty, false otherwise.
* size() returns the number of items in the heap.
* buildHeap(list) builds a new heap from a list of keys.

"""

class BinHeap: 
    # Initialization of Heap List
    # Value of 0 signifies empty and for integer division
    def __init__(self): 
        self.heaplist = [0] 
        self.currentSize = 0
    
    # To keep the property of min heap percolates upwards if child value is less than parent
    def percUpMin(self,i): 
        
        while i // 2 > 0: 
            if self.heaplist[i] < self.heaplist[i//2]: 
                self.heaplist[i],self.heaplist[i//2] = self.heaplist[i//2], self.heaplist[i]
            i = i//2
    # appends the element at the end of the list O(1) and percUp O(log(n)) if less than parent
    def insertMin(self,k):
        self.heaplist.append(k)
        self.currentSize += 1
        self.percUpMin(self.currentSize)
    
    # Perc Down and minChild funtion to help delete Min child from the heap
    def percDownMin(self,i):
        while (i * 2) <= self.currentSize:
            # To get the next Min of the two children 
            mc = self.minChild(i)
            if self.heapList[i] > self.heapList[mc]:
                self.heaplist[i],self.heaplist[mc] = self.heaplist[mc],self.heaplist[i]
            i = mc

    def minChild(self,i):
        # If we reach the last node
        if i * 2 + 1 > self.currentSize:
            return i * 2
        else:
            # Compare the two children and return the min value 
            if self.heapList[i*2] < self.heapList[i*2+1]:
                return i * 2
            else:
                return i * 2 + 1
    
    # main delete function to pop the O(log(n))
    def delMin(self): 
        val = self.heaplist[1]
        self.heaplist[1] = self.heaplist[self.currentSize]
        self.heaplist.pop()
        self.percDownMin(1)
        return val
    
    # We can build an entire heap from a list in O(n) running time
    def buildHeapMin(self,arr):
        # Half of the array size to keep the binary tree property intact
        i = len(arr) // 2
        self.currentSize = len(arr)
        self.heapList = [0] + arr[:]
        while (i > 0):
            self.percDown(i)
            i = i - 1