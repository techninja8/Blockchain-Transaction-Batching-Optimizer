import numpy as np
from playground import Transaction, MaxHeap

def broadcast(arrival_rate, total_duration): # mathematically arrival_rate is lambda and total_duration is T 
    transaction = [] # list of transactions per time unit

    for t in range(total_duration): # run the simulation for each timestep t where t is a member of set T 
        num = np.random.poisson(arrival_rate) # define the poisson distrubition for this simulation opeartion
        for _ in range(num):
            fee = np.random.uniform(10, 100) # taking fee from a uniform distrubition between 10 and 100
            size = np.random.uniform(100, 1000) # taking size from a uniform distrubition between 100 and 1000
            transaction.append(Transaction(fee, size)) 

    return transaction

arrival_rate = 5

duration = 1



transactions_broadcast = broadcast(arrival_rate, duration)

transaction_pool = MaxHeap()

for i in transactions_broadcast:
    print(i)
    transaction_pool.insert(i)

latest_transaction = transaction_pool.extract_next_transaction()

print("\n Max Transaction Extracted ", latest_transaction)

# transaction_pool = MaxHeap()

# transaction_pool.insert(transaction_pool)

# latest_transaction = transaction_pool.extract_next_transaction()

# print(latest_transaction)

