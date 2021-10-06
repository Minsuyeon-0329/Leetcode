class MyCircularQueue:
    
    def __init__(self, k: int):
        self.queue = [None] * (k+1)
        self.head = 0
        self.tail = 0
        self.items = 0
        self.size = k+1
        
    def enQueue(self, value: int) -> bool:
        if self.items == self.size-1:
            return False
        
        self.queue[self.tail] = value
        self.tail = (self.tail + 1)%self.size
        self.items +=1
        return True
    
    def deQueue(self) -> bool:
        if self.head == self.tail:
            return False
        self.head = (self.head +1)%self.size
        self.items -= 1
        return True
    
    def Front(self) -> int:
        if self.head == self.tail:
            return -1
        else:
            return self.queue[self.head]
        
    def Rear(self) -> int:
        if self.head == self.tail:
            return -1
        else:
            return self.queue[self.tail -1]
        
    def isEmpty(self) -> bool:
        return self.head == self.tail
    
    def isFull(self) -> bool:
        return self.items == (self.size -1)
    


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()