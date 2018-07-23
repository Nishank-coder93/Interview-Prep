class Queue():
    def __init__(self):
        self.__queue = []
        self.__size = 0
    
    def isEmpty(self):
        return self.size == 0
    
    def enqueue(self,item):
        self.__queue.insert(0,item)
    
    def dequeue(self):
        return self.__queue.pop()
        
    def size(self):
        return self.__size
    
    def printQueue(self):
        print(self.__queue[::-1])


if __name__== "__main__": 
    q = Queue()
    q.enqueue(3)
    q.enqueue(2)
    q.printQueue()
    q.enqueue(1)
    print(q.dequeue())
    print(q.isEmpty())
    print(q.size())
    q.printQueue()