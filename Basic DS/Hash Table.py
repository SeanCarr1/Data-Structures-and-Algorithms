#insert, search, delete, 
class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.next = None

class HashTable:
    def __init__(self, size):
        self.size = size
        self.table = [None]*size
    
    def hash_func(self, key):
        return hash(key) % self.size
    
    def insert(self, key, value):
        index = self.hash_func(key)
        new_node = Node(key, value)
        
        if self.table[index] is None:
            self.table[index] = new_node
            return
        
        current = self.table[index]
        while current:
            if current.key == key:
                current.value = value
                return
            if current.next == None:
                current.next = new_node
                return
            current = current.next
        
    def search(self, key):
        index = self.hash_func(key)
        current = self.table[index]
        while current:
            if current.key == key:
                return current.val
            else: current = current.next
        raise KeyError(f"key: {key} not found")
    
    def delete(self, key):
        index = self.hash_func(key)
        temp_node = self.table[index]
        prev = None

        while temp_node:
            if temp_node.key == key: #if head, link head to next. if not head, link prev node to curr.next
                if prev == None:
                    self.table[index] = temp_node.next
                else: prev.next = temp_node.next

                return
            
            prev = temp_node
            temp_node = temp_node.next
        
        return KeyError(f"key: {key} does not exist.")
    
    def __str__(self):
        result = []
        for i in range(self.size):
            current = self.table[i]
            chain = []
            while current:
                chain.append((current.key, current.val))
                current = current.next
            result.append(chain)
        return str(result)
                

ht = HashTable(10)
ht.insert("sean", 19)
print(ht)


