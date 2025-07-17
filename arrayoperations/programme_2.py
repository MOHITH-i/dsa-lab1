class node:
    def __init__(self,data):
        self.data=data
        self.next=none
class LL:
    def __init__(self):
        self.head=None

def insertatbegin(self,data):
    newnode=Node(data)
    if self.head is None:
        self.head=newnode
    else:
        newnode.next=currentnode.next
    currentnode=newnode

def insertatend(self,data):
    newnode=Node(data)
    if self.head is None:
        self.head=currentnode
    while(currentnode.next!=None):
        currentnode=currenrtnode.next
    currentnode=newnode
def show(self):
    currentnode=self.head
    while(currentnode):
        print(currentnode.data,end=" ")
        currentnode.next

k = LL([10, 20, 30])
k.insert_at_begin(5)
k.insert_at_end(40)
k.show()
