import json


def get_hourly_transactions(transactions_file_path):
    """
    Return the time between blocks in a file.
    """
    hourly_transactions = {}
    with open(transactions_file_path) as transactions_file:
        for line in transactions_file:
            transaction = json.loads(line)
            transaction_time = transaction['time']
            print(transaction_time)

    return hourly_transactions
