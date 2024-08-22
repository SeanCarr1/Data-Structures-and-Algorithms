class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

class Stack:
    def __init__(self):
        self.head = None
        self.size = 0
    
    def is_empty(self):
        return self.head is None
    
    def push(self, item):
        new_node = Node(item)
        new_node.next = self.head
        self.head = new_node
        self.size += 1
    
    def pop(self):
        if self.is_empty():
            raise IndexError("Stack is empty.")
        item = self.head
        self.head = self.head.next
        self.size -= 1
        return item
    
    def peek(self):
        if self.is_empty():
            raise IndexError("Stack is empty")
        return self.head.val
    
    def size(self):
        return self.size
    
    def __str__(self):
        stack = []
        head = self.head
        while head:
            stack.append(head.val)
            head = head.next
        return str(stack)
    
stack = Stack()
stack.push(5)
stack.push(4)
stack.push(2)
stack.push(1)
print(stack)