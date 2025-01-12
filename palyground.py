class Transaction:
    def __init__(self, fee, size):
        self.fee = fee
        self.size = size
        self.priority = fee / size

class MaxHeap:
    current_size = 0 # meassures the amount of transaction in the pool 
    def __init__(self):
        self.heap = []
        self.current_size = 0

    def _heapify_up(self, i):
        parent = (i - 1) // 2
        if i > 0 and self.heap[index][0] > self.heap[parent][0]:
            self.heap[parent], self.heap[index] = self.heap[index], self.heap[parent]
            self._heapify_up 

    def _heapify_down(self, i):
        left_child = ((2*i) + 1)
        right_child = ((2*i) + 2)
        largest = i

        if left < len(self.heap) and self.heap[left][0] > self.heap[largest][0]:
            largest = left

        if right < len(self.heap) and self.heap[right][0] > self.heap[largest][0]:
            largest = right

        if largest != i:
           largest, i = i, largest
           self._heapify_down(largest)


    def insert(self, transaction):
        self.heap.append((transaction.priority, transaction.fee, transaction.size))
        self._heapify_up(len(self.heap) - 1)
        self.current_size = current_size + 1

    def extract_next_transaction(self):
        # check if the MaxHeap is empty
        if len(self.heap) <= 0:
            return None
        
        # check if it has just one value
        if len(self.heap) == 1:
            self.current_size = current_size - 1
            return self.heap.pop()
        
        max_transaction = self.heap[0]
        self.heap[0] = self.heap[-1]
        self.heap.pop()

        self.current_size = current_size - 1

        self._heapify_down(0)

        return max_transaction
