class stack:
    def __init__(self,cap):
        self.cap=cap
        self.top=-1
        self.a=[0]*cap
        
    def push(self,data):
        if self.top>self.cap-1:
            print("overflow")
            return False
        self.top=self.top+1
        self.a[self.top]=data
        return True
    
    def pop(self):
        if self.top<-1:
            print("underflow")
            return 
        popped=self.a[self.top]
        self.top=self.top-1
        return popped
    
    def peek(self):
        print(self.a[self.top])
    
    def display(self):
        if self.top < 0:
            print("stack is empty")
            return
        for i in range(self.top, -1, -1):
            print(self.a[i], end=" ")
        print() 
    
s=stack(5)
s.push(10)
s.push(20)
s.push(40)
s.push(50)
s.pop()
s.display()