class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

class Queue:
    def __init__(self):
        self.front = None
        self.rear = None
        self.size = 0
    
    def __str__(self):
        queue = []
        current_node = self.front
        while current_node:
            queue.append(current_node.val)
            current_node = current_node.next
        return str(queue)
    
    def is_empty(self):
        return True if self.size == 0 else False
    
    def enqueue(self, val):
        node = Node(val)
        if self.rear:
            self.rear.next = node
        else: self.rear = node

        if not self.front:
            self.front = self.rear

        self.size += 1
    
    def dequeue(self):
        if self.is_empty():
            raise IndexError("Queue is empty. Invalid input")
        
        front_node_val = self.front.val
        self.front = self.front.next
        if not self.front:
            self.rear = None
        self.size -= 1
        return front_node_val
    
    def peek(self):
        if not self.front:
            raise IndexError("Queue is empty. Invalid input")
        return self.front.val
        