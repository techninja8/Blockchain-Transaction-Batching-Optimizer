from playground import Transaction, MaxHeap

# creating a new Transaction Pool i.e. MaxHeao 
transaction_pool = MaxHeap()

# let's create a bucnh of simple transactions 
t1 = Transaction(fee=1000, size=10)
t2 = Transaction(fee=100, size=1000)
t3 = Transaction(fee=70, size=500)
t4 = Transaction(fee=100, size=1000)
t5 = Transaction(fee=1000, size=500)
t6 = Transaction(fee=100000, size=10) # dummy test
t7 = Transaction(fee=100000, size=1)

print("Information of Transaction 1: ", t1, "\n") # should return string-based info of transaction 

print("Priority of Transaction is 1: ", t1.show_priority(), "\n")

print(transaction_pool)

# insert this transactions into the Transaction Pool 
transaction_pool.insert(t1)
transaction_pool.insert(t2)
transaction_pool.insert(t3)
transaction_pool.insert(t4)
transaction_pool.insert(t5)
transaction_pool.insert(t6)
transaction_pool.insert(t7)

print(transaction_pool)

block_simulation = []
# let's get the root Transaction which is the next transaction to be added to block
new_addition_to_block = transaction_pool.extract_next_transaction()
print("Max Transaction Extracted: ", new_addition_to_block, "\n")

block_simulation.append(new_addition_to_block)

new_addition_to_block = transaction_pool.extract_next_transaction()
print("Max Transaction Extracted: ", new_addition_to_block, "\n")

block_simulation.append(new_addition_to_block)

new_addition_to_block = transaction_pool.extract_next_transaction()
print("Max Transaction Extracted: ", new_addition_to_block, "\n")
block_simulation.append(new_addition_to_block)


print("Processing Block Update: ", block_simulation, "\n")


