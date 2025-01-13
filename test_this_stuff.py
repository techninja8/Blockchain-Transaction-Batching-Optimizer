from playground import Transaction, MaxHeap

# creating a new Transaction Pool i.e. MaxHeao 
transaction_pool = MaxHeap()

# let's create a bucnh of simple transactions 
t1 = Transaction(fee=50, size=1000)
t2 = Transaction(fee=100, size=1000)
t3 = Transaction(fee=70, size=5000)

# insert this transactions into the Transaction Pool 
transaction_pool.insert(t1)
transaction_pool.insert(t2)
transaction_pool.insert(t3)

# let's get the total number of transactions in our Transaction Pool
transaction_pool.see_current_size()

# let's get the root Transaction which is the next transaction to be added to block
new_addition_to_block = transaction_pool.extract_next_transaction()
print("Max Transaction Extracted: ", new_addition_to_block)

# let's see the latest number of transactions
transaction_pool.see_current_size()





