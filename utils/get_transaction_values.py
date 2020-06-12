import json


def get_transaction_values(blocks_file_path, transactions_file_path):
    '''
    Returns a dictionary containing the sum of values of transactions
    for blocks.

    Ex: { block_hash: block_value }
    '''
    block_values = {}

    transaction_value_dict = get_transaction_value_dict(transactions_file_path)

    with open(blocks_file_path) as blocks_file:
        for line in blocks_file:
            block = json.loads(line)
            block_transactions = block['tx']
            block_hash = block['hash']
            block_transactions_value_sum = 0
            for id_transaction in block_transactions:
                transaction_value = transaction_value_dict[id_transaction]
                block_transactions_value_sum += transaction_value

            block_values[block_hash] = block_transactions_value_sum

    return block_values


def get_transaction_value_dict(transactions_file_path):
    '''
    Creates a dictionary with key 'transaction_id' and value 'transaction_value'
    to allow fast search of transaction values.

    Ex: { "cd903eeee6b909148d80e19b66fe8f4d32628e63e82f6b67627cf31f58321c2c": 53.566192259999994 }
    '''

    transaction_values_dict = {}

    with open(transactions_file_path) as transactions_file:
        for line in transactions_file:
            transaction = json.loads(line)
            transaction_id = transaction['txid']
            transaction_vout = transaction['vout']
            transaction_value = 0

            for vout in transaction_vout:
                transaction_value += vout['value']

            transaction_values_dict[transaction_id] = transaction_value

    return transaction_values_dict
