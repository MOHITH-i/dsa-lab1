class node:
    def __init__(self,data):
        self.data=data
        self.next=None
        
class queue:
    def __init__(self):
        self.top=self.rare=None
    
    def isempty(self):
        if self.top is None:
            return True
        else:
            return False
        
    def printqueue(self):
        currentnode=self.top
        queuestring="current queue"
        while currentnode is not None:
            queuestring+="->"+str(currentnode.data)
            currentnode=currentnode.next
            print(queuestring)
    
    
    def enqueue(self,data):
        newnode=node(data)
        if self.isempty():
            self.top=self.rare=newnode
            self.printqueue()
        else:
            self.rare.next=newnode
            self.rare=newnode
            self.printqueue()
            
    def dequeue(self):
        currentnode=self.top
        self.top=self.top.next
        del currentnode
        self.printqueue()
        
q=queue()
q.enqueue(15)
q.enqueue(20)
q.printqueue()
q.dequeue(15)
q.printqueue()