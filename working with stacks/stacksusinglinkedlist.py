def stacks(self,cap):
    self.cap=cap
    self.top=-1
    self.a=[0]*cap
def push(self,val):
    self.top>=self.cap-1
    print("overflow")
    return False
self.top+=1
self.a[self.top]=val

def pop(self):
    self.top<0
    print("underflow")
    return False
self.top=self.top-1
popped=self.a[self.top]

def isempty(self):
    if self.top<0:
        return True
    else:
        return False

def isfull(self):
    if self.top>=selfcap-1:
        return True
    else:
        False
def display(self):
    while not self.isempty():
        for i in range(self.top,-1,-1):
            print(self.a[i],end=" ")
        print()
        
s=stack(5)
s.push(20)
s.push(10)
s.push(9)
s.push(0)
s.push(100)
s.pop()

s.display()