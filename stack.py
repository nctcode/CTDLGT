class Empty(Exception):
    pass

class ArrayStack:
    def __init__(self):
        self.data = []
    #len
    def isEmpty(self):
        return len(self.data) == 0
    #them
    def push(self,e):
        self.data.append(e)
    #lay phan tu dinh
    def top(self):
        if self.isEmpty():
            raise Empty('Stack is Empty')
        return self.data[-1]
    #xoa 
    def pop(self):
        if self.isEmpty():
            raise Empty('Stack is Empty')
        return self.data.pop()
    # do dai 
    def __len__(self):
        return len(self.data)
    
S = ArrayStack()
S.push(1)
S.push(3)
print(S.top())
print(S.pop())
print(len(S))
   