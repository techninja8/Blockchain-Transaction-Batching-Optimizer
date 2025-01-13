# A transaction is a node on our heap, basically a tuple representing transactions boradcast
class Transaction:
    def __init__(self, fee, size):
        self.fee = fee # fee of the transaction
        self.size = size # blocksize of the transaction
        self.priority = fee / size # priority would determine level on our heap

class MaxHeap:
    def __init__(self):
        self.heap = [] # our heap is represented by an array of transactions 
        self.current_size = 0 # shows how many transactions are current in our heap 

    # i is the index of the added node :)
    def _heapify_up(self, i):
        parent = (i - 1) // 2 # calculating parent index
        if i > 0 and self.heap[i][0] > self.heap[parent][0]: # as long as the node is not the root and the priority is larger than parent 
            self.heap[parent], self.heap[i] = self.heap[i], self.heap[parent]
            self._heapify_up(parent) # heapify the parent node

    def _heapify_down(self, i):
        left_child = ((2*i) + 1) 
        right_child = ((2*i) + 2)
        largest = i # we assume that larger node is the parent node (the one with index i in this context)

        if left_child < len(self.heap) and self.heap[left_child][0] > self.heap[largest][0]: # as long as node exists and priority is larger than the largest 
            largest = left_child

        if right_child < len(self.heap) and self.heap[right_child][0] > self.heap[largest][0]: # as long as node exists and the priority of the the right node is larger than largest
            largest = right_child

        if largest != i: # if the largest is not parent node, assuming on one of the children nodes, switch them and heapify 
           temp = self.heap[i]
           self.heap[i] = self.heap[largest]
           self.heap[largest] = temp 
           self._heapify_down(largest)
           


    def insert(self, transaction):
        self.heap.append((transaction.priority, transaction.fee, transaction.size)) # add new transaction to the last empty node space
        self._heapify_up(len(self.heap) - 1) # heapify recently added node
        self.current_size = self.current_size + 1 # update the node size 

    def extract_next_transaction(self):
        # check if the MaxHeap is empty
        if len(self.heap) <= 0:
            return None
        
        # check if it has just one value
        if len(self.heap) == 1:
            self.current_size = self.current_size - 1
            return self.heap.pop()
        
        # get root, which is the max_transaction, replace with last node and _heapify_dow
        max_transaction = self.heap[0]
        self.heap[0] = self.heap[-1]
        self.heap.pop()

        self.current_size = self.current_size - 1

        self._heapify_down(0) # yes, it's correct, we're heapifying the mew root which is the previous last value basically 

        return max_transaction
    
    def see_current_size(self):
        return self.current_size


# let's test this stuff!!!
