import numpy as np
from playground import Transaction, MaxHeap

def broadcast(arrival_rate, total_duration): # mathematically arrival_rate is lambda and total_duration is T 
    transaction = [] # list of transactions per time unit

    for t in range(total_duration): # run the simulation for each timestep t where t is a member of set T 
        num = np.random.poisson(arrival_rate) # define the poisson distrubition for this simulation opeartion
        for _ in range(num):
            fee = np.random.randint(10, 100) # taking fee from a uniform distrubition between 10 and 100
            size = np.random.randint(100, 1000) # taking size from a uniform distrubition between 100 and 1000
            transaction.append(Transaction(fee, size)) 
    return transaction

arrival_rate = 10

duration = int(input("Duration Period: "))

# update_time = duration / 3

transactions_broadcast = broadcast(arrival_rate, duration) # create new transactions based on Poisson distrubition

transaction_pool = MaxHeap() # create a Transaction Pool, which is basically a max heap 

block = []

transaction_count = 0
for i in transactions_broadcast:
    print(i) # sepearate transactions and print them out
    transaction_pool.insert(i) # input the individual transactions into the transaction pool 
    transaction_count = transaction_count + 1

print("Total Number of Transactions in ", duration, " minutes Equals: ", transaction_count)

latest_transaction = transaction_pool.extract_next_transaction() # get the most optimal transaction from the transaction pool 

# for i in range(update_time):
#    block.append(latest_transaction)

# print("\nMax Transaction Extracted ", latest_transaction) # print out the most optimal transaction 

