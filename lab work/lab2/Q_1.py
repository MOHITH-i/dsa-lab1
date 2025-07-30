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
        
    def insertatend(self,data):
        newnode=node(data)
        if self.head is None:
            self.head=newnode
            return
        currentnode=self.head
        while(currentnode.next):
            currentnode=currentnode.next
        currentnode.next=newnode
        
    def removeatstart(self):
        if self.head is None:
            return
        self.head=self.head.next
    
    def removeatend(self):
        if self.head is None:
            return
        currentnode=self.head
        while(currentnode.next is not None and currentnode.next.next is not None):
            currentnode=currentnode.next 
        currentnode.next=None
        
    def traverse(self):
        currentnode=self.head
        while(currentnode):
            print(currentnode.data,end="\n")
            currentnode=currentnode.next
        print("end of linked list")
    
    
    def insertatindex(self,index,value):
        if index==0:
            self.head.data=value
            return
        currentnode=self.head
        position=0
        while(currentnode!=0 and position+1!=index):
            position=position+1
            currentnode=currentnode.next
            
            if(currentnode is not None):
                newnode=node(value)
                newnode.next=currentnode.next
                currentnode.next=newnode
                
    def update(self,index,value):
        currentnode=self.head
        position=0
        if position==index:
            self.head.data=value
        while(currentnode!=0 and index!=position):
            position=position+1
            currentnode=currentnode.next
        if currentnode!=None:
            currentnode.data=value
        else:
            print("index not found")
    
    
    def removeatindex(self,index):
        currentnode=self.head
        position=0
        if index==position:
            self.head=None
        while(currentnode is not None and currentnode.next!=None and position<index-1):
            position=position+1
            currentnode=currentnode.next
        if currentnode is None or currentnode.next is None:
            print("index not found")
        else:
            currentnode.next=currentnode.next.next
            
    def removedata(self,value):
        if self.head.data==value:
            self.removeatstart()
        currentnode=self.head
        while(currentnode!=0 and currentnode.next.data!=value):
            currentnode=currentnode.next
        if currentnode is None:
            print("index not found")
        else:
            currentnode.next=currentnode.next.next
    
    
a=linkedlist()
a.insertatbegin(90)
a.insertatend(10)
a.insertatbegin(80)
a.insertatbegin(50)
a.insertatindex(2,300)
a.removeatstart()
a.removeatend()
a.update(2,200)
a.removeatindex(2)
a.insertatbegin(10)
a.insertatend(20)
a.insertatbegin(40)
a.removedata(300)
a.traverse()

