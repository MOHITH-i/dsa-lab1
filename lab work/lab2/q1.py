class node:
    def __init__(self,data):
        self.data=data
        self.next=None
        
class linkedlist:
    def __init__(self):
        self.head=None
    
    def insertatbegin(self,data):
        newnode=node(data)
        if self.head is None:
            self.head=newnode
            return
        else:
            currentnode=self.head
            newnode.next=currentnode
            self.head=newnode
        
    def indsertatend(self,data):
        newnode=node(data)
        if self.head is None:
            self.head=newnode
        currentnode=self.head
        while(currentnode.next):
            currentnode=currentnode.next
        currentnode=newnode
        
    def removeatstart(self):
        if self.head is None:
            return
        self.head=self.head.next
    
    def removeatend(self):
        if self.head is None:
            return
        currentnode=self.head
        while(currentnode is not None and currentnode.next is not None):
            currentnode=currentnode.next 
        currentnode=None
        
    def traverse(self):
        currentnode=self.head
        while(currentnode):
            print(currentnode.data)
            currentnode.next
        print("end of linked list")
        
a=linkedlist()
a.insertatbegin(90)
a.indsertatend(10)
a.insertatbegin(80)
a.insertatbegin(50)
a.traverse()
