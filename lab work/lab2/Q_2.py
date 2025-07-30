class node:
    def __init__(self,data):
        self.data=data
        self.next=None

class stack:
    def __init__(self,cap):
        self.cap=cap
        self.top=-1
        self.a=[0]*cap
        
    def push(self,value):
        if self.top>self.cap-1:
            print("overfloew")
            return False
        self.top=self.top+1
        self.a[self.top]=value
        return True
    def pop(self):
        if self.top<0:
            print("underflow")
            return False
        popped=self.a[self.top]
        self.top=self.top-1
        return popped
    def peek(self):
        if self.top<0:
            print("empty")
            return
        print(self.a[self.top])
        
    def isempty(self):
        if self.top<0:
            return True
        else:
            return False
    def display(self):
        if self.top < 0:
            print("Stack is empty")
            return
        for i in range(self.top, -1, -1):
            print(self.a[i], end=" ")
        print()       

s=stack(5)
s.push(10)
s.push(20)
s.push(30)
s.push(40)
s.pop()
s.peek() 
s.display()
