class Stack:
    def __init__(self,cap):
        self.cap=cap
        self.top=-1
        self.a=[0]*cap
        
    def isempty(self):
        return self.top<0
    
    def push(self,data):
        if self.top>=self.cap-1:
            print("overflow")
            return False
        self.top+=1
        self.a[self.top]=data
        return True
    
    def pop(self):
        if self.top<0:
            print("underflow")
            return False
        popped=self.a[self.top]
        self.top-=1
        return popped
    
    def display(self):
        if not self.isempty():
            for i in range(self.top,-1,-1):
                print(self.a[i],end=" ")
        else:
            print("empty")
            
s=Stack(5)
s.push(10)
s.push(20)
s.push(30)
s.push(140)
s.push(104)
s.pop()
s.display()