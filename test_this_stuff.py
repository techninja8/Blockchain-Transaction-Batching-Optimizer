from playground import Transaction, MaxHeap

# creating a new Transaction Pool i.e. MaxHeao 
transaction_pool = MaxHeap()

# let's create a bucnh of simple transactions 
t1 = Transaction(fee=1000, size=10)
t2 = Transaction(fee=100, size=1000)
t3 = Transaction(fee=70, size=500)
t4 = Transaction(fee=100, size=1000)
t5 = Transaction(fee=1000, size=500)

print(t1)
# insert this transactions into the Transaction Pool 
transaction_pool.insert(t1)
transaction_pool.insert(t2)
transaction_pool.insert(t3)
transaction_pool.insert(t4)
transaction_pool.insert(t5)


# Let's see the priority of the blocks 
# transaction_pool.show_priority(t1)

# Let's see if we can see batch's current state
transaction_pool.see_batching_pool()

# let's get the total number of transactions in our Transaction Pool
print(transaction_pool.see_current_size())

# let's get the root Transaction which is the next transaction to be added to block
new_addition_to_block = transaction_pool.extract_next_transaction()
print("Max Transaction Extracted: ", new_addition_to_block)

# let's see the latest number of transactions
print(transaction_pool.see_current_size())

transaction_pool.see_batching_pool()





