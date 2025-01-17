import numpy as np
from playground import Transaction, MaxHeap
from concurrent.futures import ThreadPoolExecutor


def broadcast(arrival_rate, total_duration): # mathematically arrival_rate is lambda and total_duration is T 
    transaction = [] # list of transactions per time unit

    for t in range(total_duration): # run the simulation for each timestep t where t is a member of set T 
        num = np.random.poisson(arrival_rate) # define the poisson distrubition for this simulation opeartion
        for _ in range(num):
            fee = np.random.randint(10, 100) # taking fee from a uniform distrubition between 10 and 100
            size = np.random.randint(100, 1000) # taking size from a uniform distrubition between 100 and 1000
            transaction.append(Transaction(fee, size)) 
    return transaction


def parallel_execution(transaction_pool, transactions_broadcast):
    with ThreadPoolExecutor() as executor:
        list(executor.map(transaction_pool.insert, transactions_broadcast))

def prune_transactions(transaction_pool, threshold):
    # our aim here is to remove the transactions with low priority
    filtered_transactions = [
        txn for txn in transaction_pool.heap 
        if txn[0] >= threshold
    ]

    transaction_pool.heap = filtered_transactions
    for i in range(len(transaction_pool.heap)):
        transaction_pool._heapify_down(i)
    


arrival_rate = 10
duration = int(input("Duration Period: "))
threshold = 0.05

transactions_broadcast = broadcast(arrival_rate, duration) # create new transactions based on Poisson distrubition
transaction_pool = MaxHeap() # create a Transaction Pool, which is basically a max heap 

prune_transactions(transaction_pool, threshold)
parallel_execution(transaction_pool, transactions_broadcast)

print(f"Total Transactiosns Inserted: {len(transaction_pool.heap)}")

latest_transaction = transaction_pool.extract_next_transaction() # get the most optimal transaction from the transaction pool 

print("\nMax Transaction Extracted ", latest_transaction) # print out the most optimal transaction 

