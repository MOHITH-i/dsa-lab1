class node:
    def __init__(self,data):
        self.data=data
        self.next=None
        
class stack:
    def __init__(self):
        self.head=None
        
    def push(self,data):
        new=node(data)
        if not new:
            