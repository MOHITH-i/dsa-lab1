class queue:
    def __init__(self):
        self.a=[]
    
    def enqueue(self,value):
        self.a.append(value)
    
    def dequeue(self):
        self.a.pop(0)
        
    def is_empty(self):
        return len(self.a)==0
    def display(self):
        print(' '.join(map(str,self.a)))
    
if __name__ =="__main__":
    a=queue()
    a.enqueue(10)
    a.enqueue(20)
    a.enqueue(40)
    a.dequeue()
    a.display()