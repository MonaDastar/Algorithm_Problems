class MinHeap:
    def __init__(self):
        self.heap = []

    def insert(self, value):
        self.heap.append(value)
        self._heapify_up(len(self.heap) - 1)

    def _heapify_up(self, index):
        while index > 0:
            parent_index = (index - 1) // 2
            if self.heap[index] < self.heap[parent_index]:
                # Swap the current element with its parent if it's smaller
                self.heap[index], self.heap[parent_index] = self.heap[parent_index], self.heap[index]
                index = parent_index
            else:
                break

    def display(self):
        print(self.heap)

# Example usage:
min_heap = MinHeap()
min_heap.insert(3)
min_heap.insert(5)
min_heap.insert(8)
min_heap.insert(12)
min_heap.insert(17)
min_heap.insert(20)
min_heap.insert(15)

min_heap.display()
