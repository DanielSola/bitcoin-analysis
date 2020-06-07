import json

import pandas as pd
from utils import \
    get_time_between_blocks, \
    get_all_block_transactions, \
    get_transaction_values, \
    get_avg_block_size_by_hour, \
    get_hourly_transactions

from utils.plotters import \
    plot_all_block_transactions, \
    plot_block_transaction_values, \
    plot_time_diff, \
    plot_avg_block_size

if __name__ == "__main__":

    # Set dataset path
    transactions_file_path = './data/txs.json'
    blocks_file_path = './data/blocks.json'

    #Get transactions by block
    transactions_by_block = get_all_block_transactions(blocks_file_path)
    plot_all_block_transactions(transactions_by_block)

    #Get transaction values
    transaction_values_by_block = get_transaction_values(blocks_file_path, transactions_file_path)
    plot_block_transaction_values(transaction_values_by_block)

    #Get time between blocks
    time_diff = get_time_between_blocks(blocks_file_path)
    plot_time_diff(time_diff)

    #Get average block size by hour
    avg_block_sizes = get_avg_block_size_by_hour(blocks_file_path)
    plot_avg_block_size(avg_block_sizes)

    #Get hourly transactions
    #transactions_by_hour = get_hourly_transactions(transactions_file_path)

