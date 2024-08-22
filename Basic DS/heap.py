class Heap:
    def __init__(self):
        self.heap = []
    
    def max_heapify_down(self, index):
        largest = index
        left = 2*index + 1
        right = 2*index + 2
        left_node = self.heap[left]
        right_node = self.heap[right]
        
        if left < len(self.heap) and left_node > self.heap[largest]:
            largest = left
        if right < len(self.heap) and right_node > self.heap[largest]:
            largest = right
        #if the pointer changes, swap and recursively heapify.
        if largest != index:
            self.heap[largest], self.heap[index] = self.heap[index], self.heap[largest]
            self.max_heapify_down(largest)

    def insert(self, val):
        self.heap.append(val)
        self._heapify_up(len(self.heap)-1)

    def _heapify_up(self, index):
        parent_index = (index-1)//2

        if index > 0 and self.heap[index] > self.heap[parent_index]:
            self.heap[index], self.heap[parent_index] = self.heap[parent_index], self.heap[index]
            self._heapify_up(parent_index)

    def __str__(self):
        heap = []
        for i in self.heap:
            heap.append(i)
        return str(heap)

hp = Heap()
hp.insert(0)
hp.insert(4)
hp.insert(5)
hp.insert(6)
hp.insert(9)


print(hp)