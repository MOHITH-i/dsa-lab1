class CircularQueue:
    def __init__(self, size=4):
        self.size = size
        self.queue = [None] * size
        self.front = -1
        self.rear = -1

    def is_full(self):
        return (self.rear + 1) % self.size == self.front

    def is_empty(self):
        return self.front == -1

    def enqueue(self, data):
        if self.is_full():
            print("Queue is full! Cannot enqueue", data)
            return
        if self.is_empty():
            self.front = 0
        self.rear = (self.rear + 1) % self.size
        self.queue[self.rear] = data
        self.print_queue("enqueue", data)

    def dequeue(self):
        if self.is_empty():
            print("Queue is empty! Cannot dequeue.")
            return None
        removed = self.queue[self.front]
        self.queue[self.front] = None
        if self.front == self.rear:
            self.front = -1
            self.rear = -1
        else:
            self.front = (self.front + 1) % self.size
        print(f"Operation: dequeue\nRemoved: {removed}")
        self.print_queue()
        return removed

    def print_queue(self, operation=None, data=None):
        if operation and data is not None:
            print(f"Operation: {operation} {data}")
        print(f"Queue: {self.queue} front={self.front} rear={self.rear}\n")

cq = CircularQueue()

cq.enqueue(1)
cq.enqueue(2)
cq.enqueue(3)
cq.dequeue()
cq.enqueue(4)
cq.enqueue(5) 

