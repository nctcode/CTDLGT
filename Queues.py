class Empty(Exception):
    pass

class ArrayQueues:
    Default = 10
    def __init__(self):     
        self.size = 0
        self.front = 0
        self.data = [None]  * ArrayQueues.Default
    #do dai
    def __len__(self):
        return self.size
    # la rong
    def isEmpty(self):
        return self.size == 0
    # resize
    def resize(self, cap):
        old = self.data
        self.data = [None]*cap
        walk = self.front
        for k in range(self.size):
            self.data[k] = old[walk]
            walk = (1+walk)% len(old)
        self.front = 0
    # them 
    def enqueues(self,e):
        if self.size == len(self.data):
            self.resize(2*len(self.data))
        avail = (self.front + self.size) % len(self.data)
        self.data[avail] = e
        self.size += 1
    # xoa
    def dequeues(self):
        if self.isEmpty():
            raise Empty('Queues is empty')
        answer = self.data[self.front]
        self.data[self.front] = None
        self.front = (self.front + 1) % len(self.data)
        self.size -= 1

        if 0 < self.size < len(self.data) // 4:
            self.resize(len(self.data)//2)
        return answer
    # phan tu dau tien
    def first(self):
        if self.isEmpty():
            raise Empty('Stack is empty')
        return self.data[self.front]
    
Q = ArrayQueues()
Q.enqueues(1)
Q.enqueues(3)
Q.enqueues(4)
Q.enqueues(2)
print(len(Q))
print(Q.first())
print(Q.dequeues())
print(Q.isEmpty())
print(Q.dequeues())
print(len(Q))
print(Q.dequeues())
print(Q.dequeues())
print(Q.isEmpty())
print(len(Q))
    
    