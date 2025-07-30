class node:
    def __init__(self,data):
        self.data=data
        self.next=None

class stack:
    def __init__(self):
        self.head=None
        
    def push(self,value):
        newnode=node(value)
        if self.head is None:
            self.head=newnode
        else:
            newnode.next=self.head
            self.head=newnode
            
    def pop(self):
        if self.head is None:
            print("empty")
        else:
            self.head=self.head.next
    
    
    def isempty(self):
        return self.head is None
    
    def peek(self):
        if self.head is None:
            print("it is emoty")
        else:
            print(self.head.data)
            
    def display(self):
        surrentnode=self.head
        while(surrentnode):
            print(surrentnode.data)
            surrentnode=surrentnode.next
        print("ennd of the list")
        
        
        

s=stack()
s.push(10)
s.push(20)
s.push(30)
s.push(40)
s.pop()
s.peek() 
s.display()
