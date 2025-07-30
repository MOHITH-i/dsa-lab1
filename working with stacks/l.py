class node:
    def __init__(self, data):
        self.data = data
        self.next = None

class stack:
    def __init__(self, cap):
        self.cap = cap
        self.top = -1
        self.a = [0] * cap
    
    def isempty(self):
        return self.top < 0

    def push(self, x):
        if self.top >= self.cap - 1:
            print("Overflow")
            return False
        self.top += 1
        self.a[self.top] = x
        return True

    def pop(self):
        if self.top < 0:
            print("Underflow")
            return None
        popped = self.a[self.top]
        self.top -= 1
        return popped

    def display(self):
        if not self.isempty():
            print("The elements in the stack are:")
            for i in range(self.top, -1, -1):
                print(self.a[i], end=" ")
            print()
        else:
            print("Stack is empty")

# ✅ Object creation and method calls (must be outside the class)
s = stack(5)
s.push(10)
s.push(20)
s.push(30)
s.push(40)
s.push(50)
s.pop()
s.display()
