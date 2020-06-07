import json

import pandas as pd
from utils import get_avg_block_size, get_all_block_transactions
from utils.plotters import plot_all_block_transactions

if __name__ == "__main__":

    # Set dataset path
    transactions_file_path = './data/txs.json'
    blocks_file_path = './data/blocks.json'

    #Get transactions by block
    transactions_by_block = get_all_block_transactions(blocks_file_path)
    plot_all_block_transactions(transactions_by_block)
