import json


def get_all_block_transactions(blocks_file_path):
    """
    Return the number of transactions for blocks in
        the file in a dictionary
    """
    transaction_counts = {}

    with open(blocks_file_path) as blocks_file:
        for line in blocks_file:

            block = json.loads(line)
            block_transactions = block['tx']
            block_hash = block['hash']
            transaction_counts[block_hash] = len(block_transactions)

    return transaction_counts
